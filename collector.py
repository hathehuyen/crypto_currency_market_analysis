from coinmarketcap import CoinMarketCap
import json
from common.models import Coin

cmc = CoinMarketCap()
print(cmc.stats())
coin_list = cmc.ticker()
for coin in coin_list:
    print(coin)
    coin_id = coin['id']
    last_updated = coin['last_updated']
    if not Coin.objects(coin_id = coin_id, last_updated = last_updated):
        print('updating ', coin_id, ' at ', last_updated)
        new_coin = Coin()
        new_coin.coin_id = coin['id']
        new_coin.name = coin['name']
        new_coin.symbol = coin['symbol']
        new_coin.rank = int(coin['rank'])
        new_coin.price_usd = float(coin['price_usd'])
        new_coin.price_btc = float(coin['price_btc'])
        new_coin.volume_usd_24h = float(coin['24h_volume_usd'])
        new_coin.market_cap_usd = float(coin['market_cap_usd'])
        new_coin.available_supply = float(coin['available_supply'])
        new_coin.total_supply = float(coin['total_supply'])
        new_coin.percent_change_1h = float(coin['percent_change_1h'] if coin['percent_change_1h'] else 0)
        new_coin.percent_change_24h = float(coin['percent_change_24h'] if coin['percent_change_24h'] else 0)
        new_coin.percent_change_7d = float(coin['percent_change_7d'] if coin['percent_change_7d'] else 0)
        new_coin.last_updated = int(coin['last_updated'])
        new_coin.save()
    else:
        print(coin_id, ' updated at ', last_updated)
#print(json.dumps(cmc.ticker("iota")))
