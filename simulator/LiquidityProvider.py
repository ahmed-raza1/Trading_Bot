import os

class LiquidityProvider:
    def __init__(self, symbol):
        self.symbol = symbol

    # save the data in the csv file
    def save_data_csv(self):
        pass

    # create a data frame
    def save_df(self):
        pass

    def provide_live_data(self):
        # privide live data
        # pathroute = os.path.abspath(os.path.dirname(__file__))
        pathroute = os.path.abspath(os.path.join(os.getcwd(), ".."))
        print("pathroute for upper layer", pathroute)
        f2 = open(pathroute + '/apisetting/stocks_overview_json.json', 'r')
        jsondata = f2.read()
        f2.close()
        return jsondata

    @staticmethod
    def get_positions(self):
        # provide the current holdings
        pass