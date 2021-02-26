#!/bin/python3
#TODO: dont forget to uncomment the remaing algorithm
from tkinter import *
import tkinter.font as tkfont
# color applet
background = '#222831'
background2 = '#00adb5'
foreground = '#eeeeee'
foreground2 = '#393e46'
# functions to creat all the modules
# dda function


def put_pexil(x: int, y: int, main: Canvas):
	main.create_rectangle(x, y, x+1, y+1)


def _dda(main: Canvas, x1: int, x2: int, y1: int, y2: int):
	dx = abs(x1-x2)
	dy = abs(y1-y2)
	steps = max(dx, dy)
	Xinc = dx / steps
	Yinc = dy / steps
	for i in range(steps):
		x1 += Xinc
		y1 += Yinc
		put_pexil(round(x1), round(y1), main)

# dda line drawing function
def fDda():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)
	main.grid(row=0, column=3, rowspan=7)
	Label(root, text='x1 value', fg=foreground,
		  bg=background).grid(row=1, column=1)
	Label(root, text='y1 value', fg=foreground,
		  bg=background).grid(row=2, column=1)
	Label(root, text='x2 value', fg=foreground,
		  bg=background).grid(row=3, column=1)
	Label(root, text='y2 value', fg=foreground,
		  bg=background).grid(row=4, column=1)
	xe1 = Entry(root)
	xe1.grid(row=1, column=2)
	ye1 = Entry(root)
	ye1.grid(row=2, column=2)
	xe2 = Entry(root)
	xe2.grid(row=3, column=2)
	ye2 = Entry(root)
	ye2.grid(row=4, column=2)
	submit = Button(root, text='Run',  command=lambda: _dda(main, x1=int(xe1.get()), x2=int(
		xe2.get()), y1=int(ye1.get()), y2=int(ye2.get()))).grid(row=5, column=1, columnspan=2)
	root.title('DDA')
	root.mainloop()

# dda square drawing
def fDdasqr():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)
	main.grid(row=0, column=3, rowspan=7)
	Label(root, text='x1 value', fg=foreground,
		  bg=background).grid(row=1, column=1)
	Label(root, text='y1 value', fg=foreground,
		  bg=background).grid(row=2, column=1)
	Label(root, text='x2 value', fg=foreground,
		  bg=background).grid(row=3, column=1)
	Label(root, text='y2 value', fg=foreground,
		  bg=background).grid(row=4, column=1)
	xe1 = Entry(root)
	xe1.grid(row=1, column=2)
	ye1 = Entry(root)
	ye1.grid(row=2, column=2)
	xe2 = Entry(root)
	xe2.grid(row=3, column=2)
	ye2 = Entry(root)
	ye2.grid(row=4, column=2)
	def __ddasqr(): 
		x1=int(xe1.get())
		x2=int(xe2.get())
		y1=int(ye1.get())
		y2=int(ye2.get())
		_dda(main, x1, x2, y1, y1)
		_dda(main, x1, x1, y1, y2)
		_dda(main, x1, x2, y2, y2)
		_dda(main, x2, x2, y1, y2)

	submit = Button(root, text='Run',  command=__ddasqr).grid(row=5, column=1, columnspan=2)
	root.title('DDA Square')
	root.mainloop()


def fbresnham():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)
	main.grid(row=0, column=3, rowspan=7)
	Label(root, text='x1 value', fg=foreground,
		  bg=background).grid(row=1, column=1)
	Label(root, text='y1 value', fg=foreground,
		  bg=background).grid(row=2, column=1)
	Label(root, text='x2 value', fg=foreground,
		  bg=background).grid(row=3, column=1)
	Label(root, text='y2 value', fg=foreground,
		  bg=background).grid(row=4, column=1)
	xe1 = Entry(root)
	xe1.grid(row=1, column=2)
	ye1 = Entry(root)
	ye1.grid(row=2, column=2)
	xe2 = Entry(root)
	xe2.grid(row=3, column=2)
	ye2 = Entry(root)
	ye2.grid(row=4, column=2)
	def __bresnham():
		x = int(xe1.get())
		x2 = int(xe2.get())
		y = int(ye1.get())
		y2 = int(ye2.get())
		dx = x2 - x
		dy = y2 - y
		p = (2*dx) - dy
		while x <= x2:
			put_pexil(x, y, main)
			x += 1
			if p<0:
				p = p + (2 * dy)
			else:
				y+=1
				p = p + (2*dy) - (2*dx)

	submit = Button(root, text='Run',  command = __bresnham ).grid(row=5, column=1, columnspan=2)

	root.title('Bersnham')
	root.mainloop()


def fCircle():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)

	root.title('Circle')
	root.mainloop()


def fTransformation():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)

	root.title('Transformation')
	root.mainloop()


def fElipse():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)

	root.title('Elipse')
	root.mainloop()


def fClipping():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)

	root.title('Clippping')
	root.mainloop()
# main Function


def main():
	root = Tk()
	root.configure(bg=background)
	root.title('Graphics Project')
	myFont = tkfont.Font(family='JetBrains Mono', size=20)
	main = Label(root, text='Please choose one of the following to start',
				 font=myFont, fg=foreground, bg=background)
# make the buttons
	dda = Button(root, font=myFont, bg=background2,
				 fg=foreground2, text='DDA', padx=100, pady=10, command=fDda)
	ddaSqr = Button(root, font=myFont, bg=background2,
					fg=foreground2, text='DDA Square', padx=100, pady=10, command=fDdasqr)
	bres = Button(root, font=myFont, bg=background2,
				  fg=foreground2, text='bresnham', padx=100, pady=10, command=fbresnham)
	circle = Button(root, font=myFont, bg=background2,
					fg=foreground2, text='Circle', padx=100, pady=10, command=fCircle)
	trans = Button(root, font=myFont, bg=background2, fg=foreground2,
				   text='Transformation', padx=100, pady=10, command=fTransformation)
	elipse = Button(root, font=myFont, bg=background2,
					fg=foreground2, text='Elipse', padx=100, pady=10, command=fElipse)
	clipping = Button(root, font=myFont, bg=background2,
					  fg=foreground2, text='Clipping', padx=100, pady=10, command=fClipping)

	dda.grid(row=1, column=0)
	ddaSqr.grid(row=1, column=1)
	bres.grid(row=1, column=2)

	# circle.grid(row=2, column=0)
	# trans.grid(row=2, column=1)
	# elipse.grid(row=2, column=2)

	# clipping.grid(row=3, column=1)

	main.grid(row=0, column=0, columnspan=3)
	root.mainloop()


#
if __name__ == '__main__':
	main()
