from arduino import Arduino
import time

pin = raw_input("Please enter a pin number:")

b = Arduino('/dev/ttyACM0')
#pin = 13

#declare output pins as a list/tuple
b.output([pin])


#for x in xrange(10):
while True:
    b.setHigh(pin)
    time.sleep(1)
    print b.getState(pin)
    b.setLow(pin)
    print b.getState(pin)
    time.sleep(1)

b.close()

