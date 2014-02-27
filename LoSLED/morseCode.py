
from arduino import Arduino
import time

###################
## CONFIG

#pin = int(initializeSession[0])

#b = Arduino('/dev/ttyACM2')
# declare output pins as a list/tuple
#b.output([pin])
###################
### MORSE CODE MAPPINGS ###
## CAN CONVERT THIS \/ \/ \/ INTO BIN, STORE AS INT INSTEAD OF LIST
# dot is 0
# dash is 1
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
###################


# assert ints
# try/except
def initializeSession():
    print "Initializing session.."
    pin = raw_input("Pin (default 9): ")
    timeStep = raw_input("Timestep (default .1): ")
    dotLength = raw_input("Dot length (default 1): ")
    dashLength = raw_input("Dash length (default 3): ")
    spaceLength = raw_input("Space length (default 7):  ")
    print "Good to go."
    return pin, timeStep, dotLength, dashLength, spaceLength

def getMessageFromUser():
    # UI portion
    # try/except clause
    msgOrig = raw_input("~>: ")
    msg = msgOrig.strip()
    msg = msg.strip()
    msg = list(msg.lower())
    msgLength = len(msg)
    return msg, msgLength, msgOrig

def checkMessage():
    (msg, msgLength, msgOrig) = getMessageFromUser()
    # assert the message is transmittable
    for char in xrange(msgLength):
        if not(msg[char].isspace() or msg[char].isalnum()):
            print "Message must be alphanumeric"
            break
    return msg, msgLength, msgOrig

def transmit():
    (pin, timeStep, dotLength, dashLength, spaceLength) = initializeSession()
    (msg, msgLength, msgOrig) = checkMessage() 
    timeStart = time.time()
    for char in xrange(msgLength):
        charList = morseCode[msg[char]]
        for letter in xrange(len(charList)):
            if(charList[letter] == space):
                b.setLow(pin)
                time.sleep(timeStep * space)
            if(charList[letter] == 0):
                b.setHigh(pin)
                time.sleep(timeStep * dot)
                b.setLow(pin)
                time.sleep(timeStep * dash)
            if(charList[letter] == 1):
                b.setHigh(pin)
                time.sleep(timeStep * dash)
                b.setLow(pin)
                time.sleep(timeStep * dash)
    timeEnd = time.time()
    print 'Tx:', msgOrig, "in:", float(timeEnd - timeStart), "s"
    transmit(timeStep)
    b.close()

#transmit()
initializeSession()
