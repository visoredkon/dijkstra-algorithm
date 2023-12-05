class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, *vertices):
        for vertex in vertices:
            if vertex in self.vertices:
                raise Exception(
                    f"The vertex {vertex} is already within the graph's vertices."
                )
            self.vertices.append(vertex)
            self.edges[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            raise Exception(
                "Invalid edge. One or more vertices do not exist in the graph."
            )

        self.edges[from_vertex].append({"to": to_vertex, "weight": weight})

    def __str__(self):
        return str(self.edges)
