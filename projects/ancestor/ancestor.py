class Graph:
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
    


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



def earliest_ancestor(ancestors, starting_node):
    
    g = Graph()

    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])

        g.add_edge(i[1], i[0])

    q = Queue()

    q.enqueue([starting_node])


    max_path = 1
    earliest = -1

    while q.size() > 0:
        path = q.dequeue()

        # IF the path is longer or equal than max_path and the value is smaller than earliest or if the path is longer, then max_path, return earliest
        v = path[-1]
        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)

        for neighbor in g.vertices[v]:
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)
    
    return earliest
