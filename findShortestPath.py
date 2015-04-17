'''
Created on Apr 11, 2015

@author: NGUYEN TRAN
'''
import random

class find_shortest_distance:
        
    def make_graph_uniform_cost(self):
        #myrand = random.randint(0,1000) #this is uniform cost
        
        mygraph = {
                    'a' : set(['b','c']),
                    'b' : set(['a','d','e']),
                    'c' : set(['a','f']),
                    'd' : set(['b']),
                    'e' : set(['b','f']),
                    'f' : set(['c','e'])
                  }
        return mygraph
        
    def make_graph_non_uniform_positive_cost(self):
        mylist = [random.randint(0,1000) for x in range(12)]
        
        mygraph = {
                    'a' : {'b' : mylist[0], 'd' : mylist[1], 'e' :mylist[2]},
                    'b' : {'a' : mylist[3], 'c' : mylist[4]},
                    'c' : {'b' : mylist[5], 'd' : mylist[6]},
                    'd' : {'a' : mylist[7], 'c' : mylist[8], 'e' : mylist[9]},
                    'e' : { 'a' : mylist[10], 'd' : mylist[11]}      
                  }
        return mygraph
    
    def make_graph_non_uniform_positive_negative_cost(self):
        mylist = [random.randint(-20,20) for x in range(12)]
        
        mygraph = {
                    'a' : {'b' : mylist[0], 'd' : mylist[1], 'e' :mylist[2]},
                    'b' : {'a' : mylist[3], 'c' : mylist[4]},
                    'c' : {'b' : mylist[5], 'd' : mylist[6]},
                    'd' : {'a' : mylist[7], 'c' : mylist[8], 'e' : mylist[9]},
                    'e' : { 'a' : mylist[10], 'd' : mylist[11]}      
                  }
        return mygraph
    
    def DFS_iterative(self,mygraph,start):
        '''Graph transversal using DFS - iterative method
            stack data structure & while loop
            Need to mark visited node by adding visited list'''
        visited,stack = set(),[start] #start with empty set of visited node, and list of start in stack
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(mygraph[node] - visited)
        return visited
    
    def DFS_recursive(self,mygraph,start,visited=None):
        '''Use recursive method to traverse the graph in DFS
            stack data structure & for loop'''
        #Base case
        if visited == None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            self.DFS_recursive(mygraph,next,visited)
        return visited

    def dfs_paths_iterative(self,mygraph,start,goal):
        '''Use DFS to find path with uniform positive cost.
            Run time = (|V| - worst space + |E| - worst performance)'''
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                        stack.append((next, path + [next]))
                        
    def dfs_paths_recursive(self,mygraph,start,goal,path=None):
        '''use DFS to find path from start to goal with uniform cost
            worst space = |V| and worst performance = |E|'''
        #base case
        if path == None:
            path = [start]
        
        if start == goal:
            return path
            
        for neighbor in mygraph[start] - set(path):
            mypath = self.dfs_paths_recursive(mygraph,neighbor,goal,path + [neighbor])
            if mypath != None:
                print mypath
    
    def bfs_traverse_iterative(self,mygraph,start):
        visited, queue = set(),[start]
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(mygraph[node] - visited)
                
        return visited
        
    def bfs_path_iterative(self,mygraph,start,goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in mygraph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append([next, path+[next]])
                    
    def bfs_shortest_path(self,mygraph,start,goal):
        '''find shortest path from start to goal with uniform cost
            worst space = |V| and worst performance = |E|'''
        try:
            return next(self.bfs_path_iterative(mygraph, start, goal))
        except StopIteration:
            return None
        
if __name__ == '__main__':
    fsd = find_shortest_distance()
    graph = fsd.make_graph_uniform_cost()
    print fsd.DFS_iterative(graph, 'a')
    print fsd.DFS_recursive(graph, 'a')
    print list(fsd.dfs_paths_iterative(graph, 'a', 'f'))
    fsd.dfs_paths_recursive(graph, 'a', 'f')
    #----------------------------------------------------#
    print fsd.bfs_traverse_iterative(graph, 'a')
    print list(fsd.bfs_path_iterative(graph, 'a', 'f'))
    print fsd.bfs_shortest_path(graph, 'a', 'f')
        
        
        