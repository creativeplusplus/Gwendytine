# Display code for LCD mouth

from grove_rgb_lcd import *

while (True):
	setText("----------------\n----------------")
	setRGB(255, 0, 0)
	time.sleep(0.5)
	setRGB(0, 0, 255)
	time.sleep(0.5)

	setText("-----VROOM!-----\n-VROOM----VROOM-")
	setRGB(255, 0, 0)
	time.sleep(0.5)
	setRGB(0, 0, 255)
	time.sleep(0.5)

	setText("---GWENDYTINE---\n--out-mah--way--")
	setRGB(255, 0, 0)
	time.sleep(0.5)
	setRGB(0, 0, 255)
	time.sleep(0.5)
