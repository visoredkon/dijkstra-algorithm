class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

        self.distances = {vertex: float("infinity") for vertex in self.graph.vertices}
        self.paths = {vertex: [] for vertex in self.graph.vertices}
        self.visited = set()

    def find_path(self, start, finish):
        self.distances[start] = 0

        for _ in self.graph.vertices:
            current_vertex = min(
                set(self.distances) - self.visited, key=self.distances.get
            )

            if current_vertex == finish:
                continue

            current_edge = self.graph.edges[current_vertex].copy()

            for _ in range(len(current_edge)):
                current_visited = min(current_edge, key=lambda x: x["weight"])

                current_weight = current_visited["weight"]
                current_vertex_distance = self.distances[current_vertex]
                next_vertex_distance = self.distances[current_visited["to"]]

                if next_vertex_distance > current_vertex_distance + current_weight:
                    self.distances[current_visited["to"]] = (
                        current_vertex_distance + current_weight
                    )
                    self.paths[current_visited["to"]] = self.paths[current_vertex] + [
                        current_vertex
                    ]

                current_edge.remove(current_visited)

            print(current_vertex, self.distances)

            self.visited.add(current_vertex)

        return self.paths[finish] + [finish], self.distances[finish]
