#!/bin/python3

from gpiozero import LED
from time import sleep

led = LED(18)
unit = 0.1
message = "hello my name is not jeremy"

def dit():
	print("dit")
	led.on()
	sleep(unit)
	led.off()
	sleep(unit)

def dah():
	print("dah")
	led.on()
	sleep(unit*3)
	led.off()
	sleep(unit)

def cSpace():
	print(" ")
	sleep(unit*2)

def wSpace():
	print("\n")
	sleep(unit * 6)

letterDict = {
	"a" : "._",
	"b" : "_...",
	"c" : "_._.",
	"d" : "_..",
	"e" : ".",
	"f" : ".._.",
	"g" : "__.",
	"h" : "....",
	"i" : "..",
	"j" : ".___",
	"k" : "_._",
	"l" : "._..",
        "m" : "__",
        "n" : "_.",
        "o" : "___",
        "p" : ".__.",
        "q" : "__._",
        "r" : "._.",
        "s" : "...",
        "t" : "_",
        "u" : ".._",
        "v" : "..._",
        "w" : ".__",
        "x" : "_.._",
        "y" : "_.__",
        "z" : "__..",
}

def writeMessage():
	for letter in message:
		if not letter.isspace():
			for letterSound in letterDict[letter]:
				if letterSound == ".":
					dit()
				else:
					dah()
			cSpace()
		else:
			wSpace()
	print("\n")

while True:
	print("Message incoming")
	writeMessage()
	sleep(3)
