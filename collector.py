from coinmarketcap import CoinMarketCap
import json
from mongoengine import *

cmc = CoinMarketCap()
# print(cmc.stats())
# coin_list = cmc.ticker()
# for coin in coin_list:
#     print(coin)
#print(json.dumps(cmc.ticker("iota")))
