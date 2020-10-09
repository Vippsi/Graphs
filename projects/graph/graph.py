"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Init the stack
        s = Stack()
        # Init the set for the visited nodes
        visited = set()

        # add the starting node(vert) to the tack
        s.push(starting_vertex)

        while s.size() > 0:
            # grab the first item in the stack
            v = s.pop()

            if v not in visited:
                # if that vert has not been visited, add it to the visited set
                print(v)
                visited.add(v)
                # Grab the neighbors for the given vertex
                for neighbor in self.get_neighbors(v):
                    # add them to the stack to be processed
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None:
            visited = set()
        
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue([starting_vertex])
        print("starting vertex", q.enqueue([starting_vertex]))

        while q.size() > 0:
            path = q.dequeue()
            print("Path --> ", path)
            last_vert = path[-1]


            if last_vert == destination_vertex:
                return path
            
            for next_to in self.get_neighbors(last_vert):
                new_path = list(path)
                new_path.append(next_to)
                print("new path -->", new_path)
                q.enqueue(new_path)

        """def bfs(self, starting_vertex_id, target_vertex_id):
		# Create an empty queue and enqueue A PATH TO the starting vertex ID
		# Create a Set to store visited vertices
		# While the queue is not empty...
			# Dequeue the first PATH
			# Grab the last vertex from the PATH
			# If that vertex has not been visited...
				# CHECK IF IT'S THE TARGET
				  # IF SO, RETURN PATH
				# Mark it as visited...
				# Then add A PATH TO its neighbors to the back of the queue
				  # COPY THE PATH
				  # APPEND THE NEIGHBOR TO THE BACK """

    def dfs(self, starting_vertex, destination_vertex, visited=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = []
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                path.append(v)

                if v == destination_vertex:
                    return path
                
                for next_to in self.get_neighbors(v):
                    s.push(next_to)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex == destination_vertex:
            return visited + [starting_vertex]
        
        else:
            visited.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                if edge not in visited:
                    path = self.dfs_recursive(edge, destination_vertex, visited)
                    if path:
                        return path
            visited.remove(starting_vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
