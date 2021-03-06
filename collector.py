from ccma.coinmarketcap import CoinMarketCap
from ccma.common.models import Coin, CoinTicker
from elasticsearch import Elasticsearch
import time
import json


def fix_floats(data):
    if isinstance(data,list):
        iterator = enumerate(data)
    elif isinstance(data,dict):
        iterator = data.items()
    else:
        raise TypeError("can only traverse list or dict")

    for i,value in iterator:
        if isinstance(value,(list,dict)):
            fix_floats(value)
        elif isinstance(value,str):
            try:
                data[i] = float(value)
            except ValueError:
                pass
    return data


def coin_market_cap_collect():
    cmc = CoinMarketCap()
    coin_list = cmc.ticker()
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}], http_auth=('elastic', 'changemememe'))
    for coin in coin_list:
        coin_id = coin['id']
        last_updated = coin['last_updated']
        coin_name = coin['name']
        coin_symbol = coin['symbol']
        rank = int(coin['rank'] if coin['rank'] else 0)
        if rank <= 100:
            coin_float = fix_floats(coin)
            print(coin_float)
            es.index(index='coinmarketcap', doc_type='ticker', body=json.dumps(coin_float))
        else:
            print('Skipping ', coin_name)
            # for coin in coin_list:
            #     coin_id = coin['id']
            #     last_updated = coin['last_updated']
            #     coin_name = coin['name']
            #     coin_symbol = coin['symbol']
            #     rank = int(coin['rank'] if coin['rank'] else 0)
            #     if rank <= 100:
            #         cc = Coin.objects(coin_id=coin_id, name=coin_name, symbol=coin_symbol)
            #         if not cc:
            #             cc = Coin()
            #             cc.coin_id = coin_id
            #             cc.name = coin_name
            #             cc.symbol = coin_symbol
            #             cc.save()
            #         else:
            #             cc = cc[0]
            #         if not CoinTicker.objects(coin = cc, last_updated = last_updated):
            #             print('updating ', coin_id, ' at ', last_updated)
            #             new_coin = CoinTicker()
            #             new_coin.coin_id = coin_id
            #             new_coin.name = coin_name
            #             new_coin.symbol = coin_symbol
            #             new_coin.rank = int(coin['rank'] if coin['rank'] else 0)
            #             new_coin.price_usd = float(coin['price_usd'] if coin['price_usd'] else 0)
            #             new_coin.price_btc = float(coin['price_btc'] if coin['price_btc'] else 0)
            #             new_coin.volume_usd_24h = float(coin['24h_volume_usd'] if coin['24h_volume_usd'] else 0)
            #             new_coin.market_cap_usd = float(coin['market_cap_usd'] if coin['market_cap_usd'] else 0)
            #             new_coin.available_supply = float(coin['available_supply'] if coin['available_supply'] else 0)
            #             new_coin.total_supply = float(coin['total_supply'] if coin['total_supply'] else 0)
            #             new_coin.percent_change_1h = float(coin['percent_change_1h'] if coin['percent_change_1h'] else 0)
            #             new_coin.percent_change_24h = float(coin['percent_change_24h'] if coin['percent_change_24h'] else 0)
            #             new_coin.percent_change_7d = float(coin['percent_change_7d'] if coin['percent_change_7d'] else 0)
            #             new_coin.last_updated = int(coin['last_updated'])
            #             new_coin.save()
            #         else:
            #             print(coin_id, ' updated at ', last_updated)
            #     else:
            #         print('skip ', coin_id, ' rank ', rank)


if __name__ == '__main__':
    while True:
        try:
            coin_market_cap_collect()
            time.sleep(240)
        except Exception as ex:
            print(ex)
            time.sleep(60)
