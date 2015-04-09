'''
Created on Apr 7, 2015

@author: Chris Tran
'''
import time
import os
import re

class Rope_Intranet:
    def __init__(self, filename):
        self.myfile = filename
        
    def findInversion (self, alist, blist):
        alen = len(alist)
        blen = len(blist)
        count = 0
        for i in range(alen):
            for j in range(i,blen):
                if (int(alist[j]) - int(alist[i])) * (int(blist[j]) - int(blist[i])) < 0: #different sign - they are crossed
                    count += 1
        return count
    
    #===========================================================================
    # def findInversion_opt(self,alist,blist):
    #     mydict = {}
    #     index = 0
    #     for i in alist:
    #         mydict[i] = blist[index]
    #         index += 1
    #     alist.sort()
    #     
    #     alist.sort()
    #     blist.sort()
    #     alen = len(alist)
    #     blen = len(blist)
    #     index_a= 0
    #     index_b = 0
    #     count = 0
    #     while index_a < alen and index_b < blen:
    #         if alist[index_a] <= blist[index_b]:
    #             #clist.append(alist[index_a])
    #             index_a += 1
    #         else:
    #             count = alen - index_a - 1
    #             #clist.append(blist[index_b])
    #             break
    #     return count 
    #===========================================================================
    
    
                
    
    def readInput(self):
        try:
            with open (self.myfile, 'r') as f:
                total = 0
                num_ropes = 0
                alist = []
                blist = []
                for line in f:
                    line = line.strip()
                    if total == 0:
                        total = int(line)
                        n = total - 1
                        continue
                    if num_ropes == 0:
                        num_ropes = int(line)
                        alist[:] = []
                        blist[:] = []
                        continue
                    else:
                        portions = re.split(r'\s+',line)
                        alist.append(portions[0])
                        blist.append(portions[1])
                        num_ropes -= 1
                        if num_ropes == 0:
                            #with open ('rope_intranet-large.out', 'a+') as w:
                            #   w.writelines(('Case #%d: %s\n') % (total-n, self.findInversion(alist,blist)))
                            print ('Case #%d: %s') % (total-n, self.findInversion_opt(alist,blist))
                            n -= 1
        except IOError:
            print "Can't open %s" , self.myfile
            

os.chdir('rope_intranet')
rope = Rope_Intranet('small.txt')
start = time.clock()
rope.readInput()
print time.clock() - start, 'seconds'