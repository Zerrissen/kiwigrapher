# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Sorter for Kiwigrapher. Used to sort Kiwigrapher data files.
# ===========================================================================

from os import getcwd, path
import pandas as pd


def sort():
    try:
        df = pd.read_csv('Data\Kiwisaver Data.csv')
        for i, x in df.groupby('Scheme'):
            p = path.join(getcwd(), 'Data\{} Data.csv'.format(i))
            x.to_csv(p, index=False)
    except FileNotFoundError:
        print('Error: File not found')


if __name__ == '__main__':
    sort()
