#!/bin/python3
from tkinter import *
import tkinter.font as tkfont
# color applet
background = '#222831'
background2 = '#00adb5'
foreground = '#eeeeee'
foreground2 = '#393e46'
# functions to creat all the modules
# dda function


def putPexil(x: int, y: int, main: Canvas):
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
		putPexil(round(x1), round(y1), main)

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
		x1 = int(xe1.get())
		x2 = int(xe2.get())
		y1 = int(ye1.get())
		y2 = int(ye2.get())
		_dda(main, x1, x2, y1, y1)
		_dda(main, x1, x1, y1, y2)
		_dda(main, x1, x2, y2, y2)
		_dda(main, x2, x2, y1, y2)

	submit = Button(root, text='Run',  command=__ddasqr).grid(
		row=5, column=1, columnspan=2)
	root.title('DDA Square')
	root.mainloop()

#Bresenham drwing lines alghorithm


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
			putPexil(x, y, main)
			x += 1
			if p < 0:
				p = p + (2 * dy)
			else:
				y += 1
				p = p + (2*dy) - (2*dx)

	submit = Button(root, text='Run',  command=__bresnham).grid(
		row=5, column=1, columnspan=2)

	root.title('Bersnham')
	root.mainloop()

# the function to draw a circle
def fCircle():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)
	main.grid(row=0, column=3, rowspan=6)
	Label(root, text='x value of the center', fg=foreground,
            bg=background).grid(row=1, column=1)
	Label(root, text='y value of the center', fg=foreground,
            bg=background).grid(row=2, column=1)
	Label(root, text='raduis value', fg=foreground,
            bg=background).grid(row=3, column=1)
	xe = Entry(root)
	xe.grid(row=1, column=2)
	ye = Entry(root)
	ye.grid(row=2, column=2)
	re = Entry(root)
	re.grid(row=3, column=2)

	def __circle():
		x = int(re.get())
		xc = int(xe.get())
		yc = int(ye.get())
		putPexil(xc, yc, main)
		p = 1-x
		y = 0
		while x >= y:
			putPexil(xc + x, yc+y, main)
			putPexil(xc + y, yc+x, main)
			putPexil(xc + x, yc-y, main)
			putPexil(xc + y, yc-x, main)
			putPexil(xc - x, yc+y, main)
			putPexil(xc - y, yc+x, main)
			putPexil(xc - x, yc-y, main)
			putPexil(xc - y, yc-x, main)
			if p <= 0:
				y += 1
				p = p + 2 * y + 1
			if p > 0:
				y += 1
				x -= 1
				p = p + 2 * y - 2 * x + 1
	submit = Button(root, text='Run',  command=__circle).grid(
		row=4, column=1, columnspan=2)
	root.title('Circle')
	root.mainloop()


def fTransformation():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=600, width=600)
	main.grid(row=0, column=3, rowspan=12)
	Label(root, text='x1', fg=foreground,
            bg=background).grid(row=1, column=1)
	Label(root, text='y1', fg=foreground,
            bg=background).grid(row=2, column=1)
	Label(root, text='x2', fg=foreground,
            bg=background).grid(row=3, column=1)
	Label(root, text='y2', fg=foreground,
            bg=background).grid(row=4, column=1)
	Label(root, text='sx', fg=foreground,
            bg=background).grid(row=5, column=1)
	Label(root, text='sy', fg=foreground,
            bg=background).grid(row=6, column=1)
	Label(root, text='tx', fg=foreground,
            bg=background).grid(row=7, column=1)
	Label(root, text='ty', fg=foreground,
            bg=background).grid(row=8, column=1)
	xe1 = Entry(root)
	xe1.grid(row=1, column=2)
	ye1 = Entry(root)
	ye1.grid(row=2, column=2)
	xe2 = Entry(root)
	xe2.grid(row=3, column=2)
	ye2 = Entry(root)
	ye2.grid(row=4, column=2)
	sxe = Entry(root)
	sxe.grid(row=5, column=2)
	sye = Entry(root)
	sye.grid(row=6, column=2)
	txe = Entry(root)
	txe.grid(row=7, column=2)
	tye = Entry(root)
	tye.grid(row=8, column=2)
	def __draw(x1 :int , x2 : int , y1 :int , y2:int):
		x1 += 300
		x2 += 300
		y1 += 300
		y2 += 300
		_dda(main, x1 , x2 , y1 ,y2)

	def _draw():
		x1 = int(xe1.get())
		x2 = int(xe2.get())
		y1 = int(ye1.get())
		y2 = int(ye2.get())
		__draw(x1, x2, y1, y1)
		__draw(x1, x1, y1, y2)
		__draw(x1, x2, y2, y2)
		__draw(x2, x2, y1, y2)

	def _scale():
		x1 = int(xe1.get())
		y1 = int(ye1.get())
		x2 = int(xe2.get())
		y2 = int(ye2.get())
		sx = int(sxe.get())
		sy = int(sye.get())
		x2 += ((sx-1) * abs(x2 - x1))
		y2 += ((sy-1) * abs(y2 - y1))
		__draw(x1, x2, y1, y1)
		__draw(x1, x1, y1, y2)
		__draw(x1, x2, y2, y2)
		__draw(x2, x2, y1, y2)
	
	def _trans():
		x1 = int(xe1.get())
		y1 = int(ye1.get())
		x2 = int(xe2.get())
		y2 = int(ye2.get())
		tx = int(txe.get())
		ty = int(tye.get())
		x1 += tx
		x2 += tx
		y1 += ty
		y2 += ty
		__draw(x1, x2, y1, y1)
		__draw(x1, x1, y1, y2)
		__draw(x1, x2, y2, y2)
		__draw(x2, x2, y1, y2)
	def _reflx():
		x1 = int(xe1.get())
		y1 = - int(ye1.get())
		x2 = int(xe2.get())
		y2 = - int(ye2.get())
		__draw(x1, x2, y1, y1)
		__draw(x1, x1, y1, y2)
		__draw(x1, x2, y2, y2)
		__draw(x2, x2, y1, y2)

	def _refly():
		x1 = - int(xe1.get())
		y1 = int(ye1.get())
		x2 = - int(xe2.get())
		y2 = int(ye2.get())
		__draw(x1, x2, y1, y1)
		__draw(x1, x1, y1, y2)
		__draw(x1, x2, y2, y2)
		__draw(x2, x2, y1, y2)

	_dda(main ,300,300,0,600)	
	_dda(main ,0,600,300,300)	
	draw = Button(root, text='Draw',  command=_draw).grid( row=9, column=1, columnspan=1)
	draw = Button(root, text='Scale',  command=_scale).grid( row=9, column=2, columnspan=1)
	draw = Button(root, text='translate',  command=_trans).grid( row=10, column=1, columnspan=1)
	draw = Button(root, text='reflx',  command=_reflx).grid( row=10, column=2, columnspan=1)
	draw = Button(root, text='refly',  command=_refly).grid( row=11, column=1, columnspan=2)
	root.title('Transformation')
	root.mainloop()

# A function to draw ellipse

def fElipse():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=500, width=500)
	main.grid(row=0, column=3, rowspan=7)
	Label(root, text='x value of the center', fg=foreground,
            bg=background).grid(row=1, column=1)
	Label(root, text='y value of the center', fg=foreground,
            bg=background).grid(row=2, column=1)
	Label(root, text='x raduis value', fg=foreground,
            bg=background).grid(row=3, column=1)
	Label(root, text='y raduis value', fg=foreground,
            bg=background).grid(row=4, column=1)
	xe = Entry(root)
	xe.grid(row=1, column=2)
	ye = Entry(root)
	ye.grid(row=2, column=2)
	xre = Entry(root)
	xre.grid(row=3, column=2)
	yre = Entry(root)
	yre.grid(row=4, column=2)

	def __draw(x:int , y:int , x1: int, y1: int):
		putPexil(x + x1, y + y1, main)
		putPexil(x + x1, y - y1, main)
		putPexil(x - x1, y + y1, main)
		putPexil(x - x1, y - y1, main)

	def __ellipse():
		xc = int(xe.get())
		yc = int(ye.get())
		rx = int(xre.get())
		ry = int(yre.get())
		x = 0
		y = ry
		p = int((ry ** 2) - (ry * (rx ** 2)) + ((rx ** 2) * .25))
		dx = 2 * (ry ** 2) * x
		dy = 2 * (rx ** 2) * y
		while dx < dy:
			__draw(xc, yc, x, y)
			x += 1
			dx += (2 * (ry ** 2))
			if p >= 0:
				y -= 1
				p += (dx - dy + (ry ** 2))
				dy -= (2 * (rx ** 2))
			else:
				p += (dx + (ry **2 ))
		p = int(((ry ** 2) * (x + .5) * (x + .5)) +
		        ((rx ** 2) * ((y - 1) ** 2) - ((rx ** 2) * (ry ** 2))))
		while y>=0:
			__draw(xc , yc , x, y)
			y-=1
			dy -= (2 * (rx ** 2))
			if p>=0:
				p += (- dy + (rx ** 2))
			else:
				x += 1
				dx += (2 * (ry ** 2))
				p += (dx - dy + (rx ** 2))
	submit = Button(root, text='Run',  command=__ellipse).grid( row=5, column=1, columnspan=2)
	root.title('Elipse')
	root.mainloop()


def fClipping():
	root = Tk()
	root.configure(bg=background)
	main = Canvas(root, bg=foreground, height=600, width=600)
	main.grid(row=0, column=3, rowspan=11)
	Label(root, text='x1', fg=foreground,
            bg=background).grid(row=1, column=1)
	Label(root, text='y1', fg=foreground,
            bg=background).grid(row=2, column=1)
	Label(root, text='x2', fg=foreground,
            bg=background).grid(row=3, column=1)
	Label(root, text='y2', fg=foreground,
            bg=background).grid(row=4, column=1)
	Label(root, text='xMin', fg=foreground,
            bg=background).grid(row=5, column=1)
	Label(root, text='yMin', fg=foreground,
            bg=background).grid(row=6, column=1)
	Label(root, text='xMax', fg=foreground,
            bg=background).grid(row=7, column=1)
	Label(root, text='yMax', fg=foreground,
            bg=background).grid(row=8, column=1)
	xe1 = Entry(root)
	xe1.grid(row=1, column=2)
	ye1 = Entry(root)
	ye1.grid(row=2, column=2)
	xe2 = Entry(root)
	xe2.grid(row=3, column=2)
	ye2 = Entry(root)
	ye2.grid(row=4, column=2)
	xmne = Entry(root)
	xmne.grid(row=5, column=2)
	ymne = Entry(root)
	ymne.grid(row=6, column=2)
	xmxe = Entry(root)
	xmxe.grid(row=7, column=2)
	ymxe = Entry(root)
	ymxe.grid(row=8, column=2)
	def __draw(x1 :int , x2 : int , y1 :int , y2:int):
		_dda(main, x1 , x2 , y1 ,y2)
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	xmin = 0
	ymin = 0
	xmax = 0
	ymax = 0
	LEFT = 1
	RIGHT = 2
	BOTTOM = 4
	TOP = 8
	def _computeCode(x: float, y: float):
		code = 0 
		if x < xmin:
			code |= LEFT
		elif x > xmax:
			code|=RIGHT
		elif y < ymin:
			code|= TOP
		return code

	def _clip():
		x1 = int(xe1.get())
		y1 = int(ye1.get())
		x2 = int(xe2.get())
		y2 = int(ye2.get())
		__draw(x1,x2,y1,y2)
		code1 = _computeCode(x1, y1)
		code2 = _computeCode(x2, y2)
		flag = False
		while True:
			if code1 & code2 != 0:
				break
			if code1 | code2 == 0:
				flag = True
			code = 0
			if code1 != 0:
				code = code1
			else:
				code = code2
			clippx = 0
			clippy = 0
			if (code & TOP) != 0:
				clippx = (((ymax - y1) * (x2 - x1)) / (y2 - y1)) + x1
				clippy = ymax
			elif (code & BOTTOM) != 0:
				clippx = (((ymin - y1) * (x2 - x1)) / (y2 - y1)) + x1
				clippy = ymin
			elif (code & LEFT) != 0:
				clippy = (((xmin - x1) * (y2 - y1)) / (x2 - x1)) + y1
				clippx = xmin

			elif code & RIGHT != 0:
				clippy = (((xmax - x1) * (y2 - y1)) / (x2 - x1)) + x1
				clippx = xmax

			if code == code1:
				x1 = clippx
				y1 = clippy
				code1 = _computeCode(x1, y1)
			elif code == code2:
				x2 = clippx
				y2 = clippy
				code2 = _computeCode(x2, y2)

		return flag
	def _line():
		x1 = int(xe1.get())
		y1 = int(ye1.get())
		x2 = int(xe2.get())
		y2 = int(ye2.get())
		__draw(x1,x2,y1,y2)
	def _area():
		x1 = int(xe1.get())
		y1 = int(ye1.get())
		x2 = int(xe2.get())
		y2 = int(ye2.get())
		xmin = int(xmne.get())
		ymin = int(ymne.get())
		xmax = int(xmxe.get())
		ymax = int(ymxe.get())
		if _clip():
			__draw(int(x1), int(x2), int(y1), int(y2))
	
	draw = Button(root, text='Line',  command=_line).grid( row=9, column=1, columnspan=1)
	draw = Button(root, text='Area',  command=_area).grid( row=9, column=2, columnspan=1)
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

	circle.grid(row=2, column=0)
	trans.grid(row=2, column=1)
	elipse.grid(row=2, column=2)

	clipping.grid(row=3, column=1)

	main.grid(row=0, column=0, columnspan=3)
	root.mainloop()


# Running the main Function
if __name__ == '__main__':
	main()
