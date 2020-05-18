from Laser import laser_base
from digitalio import DigitalInOut

xshut = laser_base.xshut
lasers = laser_base.vl53

xshut.append(DigitalInOut(board.D4))
laser_base.set_addresses()
laser_base.detect_range()
laser_base.reset_addresses()