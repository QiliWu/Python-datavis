import pylab, random

class Stock(object):
    def __init__(self, price, distribution):
        self.price = price
        self.history = [price]
        self.distribution = distribution
        self.lastChange = 0
        
    def setPrice(self, price):
        self.price = price
        self.history.append(price)
        print 'setPrice'
        
    def getPrice(self):
        print 'getPrice'
        return self.price
        
    def walkIt(self, marketBias, mo):
        oldPrice = self.price
        baseMove = self.distribution() + marketBias
        self.price = self.price * (1.0+baseMove)
        if mo:
            self.price = self.price + random.gauss(.5, .5)*self.lastChange
        if self.price < 0.01:
            self.price = 0.0
        self.history.append(self.price)
        print 'walkIt'
        self.lastChange = oldPrice - self.price
        
    def plotIt(self, figNum):
        pylab.figure(figNum)
        pylab.plot(self.history)
        pylab.title('Closing Price Simulation Run-' + str(figNum))
        pylab.xlabel('Day')
        pylab.ylabel('Price')
        print 'plotIt'
        
def testStockSimulation():
    def runSimulation(stocks, fig, mo):
        print 'runSimulation'
        mean = 0.0
        for s in stocks:
            for d in range(numDays):
                s.walkIt(bias, mo)
            s.plotIt(fig)
            mean += s.getPrice()
        mean = mean/float(numStocks)
        pylab.axhline(mean)
    print 'testStockSimulation'
    pylab.figure(figsize=(12,12))
    numStocks = 20
    numDays = 400
    stocks = []
    bias = 0.0
    mo = False
    startvalues = [100, 500, 200, 300, 100, 100, 100, 200, 200, 300, 300, 400, 500, 300, 300, 100, 100, 100, 200, 200, 300]
    for i in range(numStocks):
        volatility = random.uniform(0, 0.2)
        dl = lambda: random.uniform(-volatility, volatility)
        stocks.append(Stock(startvalues[i], dl))
    runSimulation(stocks, 1, mo)
    
testStockSimulation()
pylab.show()