import random
import os
import sys
sys.path.append('../graph')
from util import Queue
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.calls = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        self.calls += 1
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return True
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        
        if num_users < avg_friendships:
            print("The number of users must be greater than the average number of friendships.")
            return

        # Add users
        self.users = set()
        for i in range(1, num_users + 1):
            self.users.add(i)
        
        # Create friendships
        # Non-stretch version, O(n^2)
        # friendship_population = []
        for i in self.users:
            self.friendships[i] = set()
        #     friends = {*self.users}
        #     friends.remove(i)
        #     friendship_population += [[i,f] for f in friends]

        
        # random.shuffle(friendship_population)
        
        total_friendships = num_users * avg_friendships

        # Stretch 2 O(n) maybe.
        while total_friendships > 0:
            user_1 = random.randint(1, num_users)
            user_2 = random.randint(1, num_users)
            while user_2 == user_1:
                user_2 = random.randint(1, num_users)
            if user_2 not in self.friendships[user_1]:
                self.add_friendship(user_1, user_2)
                total_friendships -= 2
        

        # def add_friendship1(friend_pair):
        #     nonlocal total_friendships
        #     if friend_pair[1] in self.friendships[friend_pair[0]]:
        #         return
        #     else:
        #         self.friendships[friend_pair[0]].add(friend_pair[1])
        #         self.friendships[friend_pair[1]].add(friend_pair[0])
        #         total_friendships -= 2

        # while total_friendships > 0:
        #     if friendship_population[-1][0] < friendship_population[-1][1]:
        #         self.add_friendship(friendship_population[-1][0], friendship_population[-1][1])
        #         total_friendships -= 2
        #     friendship_population.pop(len(friendship_population) - 1)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        def bfs(starting_vertex, destination_vertex):
            q = Queue()
            q.enqueue([starting_vertex])
            visited_bfs = set()
            while q.size() > 0:
                last_path = q.dequeue()
                last_v = last_path[-1]
                if last_v not in visited_bfs:
                    if last_v == destination_vertex:
                        return last_path
                    visited_bfs.add(last_v)
                    for n in self.friendships[last_v]:
                        new_path = [*last_path]
                        new_path.append(n)
                        q.enqueue(new_path)
        for u in self.users:
            visited[u] = bfs(user_id, u)
            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(sg.calls)