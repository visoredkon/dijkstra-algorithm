import networkx as nx
from matplotlib import pyplot as plt
from tabulate import tabulate

from DijkstraAlgorithm.Graph import Graph


class Dijkstra:
    def __init__(self, graph):
        if not isinstance(graph, Graph):
            raise Exception("Graph must be an instance of the Graph class.")

        self.__graph = graph

        self.__distances = {
            vertex: float("infinity") for vertex in self.__graph.get_vertices()
        }
        self.__paths = {vertex: [] for vertex in self.__graph.get_vertices()}
        self.__visited = set()
        self.__previous = {vertex: None for vertex in self.__graph.get_vertices()}

        self.__superscript_map = dict(zip("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))

    def __reinitialize(self):
        self.__table_header = ["Visited"] + [
            f"   {vertex}   " for vertex in self.__graph.get_vertices()
        ]
        self.__table_data = []
        self.__temp = []

        self.__distances = {
            vertex: float("infinity") for vertex in self.__graph.get_vertices()
        }
        self.__paths = {vertex: [] for vertex in self.__graph.get_vertices()}
        self.__visited = set()
        self.__previous = {vertex: None for vertex in self.__graph.get_vertices()}

    def find_path(self, start, finish):
        self.__reinitialize()

        self.__distances[start] = 0
        self.__previous[start] = start

        for _ in self.__graph.get_vertices():
            unvisited_vertices = set(self.__distances) - self.__visited
            current = min(unvisited_vertices, key=self.__distances.get)
            current_edges = self.__graph.get_edges()[current]

            for edge in current_edges:
                vertex_to, weight = edge["to"], edge["weight"]
                new_distance = self.__distances[current] + weight

                if self.__distances[vertex_to] > new_distance:
                    self.__distances[vertex_to] = new_distance
                    self.__paths[vertex_to] = self.__paths[current] + [current]
                    self.__previous[vertex_to] = current

            self.__visited.add(current)
            self.__append_table_data(current)

        return (
            self.__formatted_table(),
            " → ".join(self.__paths[finish] + [finish]),
            self.__distances[finish],
        )

    def __append_table_data(self, current):
        self.__table_data.append(
            [current]
            + [
                self.__format_table_data(vertex, weight, current)
                for vertex, weight in self.__distances.items()
            ]
        )

    def __format_table_data(self, vertex, weight, current):
        if vertex == current and weight != float("infinity"):
            self.__temp.append(vertex)
            return f"|{''.join(self.__superscript_map[i] for i in str(weight))}{self.__previous[vertex]}|"

        if vertex in self.__temp:
            return " "

        return (
            "∞"
            if weight == float("infinity")
            else f" {''.join(self.__superscript_map[i] for i in str(weight))}{self.__previous[vertex]} "
        )

    def __formatted_table(self):
        return tabulate(
            self.__table_data,
            headers=self.__table_header,
            stralign="center",
            numalign="center",
            tablefmt="rounded_grid",
        )

    def visualize_graph(self, finish):
        G = self.__build_networkx_graph()

        plt.figure("Dijkstra Algorithm", figsize=(10, 5))

        layout_position = nx.spring_layout(G, seed=28)
        edge_labels = nx.get_edge_attributes(G, "weight")

        for i, title in zip(
            [121, 122], ["Graph Before Dijkstra", "Graph After Dijkstra"]
        ):
            self.__draw_graph(G, layout_position, edge_labels, i, title)
            if i == 122:
                self.__highlight_shortest_path(G, layout_position, finish)

        plt.tight_layout()
        plt.show()

    def __build_networkx_graph(self):
        G = nx.Graph()

        G.add_edges_from(
            [
                (vertex, edge["to"], {"weight": edge["weight"]})
                for vertex in self.__graph.get_vertices()
                for edge in self.__graph.get_edges()[vertex]
            ]
        )

        return G

    def __draw_graph(self, G, position, edge_labels, subplot_index, title):
        plt.subplot(subplot_index)
        plt.title(title)

        nx.draw(G, position, with_labels=True)
        nx.draw_networkx_edge_labels(G, position, edge_labels=edge_labels)

    def __highlight_shortest_path(self, G, position, finish):
        shortest_path = self.__paths[finish] + [finish]
        shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))

        nx.draw_networkx_edges(
            G, position, edgelist=shortest_path_edges, edge_color="red", width=2
        )
