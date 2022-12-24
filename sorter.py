import pandas as pd
import os

df = pd.read_csv('Kiwisaver Data.csv')
for i, x in df.groupby('Scheme'):
    p = os.path.join(os.getcwd(), "{} Data.csv".format(i))
    x.to_csv(p, index=False)