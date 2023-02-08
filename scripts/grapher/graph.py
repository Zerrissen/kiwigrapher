from .. import DATA_DIR, os, pd, plt


class Graph:
    def __init__(self):
        graph()


def graph():
    df = pd.read_csv(os.path.join(DATA_DIR, 'Kiwisaver Data.csv'))
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.pivot_table(index='Date', columns='Scheme',
                        values='Price').resample('D').mean()
    df.plot(kind='line')
    plt.legend(loc='upper left')
    plt.style.use('ggplot')
    plt.title('Kiwisaver Fund Unit Prices Over Time')
    plt.ylabel('Unit Price (NZD$)')
    plt.show()
