from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()

TOKEN = 'pk_0c38a77cb70e40348dd01fc20f5bfa1f'

aapl = Stock('FB', token=TOKEN)
data = aapl.get_quote()
pp.pprint(data)
print(data['companyName'], data['latestPrice'])



