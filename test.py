import json
import requests
from bs4 import BeautifulSoup

import datetime


def Telegram_data():

    print("Telegram_data add")
    dtobj1 = datetime.datetime.utcnow()  # utcnow class method
    stockcode = ['ADANIENT', 'ADANIPORTS', 'APOLLOHOSP', 'ASIANPAINT', 'AXISBANK', 'BAJAJ-AUTO', 'BAJFINANCE', 'BAJAJFINSV', 'BPCL', 'BHARTIARTL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DIVISLAB', 'DRREDDY', 'EICHERMOT', 'GRASIM', 'HCLTECH', 'HDFCBANK', 'HDFCLIFE', 'HEROMOTOCO', 'HINDALCO',
                 'HINDUNILVR', 'HDFC', 'ICICIBANK', 'ITC', 'INDUSINDBK', 'INFY', 'JSWSTEEL', 'KOTAKBANK', 'LT', 'M&M', 'MARUTI', 'NTPC', 'NESTLEIND', 'ONGC', 'POWERGRID', 'RELIANCE', 'SBILIFE', 'SBIN', 'SUNPHARMA', 'TCS', 'TATACONSUM', 'TATAMOTORS', 'TATASTEEL', 'TECHM', 'TITAN', 'UPL', 'ULTRACEMCO', 'WIPRO']
    # print(stockcode)
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

    headers = {
        
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        # 'accept-encoding': 'gzip, deflate, br',
        # 'accept-language': 'en-US,en;q=0.9'
    }
    response = requests.get(url, headers=headers).content
    data = json.loads(response.decode('utf-8'))
    nifty_val = 0
    count = 0
    nifty_val = data['filtered']['data'][0]['PE']['underlyingValue']
    print("nifty_val", nifty_val)

    for i in range(len(stockcode)):
            try:
                stock_url = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + \
                    str(stockcode[i])
                print(stock_url)
                
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
                response = requests.get(stock_url, headers=headers)
                # response
                soup = BeautifulSoup(response.text, 'html.parser')
                data_array = soup.find(id='responseDiv').getText()

                y = json.loads(data_array)

                latest_price = (y['data'][-1]['lastPrice'])
                latest_price = latest_price.replace(',', '')
                print("latest", latest_price)
                latest_price = float(latest_price)

                # name = "SUNPHARMA"

                url = f'https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol={stockcode[i]}&smeFlag=0&itpFlag=0'
                # headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

                soup = BeautifulSoup(requests.get(
                    url, headers=headers).content, 'html.parser')
                data = json.loads(soup.select_one('#responseDiv').text)

                # uncomment this to print all data:
                # print(json.dumps(data, indent=4))
                vwap = (data['data'][0]['averagePrice'])
                vwap = vwap.replace(',', '')
                vwap = float(vwap)
                # print("v",type(vwap))
                # print("latest_price",type(latest_price))
                vwap = float(vwap)

                print('vwap:', data['data'][0]['averagePrice'])

                if(latest_price > vwap):
                    count = count + 1
                # print("yes big")
                # else:
                #   # print("small")
            except Exception as e:
                print("ERROR : "+str(e))

    print("count", count)
    if(count >= 40):
        print("Count is high")
        # Send_high()
    if(count <= 10):
        print("Count is low")
        
        # Send_low()

Telegram_data()