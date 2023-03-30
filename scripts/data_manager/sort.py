# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Splits data in both verified and unverified folders
# ===========================================================================

from .. import VERIFIED_DIR, UNVERIFIED_DIR, os, pd


class Sort:
    def __init__(self):
        sort()


def sort():
    # sort from verified data
    try:
        df = pd.read_csv(os.path.join(VERIFIED_DIR, 'Kiwisaver Data.csv'))
        for i, x in df.groupby('Scheme'):
            p = os.path.join(os.getcwd(), os.path.join(
                VERIFIED_DIR, '{} Data.csv'.format(i)))
            x.to_csv(p, index=False)
    except FileNotFoundError:
        print('Error: Verified Data File not found. Skipping.')

    # sort from unverified data
    try:
        df = pd.read_csv(os.path.join(UNVERIFIED_DIR, 'Kiwisaver Data.csv'))
        for i, x in df.groupby('Scheme'):
            p = os.path.join(os.getcwd(), os.path.join(
                UNVERIFIED_DIR, '{} Data.csv'.format(i)))
            x.to_csv(p, index=False)
    except FileNotFoundError:
        print('Error: Unverified Data File not found. Skipping.')
