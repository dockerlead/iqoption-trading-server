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
        'open': 0,
        'high': 0,
        'low': 0,
        'close': 0,
        'volume': 0,
        'timestamp': 0,
        'formattedTime': ''
    }
    for timestamp in candles:
        input["open"]      = candles[timestamp]["open"]
        input["high"]      = candles[timestamp]["max"]
        input["low"]       = candles[timestamp]["min"]
        input["close"]     = candles[timestamp]["close"]
        input["volume"]    = candles[timestamp]["volume"]
        input["timestamp"] = timestamp
        input["formattedTime"] = datetime.utcfromtimestamp(timestamp).strftime("%m/%d/%Y, %H:%M:%S")
        inputs.append(input)
    return inputs    


def stop_candles_stream():
    I_want_money.stop_candles_stream(goal,size)

