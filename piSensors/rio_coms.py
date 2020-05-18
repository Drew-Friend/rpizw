import board
import serial

standin = False
print("about to serial")
rio = serial.Serial('/dev/ttyAMA0', 9600, timeout = 0)

def disabled():
    if rio.read() is 'D':
        print("Disabled")
        return True
    else:
        return False


def send_value(value):
    print("Value {}".format(value))
    rio.write(value)