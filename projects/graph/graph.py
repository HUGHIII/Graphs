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
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('Missing vertex')

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
        # breadth first use queue
        # set queue class init to variable q
        # make empty set
        # queue the starting vertex

        # while there is anything in the queue run loop
        # set variable 'v' for element to remove from queue
        # if variable 'v' (element being dequeued) is not in 'visited' set
        # add it to the set 'visited'

        # still inside 'if' statement in while scope, iterate through each neighbor of 'v' -the element being dequeued and enqueue them, this repeats in loop until queue is empty

        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size():
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)

                for EAneighbor in self.get_neighbors(v):
                    q.enqueue(EAneighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.


        instead of queue like breadth first trsversal uses, depthft uses a stack.
        data follows a single route all of the way until that routes end then reroutes to nearest route and does the same until stack is clear
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)

        while s.size():
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)

                for EAneighbor in self.get_neighbors(v):
                    s.push(EAneighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        like bft use queue and visited set, keep track of PATH SO FAR for each node and do that in q, so enqueue path so far rather than single vertices.
        so add next neighbors by breadth but along with the vertices that led to it.
        use last entry in path list to determine where to go next
        # each vertex queued destination has its own path-list - [c,b,D] [c,b,F] [c,b,A]
        
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        while q.size():
            path = q.dequeue()
            print(path)
            v = path[-1]
            print(v)
            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.add(v)

                for EAneighbor in self.get_neighbors(v):
                    q.enqueue(path + [EAneighbor])



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size():
            path = s.pop()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v == destination_vertex:
                    return path

                for EAneighbor in self.get_neighbors(v):
                    s.push(path + [EAneighbor])
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


# g = Graph()

# g.add_vertex('0')
# g.add_vertex('1')
# g.add_vertex('2')
# g.add_vertex('3')
# g.add_edge('0', '1')
# g.add_edge('1', '0')
# g.add_edge('0', '3')
# g.add_edge('3', '0')
# print(g.vertices)
# print(g.get_neighbors("0"))


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
