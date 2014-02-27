
def textToBin(text):
    sList = list(s)
    sBin = []
    for item in xrange(len(sList)):
        sBin.append(bin(ord(sList[item])))
    return s, sList, sBin

s = 'testtext'
print textToBin(s)

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

