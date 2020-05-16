class DynamicArray:

    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * 8

    def insert(self, index, value):
        """
        Insert object before index.
        """
        # Check if there's room in storage
        if self.count >= self.capacity:
            self.double_size()

        # Shift everything to the right of the index
        # Start from the end to prevent overwriting vals
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        # Insert `value`
        self.storage[index] = value

        # Increment count
        self.count += 1

    def append(self, value):
        if self.count >= self.capacity:
            self.double_size()

        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        """
        Double size of storage
        Copy items from old storage to new
        """
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


if __name__ == "__main__":
    arr = DynamicArray()

    print(arr.storage)
    arr.insert(0, "z")
    arr.insert(0, "y")
    arr.insert(0, "x")
    arr.insert(0, "w")
    print(arr.storage)
    arr.append("a")
    arr.append("b")
    arr.append("c")
    arr.append("d")
    print(arr.storage)
    arr.append("e")
    print(arr.storage)
