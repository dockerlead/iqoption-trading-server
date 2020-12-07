from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import os

goal="EURUSD"
size=10#size=[1,5,10,15,30,60,120,300,600,900,1800,3600,7200,14400,28800,43200,86400,604800,2592000,"all"]
maxdict=1
I_want_money=IQ_Option(os.getenv("IQ_OPTION_USER"), os.getenv("IQ_OPTION_PASSWORD"))

def start_candles_stream():
    I_want_money.connect()
    print("Start receiving stream from iqoption.com ...")
    I_want_money.start_candles_stream(goal,size,maxdict)


def get_real_time_candles():
    """
    Once you got a chunk by this function, you need to call `time.sleep(1)`
    """
    candles=I_want_money.get_realtime_candles(goal,size)
    inputs = []
    input = {
        'Open': 0,
        'High': 0,
        'Low': 0,
        'Close': 0,
        'Volume': 0,
        'timestamp': 0,
        'Date': ''
    }
    for timestamp in candles:
        input["Open"]      = candles[timestamp]["open"]
        input["High"]      = candles[timestamp]["max"]
        input["Low"]       = candles[timestamp]["min"]
        input["Close"]     = candles[timestamp]["close"]
        input["Volume"]    = candles[timestamp]["volume"]
        input["timestamp"] = timestamp
        input["Date"] = datetime.utcfromtimestamp(timestamp).strftime("%Y/%m/%d, %H:%M:%S")
        inputs.append(input)
    return inputs    


def stop_candles_stream():
    I_want_money.stop_candles_stream(goal,size)

