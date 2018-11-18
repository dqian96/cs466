# approximation for weighted vertex cover

# Define Vertex and Edge data types (adjacency list representation)
class Vertex(object):
    def __init__(self, neighbors, w):
        """A vertex contains a list of references to other vertices (neighbors) and an weight (w)."""
        self.neighbors = neighbors
        self.w = w

class Edge(object):
    def __init__(self, u, v):
        """An edge contains two references to its endpoint vertices."""
        self.u = u
        self.v = v

def weighted_vertex_cover(vertices, edges):
    """Finds an approx min weighted vertex cover given a list of vertices and a list of edges (i.e. Graph)."""
    for e in edges:
        # O(|E|)
        if e.u.w == 0 or e.v.w == 0: continue
        x = min(e.u.w, e.v.w)
        e.u.w -= x
        e.v.w -= x

    cover = [None] * len(vertices)  # preallocate array of size - O(|V|)
    i = 0
    for v in vertices:
        if v.w == 0:
            cover[i] = v
            i += 1

    return cover

