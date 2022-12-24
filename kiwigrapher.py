# if pd.read_html does not work, we can use pd.read_html using requests.
import pandas as pd
import requests
from fake_useragent import UserAgent
import matplotlib.pyplot as plt

url = "https://www.asb.co.nz/iFrames/investmentPerformance.asp"
header = {'User-Agent':str(UserAgent().random)}
r = requests.get(url, headers=header)

df_list = pd.read_html(r.text)
df = df_list[2]
df.drop('Date', axis=1, inplace=True)
df.rename(columns={'ASB KiwiSaver Scheme fund':'Scheme', 'Sell price':'Price'}, inplace=True)

plt.figure(1)
plt.bar(df['Scheme'], df['Price'])
plt.title('Costs per price')
plt.ylabel('Cost per unit (NZD$)')
plt.xlabel('ASB KiwiSaver Scheme')
plt.show()
