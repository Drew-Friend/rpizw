from Laser import laser_base
from Laser.adafruit_vl53l0x import VL53L0X

xshut = laser_base.xshut
lasers = laser_base.vl53

xshut.append(DigitalInOut(board.D4))
laser_base.set_addresses()
laser_base.detect_range()
laser_base.reset_addresses()