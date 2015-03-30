'''
Created on Mar 29, 2015

@author: NGUYEN TRAN
'''
import os
import time

class Numbers:
    def __init__(self,filename):
        self.myfile = filename
    
    def matrixMul(self,A,B):
        C = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000
        return C
    
    def fastExponentiation(self,A,n):
        #print a,n
        if n == 0:
            return 1
        if n == 1:
            return A
        if n % 2 == 0:
            A1 = self.fastExponentiation(A, n/2)
            return self.matrixMul(A1,A1)
        else:
            return self.matrixMul(A, self.fastExponentiation(A, n-1))
    
    def solve(self,n):
        A = [[3,5],[1,3]]
        A_n = self.fastExponentiation(A, n)
        return (A_n[0][0]*2 + 999)%1000
    
    def normalExponentiation(self,a,n):
        return a**n

    def readInput(self):
        try:
            with open (self.myfile,'r') as f:
                total = 0
                for line in f:
                    line = line.strip()
                    if total == 0:
                        total = int(line)
                        m = total - 1
                        continue
                    n = int(line)
                    output = str(self.solve(n))
                    #add leading zero if necessary
                    if len(output) == 2:
                        output = "0" + output
                    elif len(output) == 1:
                        output = "0" +"0"+output
                    with open ('numbers-large.out', 'a+') as w:
                        w.writelines("Case #%d: %s\n" % (total-m,output))
                    #print "Case #%d: %s" % (total-m,output)
                    m -= 1
        except IOError:
            print "Can't read %s" % (self.myfile)

os.chdir('numbers')
mynumber = Numbers('C-large-practice.in')
start = time.clock()
mynumber.readInput()
print time.clock() - start, "seconds"