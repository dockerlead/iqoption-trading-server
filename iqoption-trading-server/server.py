from settings import *
from iqoptionapi.stable_api import IQ_Option
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
I_want_money=IQ_Option(os.getenv("IQ_OPTION_USER"), os.getenv("IQ_OPTION_PASSWORD"))
I_want_money.connect()

ACTIVES="GBPUSD"
INTERVAL=60
COUNT=5
print("Start getting candles ... ============================>")
print(I_want_money.get_candles(ACTIVES, INTERVAL, COUNT, time.time()))

