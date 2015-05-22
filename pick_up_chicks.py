'''
Created on May 21, 2015

@author: Chris Tran
'''

import os

class PickUpChicks:
    def __init__(self,inputfile):
        self.myinput = inputfile
        
    def makeChicken(self,loc_list,vel_list):
        if len(loc_list) != len(vel_list):
            print "ERROR: reading in input"
            return None
        return_list = []
        for i in range(0,len(loc_list)):
            mytuple = (loc_list[i],vel_list[i])
            return_list.append(mytuple)
            
        return return_list
    
    def count_swaps(self,mylist,n,k,b,t):
        made_it = 0
        cant = 0
        count = 0
        for i in reversed(mylist):
            if made_it >= k:
                break
            #check if this chick can make it
            if (int(i[0]) + (int(i[1])*t)) >= b:
                made_it += 1
                #Update count for every chick which can make it.
                count += cant
            else:
                cant += 1
        if made_it >= k:
            return count
        else:
            return "IMPOSSIBLE"
    
    def readInput(self):
        try:
            with open (self.myinput,'r') as f:
                with open('pick_up_chicks-large.out', 'a+') as w:
                    total = 0
                    isRead = 0
                    isReadLocation = 0
                    location_list = []
                    velocity_list = []
                    list_chicken = []
                    for line in f:
                        line = line.strip()
                        if total == 0:
                            total = int(line)
                            atemp = total - 1
                            continue
                        if not isRead:
                            n,k,b,t = map(int,line.split(' '))
                            isRead = 1
                            continue
                        else:
                            if not isReadLocation:
                                location_list = line.split(' ')
                                isReadLocation = 1
                            else:
                                velocity_list = line.split(' ')
                                list_chicken = self.makeChicken(location_list,velocity_list)
                                output = self.count_swaps(list_chicken, n, k, b, t)
                                w.writelines("Case #%d: %s\n" % (total-atemp,output))
                                atemp -= 1
                                #reset variable for next test case
                                isRead = 0
                                isReadLocation = 0
                                location_list[:] = []
                                velocity_list[:] = []
                                list_chicken[:] = []
                            
        except IOError:
            print "Can't open this file %s" % self.myinput
            
os.chdir('pick_up_chicks')
mypickupchicks = PickUpChicks('B-large-practice.in')
mypickupchicks.readInput()