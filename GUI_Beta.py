
'''
topframe = Frame(root)
topframe.pack(side=TOP)
midframe = Frame(root)
midframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

button1 = Button(topframe, text = "fuckyes", fg = "red")
button2 = Button(topframe, text = "fuckno", fg="yellow")
button3 = Button(topframe, text = "button3", fg="green")
button4 = Button(bottomframe, text = "Refresh", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


two = Label(root, text="Time", bg="Red", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg="red", fg="black")
three.pack(side=LEFT,fill=Y)


def printkint(event):
	print("Running some shit sooooonnnnn")


label_1 = Label(root, text = "name")
label_2 = Label(root, text = "passward")
entry_1 = Entry(root)
entry_2 = Entry(root)
button1 = Button(root, text="Login!")


#sticky sticks alignment of cells (North, South, East, West)
label_1.grid(row=0,column=0,sticky=E)
label_2.grid(row=1,column=0,sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

chkbox = Checkbutton(root, text="Click if you suck!" )
chkbox.grid(columnspan=2)

button1.grid(row=4, column=1)
button1.bind("<Button-1>", printkint)

'''
'''

from tkinter import *


class Buttons:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame, text="Print Message", command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame, text="QUIT!", command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("Wowzers !!!")

	def contactaliens(self, url):
		print("contactingaliens")


root = Tk()

def leftClick(event):
	print("detected ... Left")
	print("clicklocation:  ")


def middleClick(event):
	print("detected ... middle")
	print("clicklocation:  ")


def rightClick(event):
	print("detected ... Right")
	print("clicklocation:  ")



root = Tk()
b = Buttons(root)
root.mainloop()
'''



from tkinter import *
import sys
import json
import time
from websocket import create_connection


class toolbar:


	def __init__(self, master):
		
		self.master=master

		print("init")
		frame = Frame(master)
		frame.pack()

	def filemenu(self, master):
		

		dropdown = Menu(master)

		master.config(menu=dropdown)

		fileMenu = Menu(dropdown)
		label_1 = Label(master, text = "server: ")
		label_1.pack(side=LEFT)
		button1 = Button(master, text = "Connect",  command = self.serverconf)
		button1.pack(side=LEFT)
		
		self.entry_1 = Entry(master)
		self.entry_1.pack(side=LEFT)

		


		#FILE
		dropdown.add_cascade(label="File", menu=fileMenu)
		#ITEM1
		fileMenu.add_command(label = "New Project", command = self.doNothing)
		#ITEM2
		fileMenu.add_command(label = "Do more of nothing", command = self.doNothing)
		#ITEM3
		fileMenu.add_command(label = "Quit", command = self.quitit)
		#ITEM4
		fileMenu.add_separator()
		
		#EDIT
		editMenu = Menu(dropdown)

		dropdown.add_cascade(label="Edit", menu=editMenu)
		#ITEM1
		editMenu.add_command(label="Copy", command = self.doNothing)

	def doNothing(self):
		print("doing nothing")


	def mainloopinit(self):
		master.mainloop()

	def serverconf(self):
		url = self.entry_1.get()
		self.app = servconnect(self.serverconf, url)

	


	def quitit(self):
		print("its quittin' time!!!")
		sys.exit(0)


class servconnect:


	def __init__(self, master, url):
		self.master = master
		print("Connecting to : ", url)
		ws = self.create_connections(url)
		self.subscribe(ws)
		r = self.listen(ws)
		

	def unsubscribe(self, ws):
		ws.send(json.dumps({

			#unsubscribe...

			"command": "unsubscribe",
			"channel": "1002"


			}))
		response = ws.recv()
		response = json.loads(response)
		print("\n unsubbed")

	def listen(self, ws):
		response = []

		
		r = ws.recv()
		response1 = json.loads(r)
		response2 = json.loads(r)
		response3 = json.loads(r)
		response4 = json.loads(r)
		response5 = json.loads(r)

		print(response5)



		return response


	def subscribe(self, ws):
		ws.send(json.dumps({
			#subscribe to stream
			### The USER channel requires to be logged in
			### Not sure how to do this but works on webpage
			# ws.send(json.dumps({
			#     "command": "subscribe",
			#     "channel": "1000"
			#     "userID": ""
			# }))
			# currencypair, 
			
			"command" : "subscribe",
			"channel" : "USDT_ETH",
			"pair" : "ETH_USDT"
			#"userID": ""

			}))

	def create_connections(self, url):
			ws = create_connection(url)
			response = ws.recv()
			print(ws, "\n Connection established to ", url)
			return ws


### FIX THE FOLLOWING LINES:

''' 
	def makedisconnect(self, master):
		self.button2 = Button(self.master, text = "Disconnect",  command = self.disconnect)
#### self.button2 is the error^^^^


		self.button2.pack(side=LEFT)

	def disconnect(self):
		print("totally disconnecting")
'''

### AttributeError: 'function' object has no attribute 'tk'

def main():

	
	root = Tk()

	tool = toolbar(root)
	tool.filemenu(root)

	root.mainloop()




if __name__ == '__main__':
    main()