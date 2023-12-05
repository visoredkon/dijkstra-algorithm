from tabulate import tabulate


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

        self.distances = {vertex: float("infinity") for vertex in self.graph.vertices}
        self.paths = {vertex: [] for vertex in self.graph.vertices}
        self.visited = set()

    def find_path(self, start, finish):
        self.distances[start] = 0

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

            self.visited.add(current_vertex)
            table_data.append([current_vertex])
            [table_data[-1].append(f"{weight}") for _, weight in self.distances.items()]

        table = tabulate(
            table_data,
            headers=table_header,
            stralign="center",
            numalign="center",
            tablefmt="rounded_grid",
        )

        return table, " → ".join(self.paths[finish] + [finish]), self.distances[finish]
