#!/usr/bin/python

#
# based on code from lrvick and LiquidCrystal

#

import Adafruit_BBIO.GPIO as GPIO
import time
from time import sleep
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

GPIO.setup("P8_11", GPIO.IN)
GPIO.setup("P9_11", GPIO.IN)


class Adafruit_CharLCD:

    # commands

    LCD_CLEARDISPLAY 		= 0x01
    LCD_RETURNHOME 		= 0x02

    LCD_ENTRYMODESET 		= 0x04
    LCD_DISPLAYCONTROL 		= 0x08

    LCD_CURSORSHIFT 		= 0x10
    LCD_FUNCTIONSET 		= 0x20

    LCD_SETCGRAMADDR 		= 0x40
    LCD_SETDDRAMADDR 		= 0x80


    # flags for display entry mode
    LCD_ENTRYRIGHT 		= 0x00

    LCD_ENTRYLEFT 		= 0x02
    LCD_ENTRYSHIFTINCREMENT 	= 0x01

    LCD_ENTRYSHIFTDECREMENT 	= 0x00

    # flags for display on/off control

    LCD_DISPLAYON 		= 0x04
    LCD_DISPLAYOFF 		= 0x00

    LCD_CURSORON 		= 0x02
    LCD_CURSOROFF 		= 0x00

    LCD_BLINKON 		= 0x01
    LCD_BLINKOFF 		= 0x00


    # flags for display/cursor shift
    LCD_DISPLAYMOVE 		= 0x08

    LCD_CURSORMOVE 		= 0x00

    # flags for display/cursor shift

    LCD_DISPLAYMOVE 		= 0x08
    LCD_CURSORMOVE 		= 0x00

    LCD_MOVERIGHT 		= 0x04
    LCD_MOVELEFT 		= 0x00


    # flags for function set
    LCD_8BITMODE 		= 0x10

    LCD_4BITMODE 		= 0x00
    LCD_2LINE 			= 0x08

    LCD_1LINE 			= 0x00
    LCD_5x10DOTS 		= 0x04

    LCD_5x8DOTS 		= 0x00




    def __init__(self, pin_rs="P8_12", pin_e="P8_13", pins_db=["P8_15", "P8_17", "P8_18", "P8_19"]):

	import Adafruit_BBIO.GPIO as GPIO
   	self.GPIO = GPIO

        self.pin_rs = pin_rs
        self.pin_e = pin_e

        self.pins_db = pins_db


        self.GPIO.setup(self.pin_e, GPIO.OUT, 7)

        self.GPIO.setup(self.pin_rs, GPIO.OUT, 7)


        for pin in self.pins_db:

            self.GPIO.setup(pin, GPIO.OUT, 7)


	self.write4bits(0x33) # initialization

	self.write4bits(0x32) # initialization

	self.write4bits(0x28) # 2 line 5x7 matrix

	self.write4bits(0x0C) # turn cursor off 0x0E to enable cursor

	self.write4bits(0x06) # shift cursor right


	self.displaycontrol = self.LCD_DISPLAYON | self.LCD_CURSOROFF | self.LCD_BLINKOFF


	self.displayfunction = self.LCD_4BITMODE | self.LCD_1LINE | self.LCD_5x8DOTS

	self.displayfunction |= self.LCD_2LINE


	""" Initialize to default text direction (for romance languages) """
	self.displaymode =  self.LCD_ENTRYLEFT | self.LCD_ENTRYSHIFTDECREMENT

	self.write4bits(self.LCD_ENTRYMODESET | self.displaymode) #  set the entry mode


        self.clear()



    def begin(self, cols, lines):


	if (lines > 1):

		self.numlines = lines
    		self.displayfunction |= self.LCD_2LINE

		self.currline = 0



    def home(self):


	self.write4bits(self.LCD_RETURNHOME) # set cursor position to zero

	self.delayMicroseconds(3000) # this command takes a long time!



    def clear(self):


	self.write4bits(self.LCD_CLEARDISPLAY) # command to clear display

	self.delayMicroseconds(3000)	# 3000 microsecond sleep, clearing the display takes a long time



    def setCursor(self, col, row):


	self.row_offsets = [ 0x00, 0x40, 0x14, 0x54 ]


	if ( row > self.numlines ): 

		row = self.numlines - 1 # we count rows starting w/0


	self.write4bits(self.LCD_SETDDRAMADDR | (col + self.row_offsets[row]))



    def noDisplay(self): 

	""" Turn the display off (quickly) """

	self.displaycontrol &= ~self.LCD_DISPLAYON

	self.write4bits(self.LCD_DISPLAYCONTROL | self.displaycontrol)



    def display(self):

	""" Turn the display on (quickly) """

	self.displaycontrol |= self.LCD_DISPLAYON

	self.write4bits(self.LCD_DISPLAYCONTROL | self.displaycontrol)



    def noCursor(self):

	""" Turns the underline cursor on/off """

	self.displaycontrol &= ~self.LCD_CURSORON

	self.write4bits(self.LCD_DISPLAYCONTROL | self.displaycontrol)



    def cursor(self):

	""" Cursor On """

	self.displaycontrol |= self.LCD_CURSORON

	self.write4bits(self.LCD_DISPLAYCONTROL | self.displaycontrol)



    def noBlink(self):

	""" Turn on and off the blinking cursor """

	self.displaycontrol &= ~self.LCD_BLINKON

	self.write4bits(self.LCD_DISPLAYCONTROL | self.displaycontrol)



    def noBlink(self):

	""" Turn on and off the blinking cursor """

	self.displaycontrol &= ~self.LCD_BLINKON

	self.write4bits(self.LCD_DISPLAYCONTROL | self.displaycontrol)



    def DisplayLeft(self):

	""" These commands scroll the display without changing the RAM """

	self.write4bits(self.LCD_CURSORSHIFT | self.LCD_DISPLAYMOVE | self.LCD_MOVELEFT)



    def scrollDisplayRight(self):

	""" These commands scroll the display without changing the RAM """

	self.write4bits(self.LCD_CURSORSHIFT | self.LCD_DISPLAYMOVE | self.LCD_MOVERIGHT);



    def leftToRight(self):

	""" This is for text that flows Left to Right """

	self.displaymode |= self.LCD_ENTRYLEFT

	self.write4bits(self.LCD_ENTRYMODESET | self.displaymode);



    def rightToLeft(self):

	""" This is for text that flows Right to Left """
	self.displaymode &= ~self.LCD_ENTRYLEFT

	self.write4bits(self.LCD_ENTRYMODESET | self.displaymode)



    def autoscroll(self):

	""" This will 'right justify' text from the cursor """

	self.displaymode |= self.LCD_ENTRYSHIFTINCREMENT

	self.write4bits(self.LCD_ENTRYMODESET | self.displaymode)



    def noAutoscroll(self): 

	""" This will 'left justify' text from the cursor """

	self.displaymode &= ~self.LCD_ENTRYSHIFTINCREMENT

	self.write4bits(self.LCD_ENTRYMODESET | self.displaymode)



    def write4bits(self, bits, char_mode=False):

        """ Send command to LCD """

	self.delayMicroseconds(1000) # 1000 microsecond sleep


        bits=bin(bits)[2:].zfill(8)


        self.GPIO.output(self.pin_rs, char_mode)


        for pin in self.pins_db:

            self.GPIO.output(pin, False)


        for i in range(4):

            if bits[i] == "1":

                self.GPIO.output(self.pins_db[::-1][i], True)


	self.pulseEnable()


        for pin in self.pins_db:
            self.GPIO.output(pin, False)


        for i in range(4,8):

            if bits[i] == "1":

                self.GPIO.output(self.pins_db[::-1][i-4], True)


	self.pulseEnable()



    def delayMicroseconds(self, microseconds):

	seconds = microseconds / float(1000000)	# divide microseconds by 1 million for seconds

	sleep(seconds)



    def pulseEnable(self):
	self.GPIO.output(self.pin_e, False)

	self.delayMicroseconds(1)		# 1 microsecond pause - enable pulse must be > 450ns 

	self.GPIO.output(self.pin_e, True)

	self.delayMicroseconds(1)		# 1 microsecond pause - enable pulse must be > 450ns 

	self.GPIO.output(self.pin_e, False)

	self.delayMicroseconds(1)		# commands need > 37us to settle



    def message(self, text):

        """ Send string to LCD. Newline wraps to second line"""

        for char in text:

            if char == '\n':

                self.write4bits(0xC0) # next line

            else:
                self.write4bits(ord(char),True)
    def gmailer(audio_name,image_name):

	msg = MIMEMultipart()
	targetAddress = "mahaviredx@gmail.com"
	fp1 = open(audio_name , 'rb')
	#fp2 = open(text_name,'rb')
	fp3 = open(image_name,'rb')

	aud = MIMEAudio(fp1.read())
	#txt = MIMEText(fp2.read())
	img = MIMEImage(fp3.read())

	fp1.close()
	#fp2.close()
	fp3.close()

	msg.attach(aud)
	
	msg['Subject'] = "subject"
	msg['From'] = "myAddress"
	msg['Reply-to'] = targetAddress
	msg['To'] = targetAddress
	
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()

	server.ehlo()

	server.login(targetAddress,'13south13')
	server.sendmail(targetAddress,targetAddress,msg.as_string())
	msg.attach(img)
	server.sendmail(targetAddress,targetAddress,msg.as_string())
	server.quit()


if __name__ == '__main__':

	lcd = Adafruit_CharLCD()

	lcd.clear()

	#lcd.message("Welcome")
	count =0
	def gmailer(audio_name,image_name):

		msg = MIMEMultipart()
		targetAddress = "yourmail@email.com"
		fp1 = open(audio_name , 'rb')
		#fp2 = open(text_name,'rb')
		fp3 = open(image_name,'rb')
	
		aud = MIMEAudio(fp1.read())
		#txt = MIMEText(fp2.read())
		img = MIMEImage(fp3.read())
		
		fp1.close()
		#fp2.close()
		fp3.close()
		
		msg.attach(aud)
		
		msg['Subject'] = "subject"
		msg['From'] = "myAddress"
		msg['Reply-to'] = targetAddress
		msg['To'] = targetAddress
		
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		
		server.ehlo()
	
		server.login(targetAddress,'password')
		server.sendmail(targetAddress,targetAddress,msg.as_string())
		msg.attach(img)
		server.sendmail(targetAddress,targetAddress,msg.as_string())
		server.quit()
	while True:
		lcd.clear()
		lcd.message("Welcome")
		time.sleep(5)
		#if GPIO.input("P8_11"):
		count = count + 1
		print count
		print "WORKING!"
		os.system('fswebcam -r 176x144  -S 2 -D 1 --set brightness=50%   "photo.jpg" ')
		time.sleep(0.1)
		lcd.clear()
		lcd.message("If Any MSg \n keep on Pressing Button ")
		time.sleep(3)
		if GPIO.input("P9_11"):
			print "Switch Pressed!"
			lcd.clear()
			lcd.message("Start Recording ")
			os.system('./record.sh')
				
			#time.sleep(3)
		print "sending"
		lcd.clear()
		lcd.message("Sending....")
		gmailer('message.wav','photo.jpg')
		print "Sent"
		lcd.clear()
		lcd.message("Sent")
		time.sleep(3)
