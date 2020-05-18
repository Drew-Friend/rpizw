
import time
import board
from digitalio import DigitalInOut
from adafruit_vl53l0x import VL53L0X
i2c = board.I2C()
xshut = []

class Laser:
    def __init__(self, address)
    self.address = address
    
def setup():
    for i < len(xshut):
            for j < len(xshut):
                DigitalInOut(board.xshut[j]) = False
    DigitalInOut(board.xshut[i]) = True
    VL53L0X(i2c).setaddress(i + 0x30)