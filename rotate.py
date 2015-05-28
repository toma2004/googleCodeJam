'''
Created on May 27, 2015

@author: Chris Tran
'''
import os

class Rotate:
    def __init__(self,myinputfile):
        self.myinput = myinputfile
    
    def rotate_90Clockwise_dropdown_Gravity(self,aMatrix,n):
        '''rotate 90 degrees clockwise and dropdown due to gravity
           is the same as push everything to the right'''
        for i in range(n):
            x = n - 1
            for j in range(n-1,-1,-1):
                if (aMatrix[i][j] != '.'):
                    aMatrix[i][x] = aMatrix[i][j]
                    x -= 1
            while (x >= 0):
                aMatrix[i][x] = '.'
                x -= 1
    
    def check_winner(self,aMatrix,n,k):
        '''Check to see if there is a winner after rotate and gravity'''
        winner = None
        redHasWon = 0
        blueHasWon = 0
        for i in range(n):
            for j in range(n):
                if redHasWon and blueHasWon:
                    break
                if aMatrix[i][j] != '.':
                    if redHasWon and aMatrix[i][j] == 'R':
                        continue
                    elif blueHasWon and aMatrix[i][j] == 'B':
                        continue
                    winner = self.check_winner_helper(aMatrix,i,j,n,k)
                    if winner == 'R':
                        redHasWon = 1
                    elif winner == 'B':
                        blueHasWon = 1
        
        if redHasWon and blueHasWon:
            return "Both"
        elif redHasWon:
            return "Red"
        elif blueHasWon:
            return "Blue"
        else:
            return "Neither"
    
    def check_winner_helper(self,aMatrix,i,j,n,k):
        left = 1
        right = 1
        bottom = 1
        top = 1
        diag1 = 1
        diag2 = 1
        count = 1
        temp_i = i
        temp_j = j
        if i == 0:
            top = 0
            if j == 0:
                left = 0
                diag2 = 0
            elif j == n -1:
                right= 0
                diag1 = 0
        elif i == n-1:
            bottom = 0
            if j == 0:
                left = 0
                diag1 = 0
            elif j == n-1:
                right = 0
                diag2 = 0
        done = 0
        while not done:
            count = 1
            if left or right:
                if left:
                    temp_j=j
                    temp_j -= 1
                    while temp_j >= 0:
                        if aMatrix[i][temp_j] == aMatrix[i][j]:
                            count += 1
                            if count == k:
                                return aMatrix[i][j]
                        else:
                            break
                        temp_j -= 1
                if right:
                    temp_j=j
                    temp_j += 1
                    while temp_j <= n-1:
                        if aMatrix[i][temp_j] == aMatrix[i][j]:
                            count += 1
                            if count == k:
                                return aMatrix[i][j]
                        else:
                            break
                        temp_j += 1
                left = 0
                right = 0
            elif top or bottom:
                if top:
                    temp_i = i
                    temp_i -= 1
                    while temp_i >= 0:
                        if aMatrix[temp_i][j] == aMatrix[i][j]:
                            count += 1
                            if count == k:
                                return aMatrix[i][j]
                        else:
                            break
                        temp_i -= 1
                if bottom:
                    temp_i = i
                    temp_i += 1
                    while temp_i <= n-1:
                        if aMatrix[temp_i][j] == aMatrix[i][j]:
                            count += 1
                            if count == k:
                                return aMatrix[i][j]
                        else:
                            break
                        temp_i += 1
                top = 0
                bottom = 0
            elif diag1:
                temp_i = i - 1
                temp_j = j - 1
                while temp_i >= 0 and temp_j >= 0:
                    if aMatrix[temp_i][temp_j] == aMatrix[i][j]:
                        count += 1
                        if count == k:
                            return aMatrix[i][j]
                    else:
                        break
                    temp_i -= 1
                    temp_j -= 1
                    
                temp_i = i + 1
                temp_j = j + 1
                while temp_i <= n-1 and temp_j <= n-1:
                    if aMatrix[temp_i][temp_j] == aMatrix[i][j]:
                        count += 1
                        if count == k:
                            return aMatrix[i][j]
                    else:
                        break
                    temp_i += 1
                    temp_j += 1
                diag1 = 0
                
            elif diag2:
                temp_i = i-1
                temp_j = j+1
                while temp_i >= 0 and temp_j <= n-1:
                    if aMatrix[temp_i][temp_j] == aMatrix[i][j]:
                        count += 1
                        if count == k:
                            return aMatrix[i][j]
                    else:
                        break
                    temp_i -= 1
                    temp_j += 1
                    
                temp_i = i+1
                temp_j = j-1
                while temp_i <= n-1 and temp_j >= 0:
                    if aMatrix[temp_i][temp_j] == aMatrix[i][j]:
                        count += 1
                        if count == k:
                            return aMatrix[i][j]
                    else:
                        break
                    temp_i += 1
                    temp_j -= 1
                diag2 = 0
            else:
                done = 1
                return None
                
    def readInput(self):
        try:
            with open(self.myinput,'r') as f:
                with open('rotate-large.out', 'a+') as w:
                    total = 0
                    isRead = 0
                    row = 0
                    mymatrix = None
                    isFirstLine = 1
                    for line in f:
                        line = line.strip()
                        if total == 0:
                            total = int(line)
                            atemp = total - 1
                            continue
                        if not isRead:
                            n,k = map(int,line.split(' '))
                            mytemp = n
                            #initialize my matrix
                            mymatrix = [[0 for i in range(n)] for j in range(n)]
                            isRead = 1
                            continue
                        for i in range(n):
                            mymatrix[row][i] = line[i]
                        row += 1
                        mytemp -= 1
                        if mytemp == 0:
                            self.rotate_90Clockwise_dropdown_Gravity(mymatrix, n)
                            if isFirstLine:
                                w.writelines("Case #%d: %s" % (total - atemp, self.check_winner(mymatrix, n, k)))
                                isFirstLine = 0
                            else:
                                w.writelines("\nCase #%d: %s" % (total - atemp, self.check_winner(mymatrix, n, k)))
                            #print self.check_winner(mymatrix, n, k)
                            atemp -= 1
                            isRead = 0
                            mymatrix = None
                            row = 0
        except IOError:
            print "Can't open this file %s" % self.myinput
            
os.chdir('rotate')
myrotate = Rotate('A-large-practice.in')
myrotate.readInput()                    
        