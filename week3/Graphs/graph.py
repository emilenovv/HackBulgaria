class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node_a, node_b):
        if node_a in self.nodes:
            self.nodes[node_a].append(node_b)
        else:
            self.nodes[node_a] = []
            self.nodes[node_a].append(node_b)

        if node_b not in self.nodes:
            self.nodes[node_b] = []

    def get_neighbours_for(self, node):
        return self.nodes[node]

    def path_between(self, node_a, node_b):
        if node_a not in self.nodes or node_b not in self.nodes:
            return False
        elif node_b in self.get_neighbours_for(node_a):
            return True
        for node in self.get_neighbours_for(node_a):
            if self.path_between(node, node_b):
                return True
        return False

    def __str__(self):
        results = []
        for node in self.nodes:
            results.append(str(node) + " follows: " + str(self.nodes[node]))
        return str(results)
