from coinmarketcap import CoinMarketCap
import json
from common.models import Coin

cmc = CoinMarketCap()
print(cmc.stats())
coin_list = cmc.ticker()
for coin in coin_list:
    print(coin)
#print(json.dumps(cmc.ticker("iota")))
