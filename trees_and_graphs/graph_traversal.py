class Graph:
    def __init__(self):
        self.graph = dict()
        self.dfs_output = list()
        self.bfs_output = list()

    def add_edge(self,to_vertex,from_vertex):
        if to_vertex in self.graph:
            self.graph[to_vertex].append(from_vertex)
        else:
            self.graph[to_vertex] = [from_vertex]

    def print_graph(self):
        print(self.graph)

    def dfs_traversal(self, root):
        if root not in self.dfs_output:
            self.dfs_output.append(root)
        temp = self.graph[root]
        for node in temp:
            if(node not in self.dfs_output):
                self.dfs_traversal(node)


    def bfs_traversal(self, root):
        queue = list()
        queue.append(root)
        while(queue):
            temp = queue.pop(0)
            self.bfs_output.append(temp)
            child_temp = self.graph[temp]
            for i in child_temp:
                if i not in self.bfs_output and i not in queue:
                    queue.append(i)

    def print_bfs_traversal(self):
        print(self.bfs_output)


    def print_dfs_traversal(self):
        print(self.dfs_output)

    def find_route(self, u, v):
        temp = self.graph[u][:]
        if v in temp:
            print("path_exist")
            return
        else:
            if u in temp:
                temp.remove(u)
            if temp:
                for i in temp:
                    self.find_route(i, v)
            else:
                print("path does not exist")



g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.print_graph()
g.dfs_traversal(2)
g.print_dfs_traversal()
g.bfs_traversal(2)
g.print_bfs_traversal()
g.find_route(0,2)
g.find_route(3,1)
g.find_route(3,3)
g.find_route(1,3)
g.find_route(1,1)

