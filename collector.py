from coinmarketcap import CoinMarketCap
import json
from common.models import Coin

cmc = CoinMarketCap()
print(cmc.stats())
coin_list = cmc.ticker()
for coin in coin_list:
    print(coin)
    coin_id = int(coin['id'])
    last_updated = coin['last_updated']
    if not Coin.objects(coin_id = coin_id, last_updated = last_updated):
        print('updating ', coin_id, ' at ', last_updated)
        new_coin = Coin()
        new_coin.coin_id = coin.id
        new_coin.name = coin.name
        new_coin.symbol = coin.symbol
        new_coin.rank = coin.rank
        new_coin.price_usd = coin.price_usd
        new_coin.price_btc = coin.price_btc
        new_coin.volume_usd_24h = coin['24h_volume_usd']
        new_coin.market_cap_usd = coin.market_cap_usd
        new_coin.available_supply = coin.available_supply
        new_coin.total_supply = coin.total_supply
        new_coin.percent_change_1h = coin.percent_change_1h
        new_coin.percent_change_24h = coin.percent_change_24h
        new_coin.percent_change_7d = coin.percent_change_7d
        new_coin.last_updated = coin.last_updated
        new_coin.save()
    else:
        print(coin_id, ' updated at ', last_updated)
#print(json.dumps(cmc.ticker("iota")))
