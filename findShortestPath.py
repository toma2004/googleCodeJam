'''
Created on Apr 11, 2015

@author: NGUYEN TRAN
'''
import random

class find_shortest_distance:
    def __init__(self,mygraph):
        self.mygraph = mygraph
        
    def make_graph_uniform_cost(self,num_nodes):
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
        '''Use BFS to find shortest path with uniform positive cost.
            Run time = (|V| - worst space + |E| - worst performance) 
            Need to mark visited node by adding visited list'''
        visited,stack = set(),[start] #start with empty set of visited node, and list of start in stack
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(mygraph[start] - visited)
        return visited
        
        
        