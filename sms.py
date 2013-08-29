#!/usr/bin/python
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import Adafruit_MCP230XX
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep
import MySQLdb
import urllib2
import sys
from os.path import exists
lcd = Adafruit_CharLCDPlate(busnum = 1)

##################################################################
# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "toor", db = "texts")
# prepare a cursor object using cursor() method
cursor = connection.cursor ()

def off():
	lcd.clear()
	lcd.backlight(lcd.OFF)

				
def display():
	cursor.execute ("SELECT * FROM `texts` WHERE `content` IS NOT NULL AND `messagesent` =0 LIMIT 0 , 10")
	data = cursor.fetchall ()
	for row in data :
		lcd.clear()
		lcd.backlight(lcd.BLUE)
		lcd.message("  Incoming \n    SMS")
		sleep(5)
		lcd.clear()
		lcd.backlight(lcd.GREEN)
		lcd.message(row[2])
		sleep(10)
		lcd.clear()
		lcd.backlight(lcd.BLUE)
		lcd.message(" End Of Messages")
		sleep(5)
		cursor.execute ("UPDATE `texts`  SET messagesent = '1' WHERE id = %s" % row[0])
		lcd.clear()
		


display()
off()
# close the cursor object
cursor.close ()

# close the connection
connection.close ()

# exit the program
sys.exit()