'''
Created on May 20, 2015

@author: Chris Tran
'''

import os

class FileFixIt:
    def __init__(self,inputfile):
        self.myinput = inputfile
    
    def makeDict(self,mylist):
        returnDict = {}
        mydir = ''
        for ele in mylist:
            portions = ele.split('/')
            for i in range(1,len(portions)):
                mydir = mydir+"/"+portions[i] 
                try:
                    mytemp = returnDict[mydir]
                except KeyError:
                    returnDict[mydir] = 1
            mydir = ''
        return returnDict
    
    def countMkDir(self,mylist,mydict):
        count = 0
        keep_going = 1
        for ele in mylist:  
            portions = ele.split('/')
            keep_going = 1
            while keep_going:
                atemp = '/'.join(portions)
                if atemp == '':
                    keep_going = 0
                    continue
                try:
                    mytemp = mydict[atemp]
                    keep_going = 0
                except KeyError:
                    #update dict
                    mydict[atemp] = 1
                    holder = portions.pop()
                    count += 1
        return count
         
    
    def readInput(self):
        try:
            with open(self.myinput,'r') as f:
                with open('file_fix_it-large.out', 'a+') as w:
                    total = 0
                    isRead = 0
                    temp_list = []
                    list_dir = []
                    aDict = {}
                    for line in f:
                        line = line.strip()
                        if total == 0:
                            total = int(line)
                            atemp = total - 1
                            continue
                        if not isRead:
                            isRead = 1
                            n,m = line.split(' ')
                            m = int(m)
                            n = int(n)
                            temp = n
                            temp1 = m
                            continue
                        if temp > 0:
                            temp_list.append(line)
                            temp -= 1
                            if temp == 0:
                                # Start to make my dictionary
                                aDict = self.makeDict(temp_list)
                        elif temp1 > 0:
                            list_dir.append(line)
                            temp1 -= 1
                            if temp1 == 0:
                                #Solve problem
                                hold_count = self.countMkDir(list_dir, aDict)
                                w.writelines("Case #%d: %s\n" % (total - atemp,hold_count))
                                atemp -= 1
                                isRead = 0
                                temp_list[:] = []
                                list_dir[:] = []
                                aDict.clear()
        except IOError:
            print "Can't open this file %s" % self.myinput
            
os.chdir('file_fix_it')
myFileFixIt = FileFixIt('A-large-practice.in')
myFileFixIt.readInput()
                        
                        
                
