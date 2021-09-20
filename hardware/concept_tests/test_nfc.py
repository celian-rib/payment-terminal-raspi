from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

pn532 = Pn532_i2c()
pn532.SAMconfigure()

while True :
	print("Waiting for card :")
	card_data = pn532.read_mifare().get_data()

	print(card_data)
