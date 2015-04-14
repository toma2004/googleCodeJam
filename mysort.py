'''
Created on Apr 8, 2015

@author: Chris Tran
'''
import random
import time

class mysort:        
    def mergeSort(self,alist):
        '''Merge sort a list. Big O (n log n)'''
        #base case
        if len(alist) <= 1:
            return
        
        mid = int(len(alist) / 2)
        left = alist[:mid]
        right = alist[mid:]
        
        self.mergeSort(left)
        self.mergeSort(right)
        
        self.mergeTwoList(alist,left,right)
        
    def mergeTwoList(self,mylist,alist,blist):
        alen = len(alist)
        blen = len(blist)
        index_a = 0
        index_b = 0
        index_mylist = 0
        
        while index_a < alen and index_b < blen:
            if alist[index_a] <= blist[index_b]:
                mylist[index_mylist] = alist[index_a]
                index_mylist += 1
                index_a += 1
            else:
                mylist[index_mylist] = blist[index_b]
                index_mylist += 1
                index_b += 1
                
        #check for left over
        while index_a < alen:
            mylist[index_mylist] = alist[index_a]
            index_mylist += 1
            index_a += 1
            
        while index_b <blen:
            mylist[index_mylist] = blist[index_b]
            index_mylist += 1
            index_b += 1
    
    def quickSort(self,alist,first,last):
        '''Quick sort a list. Average Big O (n log n) with worst case is O (n2)'''
        if first < last:
            index_pivot = self.partition(alist,first,last)
            self.quickSort(alist,first,index_pivot-1)
            self.quickSort(alist,index_pivot+1,last)
            
    def partition(self,alist,first,last):
        mypivot = alist[first] #Assume the first value is pivot
        
        left_index = first+1
        right_index = last
    
        done = False
        while not done:
            while left_index <= right_index and alist[left_index] <= mypivot:
                left_index += 1
         
            while alist[right_index] >= mypivot and right_index >= left_index:
                #right_index = right_index -1
                right_index -= 1
                 
            if right_index < left_index:
                done = True
            else:
                alist[left_index],alist[right_index] = alist[right_index],alist[left_index]
                        
        alist[first],alist[right_index] = alist[right_index],mypivot
        return right_index

#test
if __name__ == "__main__":
    test_list = []
    for x in range(100000):
        test_list.append(random.randint(0,1000))
    quick_list = test_list[:]
    test_sort = mysort()
    print "Using Merge Sort"
    start = time.clock()
    test_sort.mergeSort(test_list)
    print "Time it takes to complete merge sort is ", time.clock() - start
    
    print "Using Quick Sort"
    start = time.clock()
    test_sort.quickSort(quick_list,0,len(quick_list)-1)
    print "Time it takes to complete quick sort is ", time.clock() - start

