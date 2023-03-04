import requests
__request_headers = {
        'Host':'www.nseindia.com', 
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 
        'Accept-Language':'en-US,en;q=0.5', 
        'Accept-Encoding':'gzip, deflate, br',
        'DNT':'1', 
        'Connection':'keep-alive', 
        'Upgrade-Insecure-Requests':'1',
        'Pragma':'no-cache',
        'Cache-Control':'no-cache',    
    }
try:
    print("om")
    nse_url = 'https://www.nseindia.com/market-data/top-gainers-loosers'
    url = 'https://www.nseindia.com/api/live-analysis-variations?index=gainers'
    resp = requests.get(url=nse_url, headers=__request_headers)
    print("yes 18")
    if resp.ok:
        req_cookies = dict(nsit=resp.cookies['nsit'], nseappid=resp.cookies['nseappid'], ak_bmsc=resp.cookies['ak_bmsc'])
        tresp = requests.get(url=url, headers=__request_headers, cookies=req_cookies)
        result = tresp.json()
        res_data = result["NIFTY"]["data"] if "NIFTY" in result and "data" in result["NIFTY"] else []
        if res_data != None and len(res_data) > 0:
            __top_list = res_data
except OSError as err:
    print('Unable to fetch data')