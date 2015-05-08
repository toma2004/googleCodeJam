'''
Created on Apr 24, 2015

@author: NguyenTran
'''
from __future__ import division
from macpath import curdir

class Queue:
    def __init__(self):
        self.myqueue = []
        
    def enqueue(self,item):
        #need to insert in front of list
        self.myqueue.insert(0, item)
        
    def dequeue(self):
        return self.myqueue.pop()
    
    def isEmpty(self):
        return self.myqueue == []
    
    def size(self):
        return len(self.myqueue)
    
    def peek(self):
        return self.myqueue[-1]
    
class BinaryHeap:
    #When implement a heap, we don't care about first element. Therefore, initialize it to None
    def __init__(self):
        self.myheap = [None]
        self.heapsize = 0
        
    def insert(self,item):
        self.myheap.append(item)
        self.heapsize += 1
        #need to reserve heap propery. This operation takes O (log n)
        self.upheap(self.heapsize)
        
    def upheap(self,size):
        while size // 2 > 0: #while there is still a parent to current node
            parent_index = size // 2
            if self.myheap[size] < self.myheap[parent_index]:
                self.myheap[size],self.myheap[parent_index] = self.myheap[parent_index],self.myheap[size]
            size = size // 2
    
    def delMin(self):
        try:
            mymin = self.myheap[1]
            self.heapsize -= 1
            self.myheap[1] = self.myheap[-1]
            #remove last item as it's replaced the first item
            self.myheap.pop()
            #re-construct heap to reserve its property. This will take O (log n)
            self.downheap(1)
            return mymin
        except IndexError:
            print "There is not root in the heap\n"
    
    def downheap(self,index):
        while(index << 1) <= self.heapsize:
            minchild = self.findMinChild(index)
            if self.myheap[index] > self.myheap[minchild]:
                self.myheap[index],self.myheap[minchild] = self.myheap[minchild],self.myheap[index]
            index = minchild
        
    def findMinChild(self,i):
        if (i << 1) + 1 > self.heapsize:
            return (i << 1)
        else:
            if self.myheap[i<<1] < self.myheap[(i<<1)+1]:
                return i<<1
            else:
                return (i<<1) + 1
        
    def printHeap(self):
        print self.myheap

class PriorityQueue:
    #When implement a heap, we don't care about first element. Therefore, initialize it to None
    def __init__(self,pq):
        self.myPQueue = pq
        self.heapsize = 0
        
    def insert(self,item):
        self.myPQueue.append(item)
        self.heapsize += 1
        #need to reserve heap propery. This operation takes O (log n)
        self.upheap(self.heapsize)
        
    def upheap(self,size):
        while size // 2 > 0: #while there is still a parent to current node
            parent_index = size // 2
            if self.myPQueue[size][0] < self.myPQueue[parent_index][0]:
                self.myPQueue[size],self.myPQueue[parent_index] = self.myPQueue[parent_index],self.myPQueue[size]
            size = size // 2
    
    def delMin(self):
        try:
            mymin = self.myPQueue[1]
            self.heapsize -= 1
            self.myPQueue[1] = self.myPQueue[-1]
            #remove last item as it's replaced the first item
            self.myPQueue.pop()
            #re-construct heap to reserve its property. This will take O (log n)
            self.downheap(1)
            return mymin
        except IndexError:
            print "There is not root in the heap\n"
    
    def downheap(self,index):
        while(index << 1) <= self.heapsize:
            minchild = self.findMinChild(index)
            if self.myPQueue[index][0] > self.myPQueue[minchild][0]:
                self.myPQueue[index],self.myPQueue[minchild] = self.myPQueue[minchild],self.myPQueue[index]
            index = minchild
        
    def findMinChild(self,i):
        if (i << 1) + 1 > self.heapsize:
            return (i << 1)
        else:
            if self.myPQueue[i<<1][0] < self.myPQueue[(i<<1)+1][0]:
                return i<<1
            else:
                return (i<<1) + 1
        
    def printHeap(self):
        print self.myPQueue

###########################################
#Node class for use in LinkedList and Tree#
###########################################
class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    
    def insert_node(self,node):
        #insert node at the beginning of the list
        if not self.head:
            self.head = node
        else:
            node.nextNode = self.head
            self.head = node
            
    def search_linkedlist(self, value):
        if self.head.value == value:
            return self.head
        else:
            cur = self.head.nextNode
            while cur:
                if cur.value == value:
                    return cur
                cur = cur.nextNode
            return None
    
    def delete_node(self,node):
        if self.head == node:
            self.head = self.head.nextNode
            return 1
        else:
            prev = self.head
            cur = self.head.nextNode
            while cur:
                if cur == node:
                    prev.nextNode = cur.nextNode
                    return 1
                cur = cur.nextNode
                prev = prev.nextNode
        return 0
            
    def print_linkedList(self):
        if not self.head:
            return None
        cur = self.head
        while cur:
            if cur.nextNode:
                print '{%s}->' % cur.value,
            else:
                print '{%s}' % cur.value
            cur = cur.nextNode
                
if __name__ == "__main__":
    test_linkedlist = 1
    if test_linkedlist:
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        my_linkedlist = LinkedList()
        my_linkedlist.insert_node(n1)
        my_linkedlist.insert_node(n2)
        my_linkedlist.insert_node(n3)

        my_linkedlist.print_linkedList()
        my_linkedlist.delete_node(n2)
        my_linkedlist.print_linkedList()
        
    else:
        myheap = BinaryHeap()
        myheap.insert(5)
        myheap.insert(2)
        myheap.insert(7)
        myheap.insert(1)
        myheap.printHeap()
        
        print "After delete Min operation"
        print "My min in heap =", myheap.delMin()
        myheap.printHeap()
        #################
        print "Testing Priority Queue"
        pq = [None]
        myPQ = PriorityQueue(pq)
        myPQ.insert((5,'v'))
        myPQ.insert((2,'b'))
        myPQ.insert((7,'n'))
        myPQ.insert((1,'m'))
        myPQ.printHeap()
        print "Delete min"
        print "My min =",myPQ.delMin()
        myPQ.printHeap()