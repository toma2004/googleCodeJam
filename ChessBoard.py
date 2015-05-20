'''
Created on May 19, 2015

@author: NguyenTran
'''
import os

class ChessBoard:
    def __init__(self,inputfile):
        self.myfile = inputfile
    
    def makeGrid(self,m,n,mygrid):
        matrix = [[0 for i in range(n)] for j in range(m)]
        #Fill in matrix
        for i in range(m):
            j = n-1
            if mygrid:
                #temp = bin(int(mygrid.pop(),16))[2:]
                temp = int(mygrid.pop(0),16)
                while(temp > 0):
                    if temp & 1 == 1:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
                    j -= 1
                    temp = temp >> 1;
            else:
                print "Error: not enough rows"     
        return matrix
    
    def findLargestChessBoard(self,m,n,matrix):
        '''Use DP to calculate the largest square whose
            bottom-right cornor is (i,j)'''
        larg = [[1 for i in range(n)] for j in range (m)]
        for i in range(m):
            for j in range(n):
                #check condition
                if (i-1 >= 0) and (j-1 >= 0):
                    if(matrix[i-1][j] != matrix[i][j] and matrix[i][j-1] != matrix [i][j] and matrix[i-1][j-1] == matrix[i][j]):
                        larg[i][j] = 1 + min(larg[i-1][j],larg[i][j-1],larg[i-1][j-1])
        
        print larg
    
    def readInput(self):
        try:
            with open(self.myfile, 'r') as f:
                total = 0
                readGrid = 0
                mygrid = []
                for line in f:
                    line = line.strip()
                    if total == 0:
                        total = int(line)
                        n = total - 1
                        continue
                    if not readGrid:
                        readGrid = 1
                        m,n = line.split(' ')
                        m = int(m)
                        n = int(n)
                        temp = m
                    else:
                        mygrid.append(line)
                        temp -= 1
                        if temp == 0:
                            #call function to solve mygrid
                            mymatrix = self.makeGrid(m, n, mygrid)
                            self.findLargestChessBoard(m, n, mymatrix)
                            #reset to read in new grid
                            readGrid = 0
                            mygrid[:] = []
        except IOError:
            print "Can't open this file %s" % self.myfile

os.chdir('Chess_board')
mychessboard = ChessBoard('small.txt')
mychessboard.readInput()