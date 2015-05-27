'''
Created on May 21, 2015

@author: NguyenTran
'''
import os
import time

class RankPure:    
    def __init__(self,inputfile):
        self.myinput = inputfile

    def pureIwithJelements(self,C,MOD,nmax):
        '''use DP to calculate count[N,K] where N is the number {2...N}
           with K elements. Formula used: count[N,K] = count[K,K'] * C[N-K-1][K-K'-1]'''
        count = [[0] * nmax for i in range(nmax)]
        for i in range (0,nmax):
            for j in range(0,nmax):
                if i == 0 or j == 0:
                    count[i][j] = 0
                elif j == 1:
                    count[i][j] = 1
                elif j >= i:
                    count[i][j] = 0
                else:
                    mycount = 0
                    for x in xrange(1, j):
                        mycount += count[j][x] * C[i - j - 1][j - x - 1]
                        mycount %= MOD
                    count[i][j] = mycount
        return count

    def chooseJoutofI(self,MOD,nmax):
        '''put the combination calculation into a matrix
           Choose j elements out of i objects '''
        C = [[0] * nmax for i in range(nmax)]
        for i in range (0,nmax):
            for j in range(0,nmax):
                if i == 0:
                    if j == 0:
                        C[i][j] = 1
                    else:
                        C[i][j] = 0
                else:
                    if j > i:
                        C[i][j] = 0
                    else:
                        C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
        return C 

    def readInput(self):
        try:
            with open (self.myinput,'r') as f:
                with open('rank_pure-large.out', 'a+') as w:
                    MOD = 100003
                    nmax = 512
                    C = self.chooseJoutofI(MOD,nmax)
                    count = self.pureIwithJelements(C, MOD, nmax)
                    sol = 0
                    isFirstLine = 1     
                    total = 0
                    for line in f:
                        line = line.strip()
                        if total == 0:
                            total = int(line)
                            atemp = total - 1
                            continue
                        n = int(line)
                        for i in range(1,n):
                            sol += count[n][i]
                            sol %= MOD
                        if not isFirstLine:
                            w.writelines("\nCase #%d: %s" % (total -atemp, sol))
                        else:
                            w.writelines("Case #%d: %s" % (total -atemp, sol))
                            isFirstLine = 0
                        atemp -= 1
                        sol = 0
        except IOError:
            print "Can't open this file %s" % self.myinput
            
os.chdir('rank_pure')
myrankpure = RankPure('C-large-practice.in')
start = time.clock()
myrankpure.readInput()
print time.clock() - start, "seconds"