class Graph:
    def __init__(self):
        self.__vertices = []
        self.__edges = {}

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def add_vertex(self, *vertices):
        for vertex in vertices:
            if vertex in self.__vertices:
                raise Exception(
                    f"The vertex {vertex} is already within the graph's vertices."
                )
            self.__vertices.append(vertex)
            self.__edges[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.__vertices or to_vertex not in self.__vertices:
            raise Exception(
                "Invalid edge. One or more vertices do not exist in the graph."
            )

        self.__edges[from_vertex].append({"to": to_vertex, "weight": weight})

    def __str__(self):
        return str(self.__edges)
