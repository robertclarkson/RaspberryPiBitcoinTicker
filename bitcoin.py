#! /usr/bin/env python

from __future__ import print_function
import subprocess
import sys
import time
import json, requests
import math
import scrollphat


scrollphat.set_brightness(4)

# Every refresh_interval seconds we'll refresh the weather data, doesn't change too often so 30mins appropriate
pause = 0.12
ticks_per_second = 1/pause
refresh_interval = 60

url = "http://api.coindesk.com/v1/bpi/currentprice.json"

def get_timeout():
    return ticks_per_second * refresh_interval

def get_wet():
# Get the weather data
#    print("Price Update...")
#scrollphat.set_pixels(lambda x, y: 1, auto_update=True)
    resp = requests.get(url)
    sine()
    try:
	data = json.loads(resp.text)
    except:
	print(resp)
	return "ERR"
    val = data['bpi']['USD']['rate']+"           "
    return val

def sine():
    timer = 0
    i = 0
    buf = [0] * 11
    while (timer < 2):
        try:
            for x in range(0, 11):
                y = (math.sin((i + (x * 10)) / 10.0) + 1) # Produces range from 0 to 2
                y *= 2.5 # Scale to 0 to 5
                buf[x] = 1 << int(y)

            scrollphat.set_buffer(buf)
            scrollphat.update()

            time.sleep(0.005)
	    timer+=0.005
            i += 1
        except KeyboardInterrupt:
            scrollphat.clear()
            sys.exit(-1)

timeout = get_timeout()
count = 0
msg = get_wet()
scrollphat.write_string(msg)

while True:
    try:
#        scrollphat.scroll()
        time.sleep(pause)

        if(count > timeout):
            msg = get_wet()
            scrollphat.write_string(msg)
            timeout = get_timeout()
            count = 0
        else:
            count = count+ 1
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)

