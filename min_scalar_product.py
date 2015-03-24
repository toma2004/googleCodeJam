'''
Created on Mar 22, 2015

@author: NGUYEN TRAN
'''
import re
import os

class min_scalar_product:
    def __init__(self,filename):
        self.myfile = filename
    
    def findMin_ScalarProduct(self,v1,v2):
        mysum = 0
        index = 0
        while index < len(v1):
            v1[index] = int(v1[index])
            v2[index] = int(v2[index])
            index += 1
        v1.sort()
        v2.sort(reverse=True)
        index = 0
        while index < len(v1):
            product = v1[index]*v2[index]
            mysum = mysum + product
            index += 1
        return mysum
    
    def readInput(self):
        try:
            with open(self.myfile,'r') as f:
                total = 0
                count = 0
                elements = 0
                vector1 = []
                vector2 = []
                for line in f:        
                    if total == 0:
                        total = int(line)
                        n = total - 1
                        continue
                    if count < 3:
                        if elements == 0:
                            elements = int(line)
                            count += 1
                            continue
                        elif not vector1:
                            line = line.strip()
                            vector1 = re.split(r'\s+',line)
                            count += 1
                            continue
                        elif not vector2:
                            line = line.strip()
                            vector2 = re.split(r'\s+',line)
                            count += 1
                            with open ("min_scalar_product_large.out", 'a+') as w:
                                w.writelines(("Case #%d: %d\n") % (total-n, self.findMin_ScalarProduct(vector1,vector2)))
                            n -= 1
                            continue
                    else:
                        count = 1
                        elements = int(line)
                        vector1[:] = []
                        vector2[:] = []
        except IOError:
            print "Can't read %s!\n" % (self.myfile)
            return

os.chdir('min_scalar_product')
my_minProduct = min_scalar_product('A-large-practice.in')
my_minProduct.readInput()  