class Graph():
    '''Graph ADT implementation: simple, undirected, weighted.
    For non-simple uses, multiple edges should work but self-loops might break it.'''

    # The Graph is implemented as a dictionary of vertices,
    # where each vertex is a key and the value is a set of neighbors.
    # Each neighbor is a tuple of (vertex, weight).
    # The Graph is undirected, so each edge is represented twice.
    def __init__(self, V=(), E=()):
        '''Initializes a Graph with optional sets of vertices V and edges E'''
        self._vertices = set() # this attribute seems redundant
        self._nbrs = dict()

        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)
        
    def add_vertex(self, v):
        '''Adds vertex v to the Graph'''
        # Check if it already exists so I don't overwrite it in the dict
        if v not in self:
            self._vertices.add(v)
            self._nbrs[v] = set()

    def remove_vertex(self, v):
        '''Removes vertex v from the Graph. 
        Raises a KeyError if v is not a vertex in the Graph'''
        # Remove all edges incident to this vertex v, if any
        # Let a KeyError bubble up if v is not in the graph
        for vertex, weight in self._nbrs[v].copy(): # I'm not sure why this breaks when I don't use .copy()
            self.remove_edge(v, vertex, weight)

        # Remove the vertex. 
        del self._nbrs[v]
        self._vertices.remove(v)

    def add_edge(self, u, v =None, wt =None):
        '''Adds undirected edge between u and v with weight wt to the graph.
        Will accept a tuple of the 2 vertices and weight as a single argument.'''
        # Check if the edge is given as a tuple
        if not v and not wt:
            # If so, unpack it
            u, v, wt = u

        # Make sure both vertices of the edge are in the Graph too
        self.add_vertex(u)
        self.add_vertex(v)

        # Since the Graph is undirected, add both vertices as neighbors for each other
        self._nbrs[u].add((v, wt))
        self._nbrs[v].add((u, wt))

    def remove_edge(self, u, v =None, wt =None):
        '''Removes undirected edge between u and v with weight wt from the graph
        Raises a KeyError if such an edge is not in the Graph,
        however it will accept a tuple of the 2 vertices and weight as a single argument.
        Does not remove the vertices. '''
        # Check if the edge is given as a tuple
        if not v and not wt:
            u, v, wt = u
        
        # Let a KeyError bubble up if u or v are not in the graph
        self._nbrs[u].remove((v, wt))
        self._nbrs[v].remove((u, wt))
    
    def nbrs(self, v, isWeighted =False):
        """Returns an iterator over a set of neighbors of vertex v.
        If isWeighted is False, returns an iterable of a set of vertices.
        If isWeighted is True, returns an iterable of a set of tuples of (neighbor, weight).
        Raises a KeyError if v is not in the graph."""
        if isWeighted:
            return iter(self._nbrs[v])
        return iter({nbr[0] for nbr in self._nbrs[v]}) 
        # if v not in self:
        #     raise KeyError(v)
        # for nbr in self._neighbors(v).copy():
        #     yield nbr[0] # should this return the weight too?
    
    def __len__(self):
        '''Returns the number of vertices in the graph.'''
        return len(self._vertices)
    def __contains__(self, v):
        '''Returns True/False if the vertex v is/isn't in the graph.'''
        return v in self._vertices
    def __iter__(self):
        '''Return an iterator over the Graph's vertices'''
        return iter(self._vertices)

    def __repr__(self):
        '''Return a string representation of the Graph'''
        s = ""
        for v in self._vertices:
            s += str(v) + ': ' + str(self._nbrs[v]) + "\n"
        return s

    def independent_set(self, visited =set()):
        '''Returns a maximum independent set of the Graph'''

        # find the set of vertices not yet visited
        vertices = self._vertices - visited - {nbr[0] for v in visited for nbr in self._nbrs[v]}

        # Base case: if there are no vertices left, return 0
        if not vertices:
            return visited, 0
        
        # Recursive case: find the vertex with the highest score
        # from recursing on all the remaining vertices
        scores = {}
        for v in vertices:
            scores[v] = 1 + self.independent_set(visited | {v})[1]

        # find the max in scores and save it
        max_score, vertex = 0, None
        for key, val in scores.items():
            if val > max_score:
                max_score = val
                vertex = key
        visited.add(vertex)
        return visited, max_score


import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        '''Initialize a basic Graph of 5 cities and 7 edges'''
        '''
                        1250 mi             1778 mi
        San Francisco ----------- Denver ---------- New York
                    \                | \                |
                     \               |  \               |
                      \              |   \              | 
                       \             |    \             |
                        \     794 mi |     \ 1404 mi    |
                         \           |      \           | 864 mi
                1730 mi   \          |       \          |
                           \         |        \         |
                            \        |         \        |
                             \       |          \       |
                              \      |           \      |
                               Dallas ----------- Atlanta
                                        781 mi
        '''
        self.n = 5
        self.vertices = ('San Francisco', 'Denver', 'New York', 'Dallas', 'Atlanta')
        self.edges = (('San Francisco', 'Denver', 1250), 
                      ('San Francisco', 'Dallas', 1730),
                      ('Denver', 'New York', 1778),
                      ('Denver', 'Dallas', 794), 
                      ('Denver', 'Atlanta', 1404),
                      ('New York', 'Atlanta', 864),
                      ('Atlanta', 'Dallas', 781),
                      )
        self.g = Graph(self.vertices, self.edges)

    def test_init(self):
        '''Test that the Graph is initialized correctly'''
        # Check vertices
        self.assertTrue('San Francisco' in self.g)
        self.assertTrue('Denver' in self.g)
        self.assertTrue('New York' in self.g)
        self.assertTrue('Atlanta' in self.g)
        self.assertTrue('Dallas' in self.g)

        # Check neighbors
        self.assertEqual({nbr for nbr in self.g.nbrs('San Francisco')}, 
                         {'Denver', 'Dallas'})
        self.assertEqual({nbr for nbr in self.g.nbrs('Denver')}, 
                         {'San Francisco', 'New York', 'Dallas', 'Atlanta'})
        self.assertEqual({nbr for nbr in self.g.nbrs('New York')}, 
                         {'Denver', 'Atlanta'})
        self.assertEqual({nbr for nbr in self.g.nbrs('Atlanta')}, 
                         {'New York', 'Denver', 'Dallas'})
        self.assertEqual({nbr for nbr in self.g.nbrs('Dallas')}, 
                         {'San Francisco', 'Denver', 'Atlanta'})

        # Check length
        self.assertEqual(len(self.g), self.n)

    def test_ind_set(self):
        '''Test that the independent set algorithm works'''
        visited, score = self.g.independent_set()
        print(visited, score)
        self.assertEqual(len(visited), score)
        self.assertEqual(score, 2)

unittest.main()