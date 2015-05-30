'''
Created on May 29, 2015

@author: Chris Tran
'''
from __future__ import division
import os
import time

class MakeItSmooth:
    def __init__(self,inputfile):
        self.myinput = inputfile
    
    def solve(self,d,i,m,n,pixel):
        '''solve the problem by getting the min of deleting an element
           or changing it and inserting'''
        sol = [0 for j in range(256)]
        temp = [0 for j in range(256)]
        
        for j in range(n):
            temp,sol = sol,temp
            for k in range(256):
                cost = temp[k] + d #cost of prev + delete
                change_cost = abs(pixel[j] - k) #|final_value - prev_value|
                if cost > change_cost: #check for insertion costs
                    for l in range(256): #try all possible values of q
                        if m == 0 and l != k:
                            continue
                        val = temp[l]
                        if l != k:
                            val += (abs(l-k)-1) // m * i #cost of inserting after changing value
                        if cost > change_cost+val:
                            cost = change_cost+val
                sol[k] = cost
        return min(sol[j] for j in range(256))
            
    def readInput(self):
        try:
            with open (self.myinput,'r') as f:
                with open ('make_it_smooth-large.out', 'a+') as w:
                    total = 0
                    isRead = 0
                    pixel = []
                    isFirstLine = 1
                    for line in f:
                        line = line.strip()
                        if total == 0:
                            total = int(line)
                            atemp = total - 1
                            continue
                        if not isRead:
                            d,i,m,n = map(int,line.split(' '))
                            isRead = 1
                            continue
                        line = map(int,line.split(' '))
                        for j in range(n):     
                            pixel.append(line[j])
                        if isFirstLine:
                            w.writelines("Case #%d: %s" % (total - atemp, self.solve(d, i, m, n, pixel)))
                            isFirstLine = 0
                        else:
                            w.writelines("\nCase #%d: %s" % (total - atemp, self.solve(d, i, m, n, pixel)))
                        atemp -= 1
                        isRead = 0
                        pixel[:] = []
        except IOError:
            print "Can't read file %s" % self.myinput
            
os.chdir('make_it_smooth')
myMakeItSmooth = MakeItSmooth('B-large-practice.in')
start = time.clock()
myMakeItSmooth.readInput()
print time.clock() - start, "seconds"                    