import requests
from datetime import datetime
#API link
URL="https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"

prev_bitcoin=0
count=0
def getPRice(coin,currency):
    try:
        response=requests.get(URL.format(coin,currency)).json()
        return response
    except:
        return False

while True:
    date_time=datetime.now()
    date_time=date_time.strftime("%d/%m/%Y %H:%M:%S")


    if count==0:
        currentPrice = getPRice("BTC", "USD")
        prev_bitcoin=currentPrice["USD"]

        currentPrice2 = getPRice("BTC", "USD")
        prev_Ethereum = currentPrice["USD"]
        count+=1


    currentPrice= getPRice("BTC","USD")
    currentPrice2=getPRice("ETH","USD")
    print(12*'  '+'Bitcoin', 6*'  '+'Ethereum')

    prev_bitcoin = currentPrice["USD"] - prev_bitcoin
    prev_Ethereum = currentPrice2["USD"] - prev_Ethereum


    if prev_bitcoin > 0:
        arrow=u'\u2191'

    elif prev_bitcoin < 0:
        arrow=u'\u2193'

    else:
        arrow='-'


    if prev_Ethereum > 0:
        arrow2=u'\u2191'

    elif prev_Ethereum < 0:
        arrow2=u'\u2193'

    else:
        arrow2='-'

    if currentPrice:

        print(date_time,' | ',arrow," $",currentPrice["USD"],'  |  ',arrow2,' $',currentPrice2["USD"],'\n')
