'''
Created on May 19, 2015

@author: Chris Tran
'''
import os

class LoadTest:
    def __init__(self,inputfile):
        self.input = inputfile
        
    def solveLoadTest(self,L,P,C):
        count = 0
        
        #Binary dividing / Binary multiplying
        #Has 1 load test left, we need to find L*C >= X & X*C >= P =>L*C**2 >= P to know if X exists
        #Has 2 load tests left, we need L*C**4 >= P. This is because when we have 1 load test, reduce to L*C**2 >= P (like above)
        #Has 3 load tests left, L*C**8 >= P
        while(L*(C**(2**count)) < P):
            count += 1
            
        return count
    
    def readInput(self):
        try:
            with open (self.input, 'r') as f:
                with open ('LoadTest-large.out', 'a+') as w:
                    total = 0
                    for line in f:
                        line = line.strip()
                        if total == 0:
                            total = int(line)
                            n = total - 1
                            continue
                        (L,P,C) = line.split(' ')
                        #print ("Case #%s: %s") % (total - n, self.solveLoadTest(int(L),int(P),int(C)))
                        w.writelines("Case #%d: %s\n" % (total - n, self.solveLoadTest(int(L),int(P),int(C))))
                        n -= 1
        except IOError:
            print "Can't open %s" % (self.input)
            
os.chdir('load_test')
myLoadTest = LoadTest('B-large-practice.in')
myLoadTest.readInput()
                    

