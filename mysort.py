'''
Created on Apr 8, 2015

@author: Chris Tran
'''
import random

class mysort:
    def mytest(self,alist):
        alist.sort()
        
    def mergeSort(self,alist):
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
            
#test
if __name__ == "__main__":
    test_list = []
    for x in range(10):
        test_list.append(random.randint(0,1000))
    print "My unsorted list: " , test_list
    test_sort = mysort()
    test_sort.mergeSort(test_list)
    print "My sorted list: " , test_list