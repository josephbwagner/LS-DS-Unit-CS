from pprint import pprint
import random
import time

from util import Stack, Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID]\
             or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.lastID += 1  
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # call addUser() until numUsers
        for i in range(numUsers):
            self.addUser(f'User {i+1}')

        # Create random friendships
        possibleFriendships = []
        # Avoid dups by ensuring unique IDs
        for userID in self.users:
            for friendID in range(userID+1, self.lastID+1):
                possibleFriendships.append((userID, friendID))

        # Shuffle the list
        random.shuffle(possibleFriendships)

        # Slice totalFriendships from the front to create friendships
        totalFriendships = avgFriendships * numUsers // 2
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # To get ALL paths, use BFS (with a Queue)
        q = Queue()
        q.enqueue([userID])
        visited = {}

        # As long as there are users not pop()ed into visited
        while q.size() > 0:
            # Initialize `path` from Queue
            path = q.dequeue()
            user = path[-1]

            # If `user` not visited yet:
            if user not in visited:
                visited[user] = path

                # Enqueue new `friend`s
                for friend in self.friendships[user]:
                    if friend not in visited:
                        path_copy = path.copy()
                        path_copy.append(friend)
                        q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraph(1000, 5)
    end_time = time.time()
    print(f"runtime: {end_time - start_time} seconds")
    connections = sg.getAllSocialPaths(1)

    total = 0
    for userID in connections:
        total += len(connections[userID]) - 1
    print(len(connections))
    print(total / len(connections))

    totalConnections = 0
    totalDegrees = 0
    iterations = 10
    for i in range(0, iterations):
        sg.populateGraph(1000, 5)
        connections = sg.getAllSocialPaths(1)
        total = 0
        for userID in connections:
            total += len(connections[userID]) - 1
        totalConnections += len(connections)
        totalDegrees += total / len(connections)
        print("-----")
        print(f"Friends in network: {len(connections)}")
        print(f"Avg degrees: {total / len(connections)}")
    print(totalConnections / iterations)
    print(totalDegrees / iterations)
