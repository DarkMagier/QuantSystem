from bs4 import BeautifulSoup
import requests
heads = {}
heads['User-Agent'] = 'Mozilla/5.0 ' \
                          '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                          '(KHTML, like Gecko) Version/5.1 Safari/534.50'
def handle_html(html):

    soup=BeautifulSoup(html,"html.parser")
    BankNameList=soup.find_all(id="BankNameList")
    print(BankNameList)
def handel_text(text):
    textList = text[15:-3].split('},{')
    resList = []
    for item in textList:
        # print(type(item))
        # print(item)
        node = item.split(',')

        node_dict = dict()
        for i in node:
            j = i.split(':')

            k = j[0]
            v = ":".join(j[1:]).strip("'")
            if v =="":
                v="--"
            node_dict[k] = v
        resList.append(node_dict)
        print(resList)
    return resList
def get_exchange_rate():

    # url="""http://data.bank.hexun.com/other/cms/foreignexchangejson.ashx?callback=ShowDatalist"""
    url="""http://data.bank.hexun.com/other/cms/foreignexchangejson.ashx?callback=ShowDatalist"""
    resp=requests.get(url,headers=heads)
    # handle_html(resp.text)
    # print(resp.text)
    return handel_text(resp.text)
if __name__=='__main__':
    get_exchange_rate()
    import json
    # text=get_exchange_rate()
    # print(text)
    # textList = text[15:-3].split('},{')
    # resList=[]
    # for item in textList:
    #     print(type(item))
    #     print(item)
        # node=item.split(',')
        #
        # node_dict = dict()
        # for i in node:
        #     j=i.split(':')
        #
        #     k=j[0]
        #     v=":".join(j[1:]).strip("'")
        #     node_dict[k]=v
        # resList.append(node_dict)
    # print(resList)
#