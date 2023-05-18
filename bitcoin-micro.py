#! /usr/bin/env python

from __future__ import print_function
import subprocess
import sys
import time
import json, requests
import math
#import scrollphat
import microdotphat #import clear, set_pixel, set_brightness, show, write_string

#scrollphat.set_brightness(4)

# Every refresh_interval seconds we'll refresh the weather data, doesn't change too often so 30mins appropriate
pause = 0.12
ticks_per_second = 1/pause
refresh_interval = 60
microdotphat.write_string("hello", offset_x=0, offset_y=0, kerning=False)
url = "http://api.coindesk.com/v1/bpi/currentprice.json"

def get_timeout():
    return ticks_per_second * refresh_interval

def get_wet():
# Get the weather data
#    print("Price Update...")
#scrollphat.set_pixels(lambda x, y: 1, auto_update=True)
    try:
        resp = requests.get(url)
        sine()
    data = json.loads(resp.text)
        val = data['bpi']['USD']['rate']
    except:
    #print(resp)
    return "ERR"
    return val

def sine():
    timer = 0
    while (timer < 1):
        microdotphat.clear()
    t = time.time() * 10
        for x in range(45):
            y = int((math.sin(t + (x/2.5)) + 1) * 3.5)
            microdotphat.set_pixel(x, y, 1)
        
        microdotphat.show()
        time.sleep(0.01)
    timer+=0.01

timeout = get_timeout()
count = 0
msg = get_wet()
microdotphat.clear()
microdotphat.write_string(msg, offset_x=0, offset_y=0, kerning=False)
microdotphat.show()

while True:
    try:
#        scrollphat.scroll()
        time.sleep(pause)

        if(count > timeout):
            msg = get_wet()
            #scrollphat.write_string(msg)
            microdotphat.clear()
        microdotphat.write_string(msg, offset_x=0, kerning=False)
        microdotphat.show()
        timeout = get_timeout()
            count = 0
        else:
            count = count+ 1
    except KeyboardInterrupt:
        #scrollphat.clear()
        sys.exit(-1)

