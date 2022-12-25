import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import matplotlib.pyplot as plt

url = "https://www.asb.co.nz/iFrames/investmentPerformance.asp"
header = {'User-Agent':str(UserAgent().random)}
r = requests.get(url, headers=header)

df_list = pd.read_html(r.text)
df = df_list[2]
df.rename(columns={'ASB KiwiSaver Scheme fund':'Scheme', 'Sell price':'Price'}, inplace=True)


# show period over time



# show fixed point in time
plt.figure(1)
for i in df.index:
    plt.bar(df['Scheme'][i], df['Price'][i])
plt.title('Fund Scheme vs Unit Price Today')
plt.ylabel('Unit Price')
plt.show()