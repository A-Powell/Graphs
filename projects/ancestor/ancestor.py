from util import Queue


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print("ERROR: Vertext does not exist")


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for a in ancestors:
        g.add_vertex(a[0])
        g.add_vertex(a[1])
        g.add_edge(a[1], a[0])

    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    early = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if (v < early) or (len(path) > 1):
                early = v
        for neighbor in g.get_neighbors(v):
            copy = path.copy()
            copy.append(neighbor)
            q.enqueue(copy)
    return early
