"""
1038 VL53L0X sensor library
"""
import time
import board
from digitalio import DigitalInOut
from Laser.adafruit_vl53l0x import VL53L0X


i2c = board.I2C()       #setup singleton i2c bus
xshut = []              #list of xshut pins, apended in hub
vl53 = []               #list of laser objects, ordered in the order the xshut's are declared


def set_addresses():
    """ Set a unique address for each laser with an assigned xshut pin """
    for power_pin in xshut:                     #set each xshut pin to output and turn off
        power_pin.switch_to_output(value=False)

    for i, power_pin in enumerate(xshut):
        power_pin.value = True                  #turn xshut on for selected pin
        vl53.insert(i, VL53L0X(i2c))            #add a sensor object, in the same order as the xshut's
        if i < len(xshut)-1:                    # leave last sensor's address 29, before that, they will be increasing
            vl53[i].set_address(0x30 + i)


def reset_addresses():
    """ set all adresses back to zero """
    for i, power_pin in enumerate(xshut):   #turns on each laser
        power_pin.value = True
        vl53[i].set_address(0x29)           #set each laser to 29 as it turns on


def detect_range(count=5):
    """ take 5 samples from each sensor"""
    while count:
        for index, sensor in enumerate(vl53):
            print("Sensor {} Range: {}mm".format(index + 1, sensor.range))
        time.sleep(1.0)
        count -= 1


def distance(laserNum):
    """get current distace of a specific laser"""
    dist = vl53[laserNum].range
    return dist
