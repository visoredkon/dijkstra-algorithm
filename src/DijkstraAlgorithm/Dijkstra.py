import networkx as nx
from matplotlib import pyplot as plt

from tabulate import tabulate


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {vertex: float("infinity") for vertex in self.graph.vertices}
        self.paths = {vertex: [] for vertex in self.graph.vertices}
        self.visited = set()
        self.previous = {vertex: None for vertex in self.graph.vertices}

    def find_path(self, start, finish):
        self.distances[start] = 0
        self.previous[start] = start

        superscript_map = {
            "0": "⁰",
            "1": "¹",
            "2": "²",
            "3": "³",
            "4": "⁴",
            "5": "⁵",
            "6": "⁶",
            "7": "⁷",
            "8": "⁸",
            "9": "⁹",
        }

        table_header = [f"   {vertex}   " for vertex in self.graph.vertices]
        table_header.insert(0, "Visited")
        table_data = []

        for _ in self.graph.vertices:
            unvisited = set(self.distances) - self.visited
            current_vertex = min(unvisited, key=self.distances.get)

            current_edge = self.graph.edges[current_vertex]

            for vertex in current_edge:
                vertex_to = vertex["to"]
                vertex_weight = vertex["weight"]

                new_distance = self.distances[current_vertex] + vertex_weight

                if self.distances[vertex_to] > new_distance:
                    self.distances[vertex_to] = new_distance
                    self.paths[vertex_to] = self.paths[current_vertex] + [
                        current_vertex
                    ]
                    self.previous[vertex_to] = current_vertex

            self.visited.add(current_vertex)
            table_data.append([current_vertex])
            [
                table_data[-1].append(
                    "".join(superscript_map[i] for i in str(weight))
                    + self.previous[vertex]
                    if weight != float("infinity")
                    else "∞"
                )
                for vertex, weight in self.distances.items()
            ]

        table = tabulate(
            table_data,
            headers=table_header,
            stralign="center",
            numalign="center",
            tablefmt="rounded_grid",
        )

        return table, " → ".join(self.paths[finish] + [finish]), self.distances[finish]

    def draw_graph(self, finish):
        G = self._create_graph()
        plt.figure("Dijkstra Algorithm", figsize=(10, 5))
        pos = nx.spring_layout(G, seed=28)
        edge_labels = nx.get_edge_attributes(G, "weight")

        for i, title in zip(
            [121, 122], ["Graph Before Dijkstra", "Graph After Dijkstra"]
        ):
            self._plot_graph(G, pos, edge_labels, i, title)
            if i == 122:
                self._highlight_shortest_path(G, pos, finish)

        plt.tight_layout()
        plt.show()

    def _create_graph(self):
        G = nx.Graph()
        G.add_edges_from(
            [
                (vertex, edge["to"], {"weight": edge["weight"]})
                for vertex in self.graph.vertices
                for edge in self.graph.edges[vertex]
            ]
        )

        return G

    def _plot_graph(self, G, pos, edge_labels, i, title):
        plt.subplot(i)
        plt.title(title)

        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    def _highlight_shortest_path(self, G, pos, finish):
        shortest_path = self.paths[finish] + [finish]
        shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))

        nx.draw_networkx_edges(
            G, pos, edgelist=shortest_path_edges, edge_color="red", width=2
        )
