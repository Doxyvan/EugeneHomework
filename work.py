class Vertex():

    _links = []
    def __init__(self, name) -> None:
        self.name = name

    @property
    def links(self):
        return self._links

    def __repr__(self) -> str:
        return self.name

class Link():
    _dist = 1

    def __init__(self, v1:Vertex, v2:Vertex) -> None:
        self._v1 = v1
        self._v2 = v2

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2
    
    @property
    def dist(self):
        return self._dist
    
    @dist.setter
    def dist(self, value):
        self._dist = value

class LinkedGraph():
    _links = []
    _vertex = []

    def add_vertex(self, v):
        self._vertex.append(v)
    
    def add_link(self, link):
        exist_links = [set([x.v1, x.v2]) for x in self._links]
        if set([link.v1, link.v2]) not in exist_links:
            self._links.append(link)
            if link.v1 not in self._vertex:
                self._vertex.append(link.v1)
            if link.v2 not in self._vertex:
                self._vertex.append(link.v2)
    
    def find_path(self, start_v, stop_v):
        distances = dict([(x, 9999999999) for x in self._vertex if x != start_v])
        distances[start_v]=0
        visited = dict([(x, False) for x in self._vertex])
        print(distances)
        print(exist_links)
        while False in visited.values():
            exist_links = dict([tuple([x.v2, x.dist]) for x in self._links if (x.v1 == start_v)])
            for i in exist_links:
                distances[i] = min(exist_links[i], distances[i])
            visited[start_v] = True

            

        
map_graph = LinkedGraph()

v1 = Vertex("v1")
v2 = Vertex("v2")
v3 = Vertex("v3")
v4 = Vertex("v4")
v5 = Vertex("v5")
v6 = Vertex("v6")
v7 = Vertex("v7")

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

map_graph.find_path(v1, v6)