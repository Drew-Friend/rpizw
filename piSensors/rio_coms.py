import busio
import board

standin = False
rio = busio.UART(board.TX, board.RX, baudrate=9600)

def disabled():
    if rio.read(1) is not None:
        return True
    else:
        return False


def send_value(value):
    rio.write(value)
    print("Value {}".format(value))