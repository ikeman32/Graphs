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
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:
            current_node = q.dequeue()

            if current_node not in visited:
                print(current_node)
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a shtack
        stack = Stack()
        # push on our starting node
        stack.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()

        # while our stack isn't empty
        while  stack.size() > 0:
            ## pop off whatever's on top, this is current_node
            current_node = stack.pop()
            
            ## if we haven't visited this vertex before
            if current_node not in visited:
                ### run function / print
                print(current_node)
                ### mark as visited
                visited.add(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors
                for neighbor in neighbors:
                    #### add to our stack
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = []):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        visited.append(starting_vertex)
        print(starting_vertex)

        for vertice in self.vertices[starting_vertex]:
            
            if vertice not in visited:#Base Case
                self.dft_recursive(vertice, visited)
        
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        
        path = [starting_vertex]

        q.enqueue(path)
        visited = set()

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:

                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)
                
                for neighbor in neighbors:
                    copy_path = current_path[:]
                    copy_path.append(neighbor)
                    q.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        path = [starting_vertex]

        stack.push(path)

        visited = set()

        while stack.size() > 0:
            current_path = stack.pop()

            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    copy_path = current_path[:]
                    copy_path.append(neighbor)
                    stack.push(copy_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited =set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)

        if starting_vertex == destination_vertex:
            return path
        if len(path) == 0:
            path.append(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        for neighbor in neighbors:
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
                if result is not None:
                    return result

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
