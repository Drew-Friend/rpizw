import board
import serial

print("about to serial")
rio = serial.Serial('/dev/ttyAMA0', 9600, timeout = 0, write_timeout = 0)
standin = rio.read()

def disabled():
    print((rio.read()).decode('utf-8'))
    if rio.read() is not standin:
        return True
    else:
        return False


def send_value(value):
    print("Value {}".format(value))
    rio.write([value])