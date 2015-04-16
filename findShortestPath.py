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
        '''Use DFS to find shortest path with uniform positive cost.
            Run time = (|V| - worst space + |E| - worst performance)'''
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                        stack.append((next, path + [next]))

            
        
        
if __name__ == '__main__':
    fsd = find_shortest_distance()
    graph = fsd.make_graph_uniform_cost()
    print fsd.DFS_iterative(graph, 'a')
    print fsd.DFS_recursive(graph, 'a')
    print list(fsd.dfs_paths_iterative(graph, 'a', 'f'))
        
        
        