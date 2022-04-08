#!/bin/python3

from gpiozero import LED
from time import sleep

# Here you can set the basic parameters you want to work with
led = LED(18)
unit = 0.3 # Unit of time you want messages to transmit in seconds. E.g. 0.1 seconds on/off/pause etc.
message = "hello my name is not jeremy"	# The message, should be in plaintext, lower case, no punctuation (unless you expand the dict)

# Both dit and dah include the sleep function at one unit, so no inter/intra character pauses are necessary
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

# For both word and character sleeps, they are reduced by one, since the dit and dah functions already sleep for 1 unit
def cSpace():
	print(" ")
	sleep(unit*2)

def wSpace():
	print("\n")
	sleep(unit * 6)

# The letterdict maps the morse code for each letter. It can be expanded to support any character, including unicode and emoji (to represent acronyms)
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

# The writeMessage function loops through each message character, then through the morse representation from the dict, and creates the appropriate output
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
			wSpace() # If the character is a space, it runs the wordspace function
	print("\n")

while True:
	print("Message incoming")
	writeMessage()
	sleep(3)
