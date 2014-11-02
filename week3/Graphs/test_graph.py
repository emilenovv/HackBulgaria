from graph import DirectedGraph
import unittest


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.my_graph = DirectedGraph()

    def test_init(self):
        self.assertEqual(self.my_graph.nodes, {})

    def test_addEdge(self):
        self.my_graph.addEdge("Emil", "Galin")
        self.assertEqual(self.my_graph.nodes, {"Emil": ["Galin"], "Galin": []})

    def test_getNEighbours(self):
        self.my_graph.addEdge("Emil", "Galin")
        self.my_graph.addEdge("Emil", "Pesho")
        self.my_graph.addEdge("Galin", "Atanas")
        self.my_graph.addEdge("Atanas", "Dimitrichka")
        self.assertEqual(self.my_graph.getNeighboursFor("Emil"), ["Galin", "Pesho"])

    def test_pathBetween_true(self):
        self.my_graph.addEdge("Emil", "Galin")
        self.my_graph.addEdge("Emil", "Pesho")
        self.my_graph.addEdge("Galin", "Atanas")
        self.my_graph.addEdge("Atanas", "Dimitrichka")
        self.assertTrue(self.my_graph.pathBetween("Emil", "Dimitrichka"))

    def test_pathBetween_false(self):
        self.my_graph.addEdge("Emil", "Galin")
        self.my_graph.addEdge("Emil", "Pesho")
        self.my_graph.addEdge("Galin", "Atanas")
        self.my_graph.addEdge("Atanas", "Dimitrichka")
        self.assertFalse(self.my_graph.pathBetween("Atanas", "Emil"))

    def test_pathBetween_cycle(self):
        self.my_graph.addEdge("Emil", "Galin")
        self.my_graph.addEdge("Emil", "Pesho")
        self.my_graph.addEdge("Galin", "Atanas")
        self.my_graph.addEdge("Atanas", "Dimitrichka")
        self.my_graph.addEdge("Dimitrichka", "Emil")
        print(self.my_graph)
        self.assertTrue(self.my_graph.pathBetween("Emil", "Dimitrichka"))

if __name__ == '__main__':
    unittest.main()