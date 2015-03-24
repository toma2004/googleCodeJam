'''
Created on Mar 23, 2015

@author: NGUYEN TRAN
'''
import os

class t9_spelling:
    def __init__(self,filename,mydict):
        self.myfile = filename
        self.mydict = mydict
    
    def buildDict(self):
        self.mydict = {
        'a':'2',
        'b':'22',
        'c':'222',
        'd':'3',
        'e':'33',
        'f':'333',
        'g':'4',
        'h':'44',
        'i':'444',
        'j':'5',
        'k':'55',
        'l':'555',
        'm':'6',
        'n':'66',
        'o':'666',
        'p':'7',
        'q':'77',
        'r':'777',
        's':'7777',
        't':'8',
        'u':'88',
        'v':'888',
        'w':'9',
        'x':'99',
        'y':'999',
        'z':'9999',
        ' ':'0'                  
                       }
        
    def translate(self,line):
        prior = None
        output = None
        for i in line:
            if not prior:
                prior = i
                output = self.mydict[i]
                continue
            str1 = self.mydict[i]
            str2 = self.mydict[prior]
            if str1[0] == str2[0]:
                output += ' '
            
            output += self.mydict[i]
            prior = i
        return output    
    
    def readInput(self):
        try:
            with open(self.myfile, 'r') as f:
                total = 0
                for line in f:
                    if total == 0:
                        total = int(line)
                        n = total - 1
                        continue
                    line = line.strip('\n')
                    with open ("t9_spelling_large.out", 'a+') as w:
                        w.writelines(("Case #%d: %s\n") % (total -n, self.translate(line)))
                    print ("Case #%d: %s") % (total -n, self.translate(line))
                    n -= 1
        except IOError:
            print "Can't open %s" % self.myfile
            return

mydict = {}
os.chdir('t9_spelling')
t9 = t9_spelling('C-large-practice.in',mydict)
t9.buildDict()
t9.readInput()