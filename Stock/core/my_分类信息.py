import requests
import time
import gevent
# Math.floor((new Date().getTime()) / 30000)
# codeMarket="000001"

# print(time.time())
# print(nowTime)
# url="""http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=000001&sty=DCRRB&st=z&sr=&p=&ps=&cb=&js=var%20zjlx_hq%20=%20{%22quotation%22:[(x)]}&token=3a965a43f705cf1d9ad7e1a3e429d622&rt=51034666"""
def getStock(code,market):
    # print(market, code)
    nowTime = str(int(time.time() / 30))
    codeMarket=code+str(market)
    url = """http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&sty=DCARQRQB&st=z&sr=&p=&ps=&cb=tiny.loadQuote.urlCb&js=&token=1942f5da9b46b069953c873404aad4b5&cmd=%s&rt=%s""" % (
    codeMarket, nowTime)
    # print(url)
    req = requests.get(url)
    print(req.text)
for code in range(0,1000000):
    code_str=str(code).zfill(6)
    # for market in range(1,3):
    market=1
    getStock(code_str,market)
        # g=gevent.spawn(getStock,code,market)
        # g.start()

