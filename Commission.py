class Commission():

	def __init__(self):
		self.lockPrice = 45
		self.stockPrice = 30
		self.barrelPrice = 25

	def calcular(self, locks, stocks, barrels):

		lockSales = self.lockPrice * locks
		stockSales = self.stockPrice * stocks
		barrelSales = self.barrelPrice * barrels

		sales = lockSales + stockSales + barrelSales

		if sales > 1800 :
			commission = 0.10 * 1000.0
			commission = commission + 0.15 * 800
			commission = commission + 0.20 * (sales - 1800)
		elif sales > 1000:
			commission = 0.10 * 1000.0
			commission = commission + 0.15 * (sales - 1000)
		else:
			commission = 0.10 * sales

		return commission