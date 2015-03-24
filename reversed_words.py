'''
Created on Mar 21, 2015

@author: NGUYEN TRAN
'''

import re
import os

class reversed_words:
    def __init__(self,filename):
        self.myfile = filename
        
    def reverse_words(self,line):
        line = line.strip()
        words = re.split(r'\s+',line)
        first = 0
        end = len(words) - 1
        while first < end:
            temp = words[end]
            words[end] = words[first]
            words[first] = temp
            first += 1
            end -= 1 
        return " ".join(words)
    
    def readinput(self):
        try:
            with open(self.myfile,'r') as f:
                total = 0
                for line in f:        
                    if total == 0:
                        total = int(line)
                        n = total - 1
                        continue
                    #print ("Case #%d: %s") % (total - n, self.reverse_words(line))
                    with open ("reversed_words_large.out", 'a+') as w:
                        w.writelines(("Case #%d: %s\n") % (total - n, self.reverse_words(line)))
                    n -= 1
        except IOError:
            print "Can't read %s!\n" % (self.myfile)
            return
        
os.chdir('reversed_words_input_output')
rw = reversed_words("B-large-practice.in")
rw.readinput()