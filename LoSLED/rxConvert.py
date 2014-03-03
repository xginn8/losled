

##################
## rxConvert.py ##
##################


morseCode = dict()
morseCode['a'] = [0,1]
morseCode['b'] = [1,0,0,0]
morseCode['c'] = [0,1,0,1]
morseCode['d'] = [0,1,1]
morseCode['e'] = [0]
morseCode['f'] = [0,0,1,0]
morseCode['g'] = [1,1,0]
morseCode['h'] = [0,0,0,0]
morseCode['i'] = [0,0]
morseCode['j'] = [0,1,1,1]
morseCode['k'] = [1,0,1]
morseCode['l'] = [0,1,0,0]
morseCode['m'] = [1,1]
morseCode['n'] = [1,0]
morseCode['o'] = [1,1,1]
morseCode['p'] = [0,1,1,0]
morseCode['q'] = [1,1,0,1]
morseCode['r'] = [0,1,0]
morseCode['s'] = [0,0,0]
morseCode['t'] = [1]
morseCode['u'] = [0,0,1]
morseCode['v'] = [0,0,0,1]
morseCode['w'] = [0,1,1]
morseCode['x'] = [1,0,0,1]
morseCode['y'] = [1,0,1,1]
morseCode['z'] = [1,1,0,0]
morseCode['1'] = [0,1,1,1,1]
morseCode['2'] = [0,0,1,1,1]
morseCode['3'] = [0,0,0,1,1]
morseCode['4'] = [0,0,0,0,1]
morseCode['5'] = [0,0,0,0,0]
morseCode['6'] = [1,0,0,0,0]
morseCode['7'] = [1,1,0,0,0]
morseCode['8'] = [1,1,1,0,0]
morseCode['9'] = [1,1,1,1,0]
morseCode['0'] = [1,1,1,1,1]
morseCode[' '] = [7]

# passed a list of signal lengths
# passed key, code index
# split on spaces
# for each  list, find that list in dict()

def reverseDict(code):
#    switch keys and values in dict, but convert new keys to tuples from lists
    for key in code:
        code[key] =  tuple(code[key])
    reversedDict = dict(zip(code.values(),code.keys()))
    return reversedDict

def letterizeMsgIn(msgIn, morseCode):
    letterized = []
    while(len(msgIn) > 0):
        letterized.append(msgIn[:msgIn.index(3)])
        for i in xrange(msgIn.index(3)):
            msgIn.pop(0)
        msgIn.pop(0)
    return letterized

def decode(msgIn, morseCode):
    letterizedList = letterizeMsgIn(msgIn, morseCode)
    reversedCode = reverseDict(morseCode)
    for row in xrange(len(letterizedList)):
        letterizedList[row] = reversedCode[tuple(letterizedList[row])]
    print '~~~>', ''.join(letterizedList)


decode([0, 0, 0, 0, 3, 0, 3, 0, 1, 0, 0, 3, 0, 1, 0, 0, 3, 1, 1, 1, 3], morseCode)
decode([0, 3, 7, 3, 1, 0, 3, 0, 1, 0, 0, 3, 0, 1, 0, 0, 3, 1, 1, 1, 3], morseCode)
