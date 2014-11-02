import requests
from graph import DirectedGraph


class GitHubAPI:
    def __init__(self, username, depth):
        self.username = username
        self.depth = depth
        self.graph = DirectedGraph()
        self.following_users = []

    def get_following_for(self, name):
        self.following_users = requests.get("https://api.github.com/users/{}/following".format(name))
        print(self.following_users.json())
        return self.following_users

    def following(self, name):
        following_users = self.get_following_for(name)
        following_names = []
        for i in range(len(following_users.json())):
            print(len(following_users.json()))
            following_names.append(following_users.json()[i]["login"])
        return following_names

    def build_graph(self, name):
        neighbors = self.following(name)
        for neighbor in neighbors:
            self.graph.add_edge(name, neighbor)
        print(self.graph)


g = GitHubAPI("RadoRado", 1)
g.get_following_for("RadoRado")