"""
Example of how to use the adafruit_vl53l0x library to change the assigned address of
multiple VL53L0X sensors on the same I2C bus. This example only focuses on 2 VL53L0X
sensors, but can be modified for more. BE AWARE: a multitude of sensors may require
more current than the on-board 3V regulator can output (typical current consumption during
active range readings is about 19 mA per sensor).
"""
import time
import board
from digitalio import DigitalInOut
from Laser.adafruit_vl53l0x import VL53L0X

# declare the singleton variable for the default I2C bus
i2c = board.I2C()
# list of xshut pins
xshut = []
# list of lasers
vl53 = []



# changes the addresses of the VL53L0X sensors
def set_addresses():
    for power_pin in xshut:
        # makes each xshut pin an output, set to low
        power_pin.switch_to_output(value=False)
        # all VL53L0X sensors are now off
    for i, power_pin in enumerate(xshut):
        power_pin.value = True
        # instantiate the VL53L0X sensor on the I2C bus & insert it into the "vl53" list
        vl53.insert(i, VL53L0X(i2c)) 
        if i < len(xshut)-1:
            # default address is 0x29
            vl53[i].set_address(i + 0x30)  # address assigned should NOT be already in use

def reset_addresses():
    for i, power_pin in enumerate(xshut):
        power_pin.value = True
    vl53[i].set_address(0x29)

def detect_range(count=5):
    """ take count=5 samples """
    while count:
        for index, sensor in enumerate(vl53):
            print("Sensor {} Range: {}mm, Address {}".format(index + 1, sensor.range, sensor.address))
        time.sleep(1.0)
        count -= 1

xshut.append(DigitalInOut(board.D4))
set_addresses()
detect_range()
reset_addresses()