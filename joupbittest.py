import time
import pyupbit
import datetime
access = "lbdlZIyxg4hPvsftgCUHOKbZn2iQSIRkw5pO26ba"
secret = "HV61qOFnlesQrzVwHYeGQ5JfQ6zlsB03ZIW6eJRp"
def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price
def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time
def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]
# 로그인
upbit = pyupbit.Upbit(access,secret)
print(upbit.get_balance("KRW"))
print("autotrade start")
# 자동매매 시작
while True:
    try:
        #이더리움
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH")
        end_time = start_time + datetime.timedelta(days=1)
        if start_time < now < end_time - datetime.timedelta(minutes=10):
            target_price = get_target_price("KRW-ETH", 0.2)
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price:
                a1 = upbit.get_balance("KRW-ETH")
                if a1 < 0.1 : 
                    upbit.buy_market_order("KRW-ETH", 500000)
                    
        else:
            a1 = upbit.get_balance("KRW-ETH")
            if a1 > 0.00008:
                upbit.sell_market_order("KRW-ETH", upbit.get_balance("KRW-ETH"))
                        
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1) 

    
    try:    
        #라이트코인
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-LTC")
        end_time = start_time + datetime.timedelta(days=1)
        if start_time < now < end_time - datetime.timedelta(minutes=9):
            target_price = get_target_price("KRW-LTC", 0.5)
            current_price = get_current_price("KRW-LTC")
            if target_price < current_price:
                a2 = upbit.get_balance("KRW-LTC")
                if a2 < 1 : 
                    upbit.buy_market_order("KRW-LTC", 500000)
                    
        else:
            a2 = upbit.get_balance("KRW-LTC")
            if a2 > 0.05:
                upbit.sell_market_order("KRW-LTC", upbit.get_balance("KRW-LTC"))
                        
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1) 

    try:    
        #테조스
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-XTZ")
        end_time = start_time + datetime.timedelta(days=1)
        if start_time < now < end_time - datetime.timedelta(minutes=8):
            target_price = get_target_price("KRW-XTZ", 0.5)
            current_price = get_current_price("KRW-XTZ")
            if target_price < current_price:
                a3 = upbit.get_balance("KRW-XTZ")
                if a3 < 1 : 
                    upbit.buy_market_order("KRW-XTZ", 500000)
                    
        else:
            a3 = upbit.get_balance("KRW-XTZ")
            if a3 > 1 :
                upbit.sell_market_order("KRW-XTZ", upbit.get_balance("KRW-XTZ"))
                        
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)     

    
    try:    
        #네오
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-NEO")
        end_time = start_time + datetime.timedelta(days=1)
        if start_time < now < end_time - datetime.timedelta(minutes=7):
            target_price = get_target_price("KRW-NEO", 0.5)
            current_price = get_current_price("KRW-NEO")
            if target_price < current_price:
                a4 = upbit.get_balance("KRW-NEO")
                if a4 < 1 : 
                    upbit.buy_market_order("KRW-NEO", 500000)
                    
        else:
            a3 = upbit.get_balance("KRW-NEO")
            if a4 > 1 :
                upbit.sell_market_order("KRW-NEO", upbit.get_balance("KRW-NEO"))
                        
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)    

   