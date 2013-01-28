from random import uniform

class Portfolio(object):
  def __init__(self):
    self.stocks = dict()
    self.funds = dict()
    self.cash = 0  
    self.history = []
#  def __repr__(self):
#    y = []
#	z = []
#	x = "cash: $ %d" % (self.cash)
#	y.append(for i in self.stocks: print "stocks: %d %s" % (self.stocks[i], i))
#    z.append(for j in self.funds: print "funds: %d %s" % (self.funds[j], j))
#    return
#	  """
#	  %s \n
#	  %s \n
#	  %s \n
#	  """ % (x, y, z)
  def addCash(self, dollas):
    self.cash += dollas
    self.history.append("Added %d dollars in cash to portfolio" % (dollas))
  
  def withdrawCash(self, dollas):
    if self.cash < dollas:
      return "You can't do that!"
    else:
      self.cash -= dollas
      self.history.append("Withdrew %d dollars in cash from portfolio" % (dollas))

  def buyStock(self, amount, stock):
    if self.cash < amount*stock.price:
      return "Zoidy want to buy on margin! But he can't!"
    else:
      if stock.ticker in self.stocks:
        self[stock.ticker] += amount
      else:
        self.stocks[stock.ticker] = amount
      self.cash -= amount*stock.price
      self.history.append("Bought %d shares of %s stock for $%d" % (amount, stock.ticker, amount*stock.price))


  def buyMutualFund(self, amount, fund):
    if self.cash < amount:
      return "Would you like to buy some CDS's too? Its people like you who got us into this mess. No funds for you."
    else:
      if fund.ticker in self.funds:
        self.funds[fund.ticker] += amount
      else:
        self.funds[fund.ticker] = amount
      self.cash -= amount
      self.history.append("Bought %d shares of %s mutual fund" % (amount, fund.ticker))
  
  def sellMutualFund(self, amount, fund):
    if fund.ticker in self.funds:
      self.funds[fund.ticker] -= amount
      price = amount*uniform(0.9, 1.2)
      self.cash += price * amount
      self.history.append("Sold %d shares f %s mutual fund for %r each." %(amount, fund.ticker, price))
    else:
      return "Do you have a bridge in Brooklyn to sell me too?"
  
  def sellStock(self, amount, stock):
    if stock.ticker in self.stocks:
      self.stocks[stock.ticker] -= amount
      sprice = amount*uniform(stock.price * .5, stock.price * 1.5)
      self.cash += sprice * amount
      self.history.append("Sold %d shares f %s stock fund for %r each." %(amount, stock.ticker, sprice))
    else:
      return "You're like the \'ATT\' of people?"
class Stock():
  def __init__(self, price, ticker):
    self.price = price
    self.ticker = str(ticker)

class MutualFund():
  def __init__(self, ticker):
    self.ticker = str(ticker)

portfolio = Portfolio()
portfolio.addCash(7)
portfolio.withdrawCash(1.5)
s = Stock(3, "XXX")
f = MutualFund("Penis")
portfolio.buyStock(3, s)
portfolio.buyMutualFund(1, f)
print portfolio.history
print portfolio
