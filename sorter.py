import pandas as pd
import os

def sort():
    df = pd.read_csv('Data\Kiwisaver Data.csv')
    for i, x in df.groupby('Scheme'):
        p = os.path.join(os.getcwd(), "\Data\{} Data.csv".format(i))
        x.to_csv(p, index=False)

if __name__ == '__main__':
    sort()