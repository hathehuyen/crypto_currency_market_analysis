import pandas as pd
from common.models import *


df = pd.DataFrame.from_records(CoinTicker.objects())
print(df.head())