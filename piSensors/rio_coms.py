import board
import serial

print("about to serial")
rio = serial.Serial('/dev/serial0', 9600, timeout = 0, write_timeout = 0)
standin = rio.read()

def disabled():
    if rio.read() is not standin:
        print((rio.read()).decode('utf-8'))
        return True
    else:
        return False


def send_value(value):
    print("Value {}".format(value))
    rio.write([value])