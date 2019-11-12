import sys


# Instructions
HLT = 0b00000001  # Exit opcode
LDI = 0b10000010  # Set op_a register to value op_b
PRN = 0b01000111  # Print
MUL = 0b10100010  # Multiply: ALU operation


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 255
        self.reg = [0] * 8
        self.pc = 0

        self.dispatch_table = {}
        self.dispatch_table[HLT] = self.handle_HLT
        self.dispatch_table[LDI] = self.handle_LDI
        self.dispatch_table[PRN] = self.handle_PRN
        self.dispatch_table[MUL] = self.handle_MUL

    def handle_HLT(self):
        sys.exit(0)  # Successful exit

    def handle_PRN(self):
        op_a = self.ram_read(self.pc+1)
        print(self.ram[op_a])

    def handle_MUL(self):
        # Read values to multiply
        op_a = int(self.ram_read(self.pc+1))  # RAM Register a
        op_b = int(self.ram_read(self.pc+2))  # RAM Register b
        # Copy values to ALU register
        self.reg[op_a] = self.ram_read(op_a)
        self.reg[op_b] = self.ram_read(op_b)
        # Perform ALU computation, overwrite RAM register op_a
        self.ram_write(op_a, self.alu("MUL", op_a, op_b))

    def handle_LDI(self):
        op_a = int(self.ram_read(self.pc+2))  # Value in base10
        op_b = int(self.ram_read(self.pc+1))  # Register in base10
        self.ram_write(op_b, op_a)

    def load(self):
        """Load a program into memory."""
        program = []
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            for line in f:
                if line[:8].isnumeric():
                    command = int(line[:8], 2)
                    program.append(command)
        f.close()

        address = 0
        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR
        return

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")
        return self.reg[reg_a]

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            # Instruction register
            IR = self.ram[self.pc]

            # Calculate PC increment value: get high bits 6 & 7
            operand_count = IR >> 6
            instr_len = operand_count + 1

            # Dispatch table
            self.dispatch_table[IR]()
            self.pc += instr_len
