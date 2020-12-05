from settings import *
# from fastapi import FastAPI
from services.iqoption_service import *

# app = FastAPI()

start_candles_stream()
while True:
    chunk = get_real_time_candles()
    print(chunk)
stop_candles_stream()

