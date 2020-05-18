from Laser import laser_base
from digitalio import DigitalInOut
import board
import rio_coms

xshut = laser_base.xshut
lasers = laser_base.vl53

enabled = True

xshut.append(DigitalInOut(board.D4))
laser_base.set_addresses()

while enabled:
    if rio_coms.disabled():
        enabled = False
    rio_coms.send_value(laser_base.distance(0))


#it'd be cool to throw rainbow led code in here
laser_base.reset_addresses()