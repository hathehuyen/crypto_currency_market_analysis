from mongoengine import *

class Coin(Document):
    id = StringField(max_length=30)
    name = StringField(max_length=200)
    symbol = StringField(max_length=30)
    rank = IntField()
    price_usd = FloatField()
    price_btc = FloatField()
    volume_usd_24h = FloatField()
    market_cap_usd = FloatField()
    available_supply = FloatField()
    total_supply = FloatField()
    percent_change_1h = FloatField()
    percent_change_24h = FloatField()
    percent_change_7d = FloatField()
    last_updated = IntField()
