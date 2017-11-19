import json
from websocket import create_connection
import sys
import json
import hmac,hashlib
import requests
import pandas as pd


class PoloAPI(object):


    def __init__(self):
            
            self.POLOpush = 'wss://api2.poloniex.com'
            self.POLOpublicAPI = "https://poloniex.com/public?command="
            self.POLOAPITrade = 'https://poloniex.com/tradingApi'
            self.POLOAPIKey = ""
            self.POLOAPISecret = ""



    def importdata(self, data, **kwargs):
            print("File Importing... \n ")
            df = pd.DataFrame(data)
            self.displaydata(df)

    def PublicReq(self, requrl, *args, **kwargs):
    		print('Pulling Data :\t', requrl)
    		req = requests.get(requrl)
    		rj = req.json()
    		df = pd.DataFrame(rj)
    		print(df)
                            





    def displaydata(self, data, **kwargs):
            print(data)
                                    

class urlz():

	def __init__(self, https=True):

		default_value = 'None'

		self.PoloAPI={'Push' : 'wss://api.poloniex.com',
			'Public' : 'https://poloniex.com/public?command=',
			'Private' : 'https://poloniex.com/tradingApi',
			}

		self.Public ={
	        'OrderBook' : 'returnOrderBook', 
	        'TradeHistory' : 'returnTradeHistory', # &currencyPair={pair}&start={timestart}&end={timeend}',  #Returns the past 200 trades for a given market, or up to 50,000 trades; "start" and "end" GET parameters.
	        'ChartData' : 'returnChartData', #&currencyPair' # ={pair}&start={timestart}&end={timened}&period={timeperiod}'
	        'Currencies' : 'returnCurrencies', #returns info about currencies
	        'LoanOrders' : 'returnLoanOrders',
	        }

		self.PoloTrade = {
	        'Balances' : 'returnBalances',                  # Returns all of your available balances. 
	        'totalBalances' : 'returnCompleteBalances',     # Returns all of your balances.                         
	        'Address' : 'returnDepositAddresses',           # Returns all of your deposit addresses.                
	        'NewAdress' : 'generateNewAddress',             # Generates a new deposit address for the currency.     REQD: "currency"  
	        'DepositHistory' : 'returnDepositsWithdrawals', # Returns your deposit and withdrawal history.          REQD: "start" "end" 
	        'OpenOrders' : 'returnOpenOrders',              # Returns your open orders for a given market.          REQD: "currencyPair"
	        'TradeHistory' : 'returnTradeHistory',          # Returns your trade history for a given market.        REQD: "currencyPair", "rate", "amount"
	        'sell' : 'sell',                                # Places a sell order in a given market.                REQD: "currencyPair", "rate", "amount"
	        'cancelOrder' : 'cancelOrder',                  # Cancels an order you have placed in a given market.   REQD: "orderNumber".
	        'moveOrder' : 'moveOrder',                      # Cancels an order and places a new one                 REQD: "orderNumber", "rate";                OPTIONAL: "amount",  "postOnly", "immediateOrCancel"
	        'withdraw' : 'withdraw',                        # Immediately places a withdrawal for a given currency  REQD: "currency", "amount", "address".
	        'FeeInfo' : 'returnFeeInfo',                    # Returns your trading fees and trailing 30-day volume  REQD:
	        'Balances' : 'returnAvailableAccountBalances',  # Returns your balances sorted by account.              REQD:                                       OPTIONAL: "account"
	        'TradableBalances' : 'returnTradableBalances',  # Returns your tradable balances in each market.        REQD: 
	        'transferBalance' : 'transferBalance',          # Transfers funds from one account to another,          REQD: "currency", "amount", "fromAccount", and "toAccount".
	        'marginaccount' : 'returnMarginAccountSummary', # Returns a summary of your entire margin account.      REQD:
	        'marginBuy' : 'marginBuy',                      # Places a margin buy order in a given market.          REQD:  "currencyPair", "rate", "amount"     OPTIONAL: "lendingRate"
	        'marginSell' : 'marginSell',                    # Places a margin sell order in a given market.         REQD: "currencyPair", "rate",  "amount"     OPTIONAL: "lendingRate"
	        'marginPosition' : 'getMarginPosition',         # Returns information about your margin position.       REQD:  "currencyPair"
	        'closeMargin' : 'closeMarginPosition',          # Closes your margin position in a given market.        REQD: "currencyPair"
	        'createLoan' : 'createLoanOffer',               # Creates a loan offer for a given currency.            REQD:  "currency", "amount", "duration", "autoRenew" (0 or 1), "lendingRate"
	        'cancelLoanOffer' : 'cancelLoanOffer',          # Cancels a loan offer.                                 REQD: "orderNumber"     
	        'OpenLoans' : 'returnOpenLoanOffers',           # returns your open loan offers for each currency.      REQD: 
	        'ActiveLoans' : 'returnActiveLoans',            # Returns your active loans for each currency.          REQD: 
	        'LendingHistory' : 'returnLendingHistory',      # Returns your lending history within a time range.     REQD: "start", "end"
	        'AutoRenewLoan' : 'toggleAutoRenew',            # Toggles the autoRenew setting on an active loan.      REQD: "orderNumber"
	        }



		self.Public_command = {

		'CurrPair' : '&currencyPair=',
		'start' : '&start=',
		'end' : '&end=',
		'period' : '&period='

		}


	def add(self, command = 'None', CurrPair = 'None', *args, **kwargs):

		if (command == 'OrderBook'):										#orderbook command
			url = self.PoloAPI['Public'] + self.Public['OrderBook']
			if (CurrPair!='None'):											#check for currency pair
				return (url + self.Public_command['CurrPair'] + CurrPair)

			else: 
				print('OrderBook no CurrPair')
				return url 												#failsafe

		elif (command == 'Currencies'):
			url = self.PoloAPI['Public'] + self.Public['Currencies']
			print(url)
			return url





	def Command(self, command, *args, **kwargs):
		print(args, kwargs)
		Commandupdate = dict.fromkeys(
			[
			(self.Public['OrderBook']),
			(self.Public['TradeHistory']),
			(self.Public['ChartData']),
			(self.Public['Currencies']),
			(self.Public['LoanOrders'])],
			default_value)




#def Arguments(self, *args, **kwargs):




api = PoloAPI()
url = urlz()

requrl = url.add('OrderBook', CurrPair = 'USDT_ETH')
api.PublicReq(requrl)

requrl = url.add('Currencies')
api.PublicReq(requrl)
