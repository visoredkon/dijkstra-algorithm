from DijkstraAlgorithm.Graph import Graph

from DijkstraAlgorithm.Dijkstra import Dijkstra

graph = Graph()

graph.add_vertex("A", "B", "C", "D", "E", "F", "G", "I")

graph.add_edge(from_vertex="A", to_vertex="B", weight=16)
graph.add_edge(from_vertex="A", to_vertex="C", weight=3)
graph.add_edge(from_vertex="A", to_vertex="D", weight=10)

graph.add_edge(from_vertex="B", to_vertex="D", weight=2)
graph.add_edge(from_vertex="B", to_vertex="I", weight=8)

graph.add_edge(from_vertex="C", to_vertex="B", weight=12)
graph.add_edge(from_vertex="C", to_vertex="E", weight=7)

graph.add_edge(from_vertex="D", to_vertex="F", weight=6)

graph.add_edge(from_vertex="E", to_vertex="B", weight=6)
graph.add_edge(from_vertex="E", to_vertex="G", weight=5)

graph.add_edge(from_vertex="F", to_vertex="I", weight=6)

graph.add_edge(from_vertex="G", to_vertex="F", weight=5)
graph.add_edge(from_vertex="G", to_vertex="I", weight=8)

dijkstra = Dijkstra(graph)

path, weight = dijkstra.find_path(start="A", finish="I")

print(f"Shortest path: {path}\nWeight: {weight}")
