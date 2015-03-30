'''
Created on Mar 30, 2015

@author: Chris Tran
'''
import os
import time
import re

class AlienLanguage:
    def __init__(self, filename,mylist):
        self.myfile = filename
        self.mylist = mylist
        
    def getToken(self,myline):
        startRead = 0
        token = ""
        for mychar in myline:
            if mychar == "(":
                startRead = 1
                continue
            if mychar == ")":
                startRead = 0
                yield token
                token = ""
                continue             
            if startRead == 1:
                token = token + mychar
            else:
                yield mychar
            
    def countWordMatch(self,myline,limit):
        count = 0
        not_count = 0
        i = 0
        for item in self.mylist:
            for mytoken in self.getToken(myline):
                if i >= limit:
                    print "Index out of bound! \n"
                    return -1
                if item[i] not in mytoken:
                    not_count = 1
                    break
                i += 1
            if not_count == 0:
                count += 1
            i = 0
            not_count = 0
        
        return count
           
    def readInput(self):
        try:
            with open (self.myfile, 'r') as f:
                total = 0
                l = 0
                d = 0
                for line in f:
                    line = line.strip()
                    if total == 0:
                        l,d,total = re.split(r'\s+', line)
                        d = int(d)
                        total = int(total)
                        n = total - 1
                        continue
                    if d > 0:
                        #store word in my list
                        self.mylist.append(line)
                        d -= 1
                    else:
                        #check each test case
                        with open ('alien_language_large.out', 'a+') as w:
                            w.writelines("Case #%d: %s\n" % (total - n, self.countWordMatch(line,l)))
                        #print "Case #%d: %s" % (total - n, self.countWordMatch(line))
                        n -= 1
        except IOError:
            print "Can't open %s" % self.myfile
            
os.chdir('alien_language')
mylist = []
aLanguage = AlienLanguage('A-large-practice.in', mylist)
start = time.clock()
aLanguage.readInput()
print time.clock() - start, "seconds"