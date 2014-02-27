
s = 'testtext'
sList = list(s)
sBin = []

for item in xrange(len(sList)):
    sBin.append(bin(ord(sList[item])))

print s, sList, sBin
