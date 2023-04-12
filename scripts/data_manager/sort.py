# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Splits data in both verified and unverified folders
# ===========================================================================

from .. import VERIFIED_DIR, UNVERIFIED_DIR, os, pd
from ..ui_manager import UIHandler


class Sort:
    def __init__(self):
        self.ui = UIHandler()

    # ================================================
    #  *                  sort
    #  ? Sorts either verified or unverified data
    #  @ param verifType string
    #  @ return None
    # ================================================

    def sort(self, verifType):
        try:
            # sort from verified data
            if verifType == 'verified':
                try:
                    df = pd.read_csv(os.path.join(
                        VERIFIED_DIR, 'Kiwisaver Data.csv'))
                    for i, x in df.groupby('Scheme'):
                        p = os.path.join(os.getcwd(), os.path.join(
                            VERIFIED_DIR, '{} Data.csv'.format(i)))
                        x.to_csv(p, index=False)
                        self.ui.plus(str(i + ' Data.csv'))
                    print('\n')
                except FileNotFoundError:
                    self.ui.error(
                        'Error: Verified Data File not found. Skipping.')

            if verifType == 'unverified':
                # sort from unverified data
                try:
                    df = pd.read_csv(os.path.join(
                        UNVERIFIED_DIR, 'Kiwisaver Data.csv'))
                    for i, x in df.groupby('Scheme'):
                        p = os.path.join(os.getcwd(), os.path.join(
                            UNVERIFIED_DIR, '{} Data.csv'.format(i)))
                        x.to_csv(p, index=False)
                        self.ui.plus(str(i + ' Data.csv'))
                    print('\n')
                except FileNotFoundError:
                    self.ui.error(
                        'Error: Unverified Data File not found. Skipping.')
            else:
                raise Exception()
        except Exception as e:
            pass
