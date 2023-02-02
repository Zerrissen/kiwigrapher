import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('Data\Kiwisaver Data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.pivot_table(index='Date', columns='Scheme', values='Price').resample('D').mean()
    df.plot(kind='line')
    plt.legend(loc='upper left')
    plt.style.use('ggplot')
    plt.title('Kiwisaver Fund Unit Prices Over Time')
    plt.ylabel('Unit Price (NZD$)')
    plt.show()

if __name__ == '__main__':
    main()