#!/usr/bin/env python
import LCD1602
import time
import datetime

now = datetime.datetime.now()

def setup():
	LCD1602.init(0x27, 1)	# init(slave address, background light)
	LCD1602.write(0, 0, now.strftime("%Y-%m-%d %H:%M"))
	LCD1602.write(1, 1, 'The RAISE Lab!')
	time.sleep(60)

def loop():
	space = '                '
	greetings = 'Thank you for buying SunFounder Sensor Kit for Raspberry! ^_^'
	greetings = space + greetings
	while True:
		tmp = greetings
		for i in range(0, len(greetings)):
			LCD1602.write(0, 0, tmp)
			tmp = tmp[1:]
			time.sleep(0.8)
			LCD1602.clear()

def destroy():
	pass	

if __name__ == "__main__":
	try:
		#setup()
		while True:
                    setup()
                    pass
	except KeyboardInterrupt:
		destroy()
