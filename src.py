#
#Author: Nguyen Tran
#Date: 3/19/2015
#
#
import re
import os
def buyItems(money, mylist,length):
    mydict = {}
    index = -1
    for item in mylist:
        index += 1
        mylist[index] = int(item)
        try:
            temp = mydict[int(item)]
            mydict[int(item)+1000] = index+1
        except KeyError:
            mydict[int(item)] = index+1
    mylist.sort()
    first = 0
    end = int(length)-1
    while first < end:
        if mylist[first] + mylist[end] > int(money):
            end -= 1
        elif mylist[first] + mylist[end] == int(money):
            if(mylist[first] == mylist[end]):
                item1 = mydict[mylist[first]+1000]
                item2 = mydict[mylist[end]]
            else:
                item1 = mydict[mylist[first]]
                item2 = mydict[mylist[end]]
            return (item1,item2) if item1 < item2 else (item2,item1)
        else:
            first += 1
os.chdir('store_creadit_input_output')
with open("A-large-practice.in", 'r') as f:
    total = 0
    money = 0
    length = 0
    mylist = []
    count = 0
    for line in f:
        line = line.strip()
        if total == 0:
            total = line
            n = int(total) - 1
            continue
        if count < 3:
            if money == 0:
                money = line
                count += 1
                continue
            elif length == 0:
                length = line
                count += 1
                continue
            elif not mylist:
                mylist = re.split('\s+',line)
                count += 1
                mytuple = buyItems(money,mylist,length)
                with open("Store_creadit_large.out", 'a+') as w:
                    myline = "Case #%d: %s %s\n" % (int(total)-n,mytuple[0],mytuple[1])
                    w.writelines(myline)
                #print "money = %s, length = %s, \nmylist = %s" % (money,length,mylist)
                n -= 1
                continue
        else:
            count = 1
            money = line
            length = 0
            mylist[:] = []
        