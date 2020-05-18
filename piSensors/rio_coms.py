import board
import serial

standin = False
rio = serial.Serial('/dev/ttyAMA0', 9600)

def disabled():
    if rio.read(1) is not None:
        return True
    else:
        return False


def send_value(value):
    rio.write(value)
    print("Value {}".format(value))