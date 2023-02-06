import yfinance as yf
import matplotlib.pyplot as plt

stocks = []
stockstwo = []

class stock:
    def __init__(self, ticker, shares, price, date):
        self.ticker = ticker
        self.shares = shares
        self.price = price
        self.date = date
        
    def plotStocks(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period="1y")
        data["Close"].plot(title=self.ticker)
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.show()
        
    def getValue(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period="1d")
        price = data["Close"][-1]
        rounding = price * self.shares
        return("Value",round(rounding, 2))

    def getPercentChange(self):
        stock = yf.Ticker(self.ticker)
        data = stock.history(period="1d")
        price = data["Close"][-1]
        rounding = ((price - self.price)/self.price)*100
        return("%",round(rounding, 2))

def printPortfolio(stocks):
    filename = input("Enter the name of your txt file: ")
    data = open(filename+".txt", "r")
    for line in data:
        ticker, shares, price, date = line.split(',')
        stocks.append(stock(ticker, float(shares), float(price), date))
    for i in stocks:
        print("Ticker:",i.ticker, "Shares:",i.shares, "Price:",i.price, "Date:",i.date, i.getValue(), i.getPercentChange())
        i.plotStocks()

def compare(stocks, stockstwo):
    filename = input("Enter the name of your txt file: ")
    data = open(filename+".txt", "r")
    for line in data:
        ticker, shares, price, date = line.split(',')
        stocks.append(stock(ticker, float(shares), float(price), date))
    filenametwo = input("Enter the name of the txt file you are comparing against: ")
    data = open(filenametwo+".txt", "r")
    for line in data:
        ticker, shares, price, date = line.split(',')
        comparestock = stock(ticker, float(shares), float(price), date)
        stockstwo.append(comparestock)
    for i in stocks:
        for j in stockstwo:
            if i.ticker == j.ticker:
                print("You: \nTicker:",i.ticker, "\n% Change:", i.getPercentChange())
                print("Other \nTicker:",j.ticker, "\n% Change:", j.getPercentChange())
    
def question():
    option = input("Would you like to see portfolio, compare portfolios, or get help? (portfolio/compare/help): ")
    if option == "portfolio":
        printPortfolio(stocks)
        final = input("Would you like to go again? (y/n): ")
        if final == "y":
            question()
        else:
            print("Goodbye!")
    elif option == "compare":
        compare(stocks, stockstwo)
    elif option == "help":
        print("Add a txt files with the following format: ticker,shares,price,date")
        print("Date is in the format of yyyy-mm-dd")
        print("Example: AAPL,10,100,2020-01-01")
        print("You can add as many stocks as you want, just make sure to add a new line for each stock")
        print("You can also compare two portfolios by entering the name of the txt file you want to compare against")
        print("Example: portfolio.txt, portfolio2.txt")

question()
















    






