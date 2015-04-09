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
                    with open ('welcome-large.out','a+') as w:
                        w.writelines(("Case #%d: %s\n") % (total -n, self.countWelcome(line)))
                    n -= 1
        except IOError:
            print "Can't read %s" % self.myfile
            
os.chdir('welcome_to_codejam')
welcome = Welcome_to_Codejam('C-large-practice.in')
start = time.clock()
welcome.readInput()
print time.clock() - start, "seconds"