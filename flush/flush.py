import os
import time
import random


def init():
	os.system('adb kill-server')
	time.sleep(1)
	os.system('adb start-server')

	pass


def start():
	pass


def slide():
	while True:
		init_coord_x = random.randint(180, 540)
		init_coord_y = random.randint(900, 1260)

		slip_coord_x = random.randint(180, 540)
		slip_coord_y = random.randint(180, 540)

		os.system('adb shell input swipe {:d} {:d} {:d} {:d}'.format(init_coord_x, init_coord_y, slip_coord_x, slip_coord_y))

		interval = random.randint(1, 15)
		time.sleep(interval)


def treasure():
	pass


if __name__ == '__main__':
	init()
	time.sleep(1)
	slide()