'''
Created on Apr 3, 2015

@author: Chris Tran
'''
import os
import time

class Welcome_to_Codejam:
    def __init__(self,filename):
        self.myfile = filename
    
    def countWelcome(self,line):
        #=======================================================================
        # mystring = 'welcome to code jam'
        # slen = len(mystring)
        # m = [[0 for x in range(slen)] for x in range(len(line))]
        # index = 0
        # for i in line:
        #     for x in range(slen):        
        #         if i == mystring[x]:
        #             if index == 0:
        #                 m[index][x] += 1
        #                 continue
        #             if x == 0:
        #                 m[index][x] = m[index-1][x] + 1
        #             else:
        #                 #print index
        #                 #print x  
        #                 m[index][x] = m[index-1][x] + m[index-1][x-1]          
        #     index += 1
        # return m[index-1][slen-1]
        #=======================================================================
        fsen = ""
        search = "welcome to code jam"
        slen = len(search)
        for c in line:
            if c in "welcome to code jam":
                fsen += c
    
        last = [0 for i in range(slen)]
        for c in fsen:
            mynext = last[:]
            for i in range(slen):
                schar = search[i]
                if c == schar:
                    if i == 0:
                        mynext[i] += 1
                    else:
                        mynext[i] += last[i-1]
            last = mynext
    
        return "%04d" % (last[slen-1] % 10000) 
    
    def readInput(self):
        try:
            with open (self.myfile, 'r') as f:
                total = 0
                for line in f:
                    line = line.strip()
                    if total == 0:
                        total = int(line)
                        n = total - 1
                        continue
                    #print len(line)
                    #pass in function
                    print self.countWelcome(line)
        except IOError:
            print "Can't read %s" % self.myfile
            
os.chdir('welcome_to_codejam')
welcome = Welcome_to_Codejam('small.txt')
welcome.readInput()
