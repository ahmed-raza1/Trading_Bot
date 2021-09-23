from LiquidityProvider import LiquidityProvider as lp

x = lp('SAMPLE')
# print(x.symbol)
# print(x.provide_live_data())
jsondata = x.provide_live_data()
# print(jsondata)

