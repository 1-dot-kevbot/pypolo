### COPIED FROM PASTEBIN USER THIS IS NOT MY CODE!!!

### This creates a connection to the new poloniex api  wss://api2.poloniex.com
### There is currently no documentation for this but all of the javascript to
### access it is directly readable from the poloniex webpage so I don't think they
### will have a problem with me sharing a python version here.
### The new poloniex API works on Websockets, I adapted some code I found for
### connecting to Bitfinex.  You can send commands in json format.  I have identified
### two types of commands.
### Commands:
###     subscribe: this allows subscription to a channel and from then on receives
###                 all pushes from the websocketWrap server for that channel
###     private: this allows actions to be performed on your account. I don't know how
###                 to authenticate from python at the moment so can't use this function.
### There are several channels which can be subscribed to:
### Channels:
###     1000: USER, this requires login authentication which I don't know how to do
###     1001: TROLLBOX, currently disabled
###     1002: TICKER, returns ticker each time a trade is made
###     1003: FOOTER, returns server time, the users online and total 24 hour volume for each of the primary currency markets
###             approximately once every 20 seconds.
###     1010: HEARTBEAT, this channel does not need subscribing to but will message to
###             show connection is alive approximately once per second.
###     PCU_SCU: MARKET, returns trades and orders in realtime for the currency pair channel
###                 in format Primary CUrrency, Secondary CUrrency "PCU_SCU"
 
### Outputs:
### ON SUBSCRIPTION: A JSON list will be returned - [channelName, 1]
### ON UNSUBCRIPTION: A JSON list will be returned - [channelName, 0]
### ON MESSAGE: A JSON list will be returned - [channelName, ID, results], the ID is for a feed of actions to
###             allow checking that all have been received e.g. MARKET. For channels 1002 and 1003 which are
###             a state (point in time information), there is no ID given.
 
### Types will be returned for the MARKET subscriptions
### Types:
###
### Results:
### The result returned for channels 1002 and 1003 and PCU_SCU will be a JSON list with the following variables
###     1002: [currencyID, last, lowestAsk, highestBid, percentChange, baseVolume, quoteVolume, isFrozen, high24hr, low24hr]
###         currencyID and isFrozen are integers, all others are unicode.
###     1003: [u'yyyy-mm-dd hh:mm', usersOnline , Dictionary {primaryCurrencySymbol:24hourVolume}
###     PCU_SCU: List of lists
###         either
###             order: ["o", bidask, rate, amount]
###             trade: ["t", tradeID, buysell, rate, amount, date]
### bidask 1:bid 0:ask
### buysell 1:buy 0:sell
  

import json
 
from websocket import create_connection
 
poloniex = "wss://api2.poloniex.com"
bitfinex = "wss://api2.bitfinex.com:3000/ws"
#kraken = ""
#gdax = ""
#

def unsubscribe(ws):
	ws.send(json.dumps({

		#unsubscribe...

		"command": "unsubscribe",
		"channel": "1002"


		}))
	response = ws.recv()
	response = json.loads(response)
	print("\n unsubbed")

def listen(ws):
	
	while True:
		response = ws.recv()
		response = json.loads(response)
		print(response)


def subscribe(ws):
	ws.send(json.dumps({
		#subscribe to stream
		### The USER channel requires to be logged in
		### Not sure how to do this but works on webpage
    # 
		# ws.send(json.dumps({
		#     "command": "subscribe",
		#     "channel": "1000" // OR currency pair
		#     "userID": ""
		# }))
		# currencypair, 
		
		"command" : "subscribe",
		"channel" : "USDT_ETH",
		"pair" : "ETH_USDT"
		#"userID": ""

		}))

def create_connections(url):
	ws = create_connection(url)
	response = ws.recv()
	print(ws, "\n Connection established to ", url)
	return ws




ws = create_connections(poloniex)
subscribe(ws)
listen(ws)
unsubscribe(ws)
ws.close()
print("success exit")
