#
#Author: Nguyen Tran
#Date: 3/19/2015
#
#

def buyItems(money, mylist,length):
    mydict = {}
    index = -1
    for item in mylist:
        index += 1
        mydict[item] = index
        
    mylist = mylist.sort();
    first = 0
    end = length-1
    while first < end:
        if mylist[first] + mylist[end] > money:
            end -= 1
        elif mylist[first] + mylist[end] == money:
            item1 = mydict[mylist[first]]
            item2 = mydict[mylist[end]]
            return (item1,item2) if item1 < item2 else (item2,item1)
        else:
            first += 1

with open("small.txt", 'r') as f:
    total = 0
    money = 0
    length = 0
    mylist = []
    count = 0
    for line in f:
        line = line.strip()
        if total == 0:
            total = line
            n = total - 1
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
                mylist = line
                count += 1
                mytuple = buyItems(money,mylist,length)
                print "Case #%d: %s %s" % (total-n,mytuple[0],mytuple[1])
                n -= 1
                continue
        else:
            count = 1
            money = line
            length = 0
            mylist[:] = []
        