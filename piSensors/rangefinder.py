
import time
import board
from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X
i2c = board.I2C()
xshut = []

class Laser:
    def __init__(self, address):
        self.address = address
    
def setup():
    for i in range(len(xshut)):
            for j in range(len(xshut)):
                DigitalInOut(board.xshut[j]).switch_to_output(value = False)
    DigitalInOut(board.xshut[i]).switch_to_output(value = True)
    VL53L0X(i2c).setaddress(i + 0x30)