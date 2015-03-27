'''
Created on Mar 25, 2015

@author: NGUYEN TRAN
'''

import os
import re
import time

class customer:
    def __init__(self,likeMalted,likeUnmalted):
        self.likeMaltedIndex = likeMalted
        self.likeUnmaltedIndex = likeUnmalted
        
    def isSatisfied(self,myBatch):
        if(self.likeMaltedIndex and myBatch[self.likeMaltedIndex[0]] == 1):
            return 1
        for i in self.likeUnmaltedIndex:
            if(myBatch[i] == 0):
                return 1            
        return 0
            

class MilkShake:
    def __init__(self,filename):
        self.myfile = filename
        
    def isSatisfiedAll(self,myCustomer_list,num_flavor):
        myBatch = [0]*int(num_flavor)
        check_satisfy = 1
        while check_satisfy:
            check_satisfy = 0
            for my_customer in myCustomer_list:
                if not my_customer.isSatisfied(myBatch):
                    if not my_customer.likeMaltedIndex:
                        return "IMPOSSIBLE"
                    else:
                        myBatch[my_customer.likeMaltedIndex[0]] = 1
                        myCustomer_list.remove(my_customer)
                        check_satisfy = 1
        
        return myBatch
            
    def readInput(self):
        try:
            with open (self.myfile, 'r') as f:
                with open ('Milkshake-large.out', 'a+') as w:
                    total = 0
                    num_flavor = 0
                    num_customer = 0
                    count = 0
                    cus_id = 0
                    mylist = []
                    list_unmalted_index = []
                    list_malted_index = []
                    mylist_customer = []
                    for line in f:
                        if total == 0:
                            total = int(line)
                            n = total - 1
                            continue
                        if num_flavor == 0:
                            num_flavor = int(line)
                            continue
                        if count < 1:
                            num_customer = int(line)
                            count += 1
                            cus_id = 0
                            if mylist:
                                mylist[:] = []
                            continue
                        else:
                            if num_customer == cus_id:  
                                #print "Case #%d: %s" %(total - n, self.isSatisfiedAll(mylist_customer,num_flavor))
                                w.writelines(("Case #%s: ") % (total -n))
                                myoutput = self.isSatisfiedAll(mylist_customer,num_flavor)
                                if isinstance(myoutput, list):     
                                    for i in myoutput:
                                        w.writelines("%s " % i)
                                else:
                                    w.writelines(myoutput)
                                w.writelines("\n")
                                
                                num_flavor = int(line)
                                count = 0
                                n -= 1
                                mylist_customer[:] = []
                            else:
                                i = 1
                                line = line.strip()
                                portions = re.split(r'\s+', line)
                                portions[0] = int(portions[0])
                                while portions[0] > 0:
                                    mytuple = (cus_id,portions[i],portions[i+1])
                                    if int(portions[i+1]) == 0: #unmalted
                                        list_unmalted_index.append(int(portions[i])-1)
                                    else:
                                        list_malted_index.append(int(portions[i])-1)
                                    i += 2
                                    portions[0] -= 1
                                    mylist.append(mytuple)
    
                                myCustomer = customer(list_malted_index,list_unmalted_index)                         
                                mylist_customer.append(myCustomer)
                                
                                list_unmalted_index = []
                                list_malted_index = []
                                cus_id += 1
                    #take care of last case
                    if num_customer == cus_id:
                        #print "Case #%d: %s" %(total - n, self.isSatisfiedAll(mylist_customer,num_flavor))
                        w.writelines(("Case #%s: ") % (total -n))
                        myoutput = self.isSatisfiedAll(mylist_customer,num_flavor)
                        if isinstance(myoutput, list):            
                            for i in self.isSatisfiedAll(mylist_customer,num_flavor):
                                w.writelines("%s " % i)
                        else:
                            w.writelines(myoutput)
        except IOError:
            print "Can't reat %s" % (self.myfile)

os.chdir('Milkshake')
mymilkshake = MilkShake('B-large-practice.in')
start = time.clock()
mymilkshake.readInput()
print time.clock() - start, "seconds"
            