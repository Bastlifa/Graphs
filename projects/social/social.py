import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

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
        friendship_population = []
        for i in self.users:
            self.friendships[i] = set()
            friends = {*self.users}
            friends.remove(i)
            friendship_population += [[i,f] for f in friends]

        # print(friendship_population)
        random.shuffle(friendship_population)
        # print(friendship_population)
        total_friendships = num_users * avg_friendships

        def add_friendship(friend_pair):
            nonlocal total_friendships
            if friend_pair[1] in self.friendships[friend_pair[0]]:
                return
            else:
                self.friendships[friend_pair[0]].add(friend_pair[1])
                self.friendships[friend_pair[1]].add(friend_pair[0])
                total_friendships -= 2

        while total_friendships > 0:
            add_friendship(friendship_population[-1])
            friendship_population.pop(len(friendship_population) - 1)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
