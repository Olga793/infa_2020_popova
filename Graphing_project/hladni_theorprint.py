import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from time import sleep

DIM = 255
FPS = 25
T_MAX = 400

def coords_transform(coords, scale):
	'''
	Recalculating coordinates.
	Input: screen coords (in pixels)
	Output: mathematical coords on the plate
	'''
	x = scale*(coords[0])
	y = scale*(DIM - coords[1])
	return (x,y)

def hladni(k, n, x, y):
	'''
	Theoretical assumption of the deviation amplitude of a certain point.
	k, n: fluctuation modes
	x, y: point coordinates in the plate system
	returns: the colour to paint that point into. Lowest amplitudes are painted as red, highest - as black
	'''
	res = np.sin(k*np.pi*x) * np.sin(n*np.pi*y) + np.sin(k*np.pi*y) * np.sin(n*np.pi*x)
	res = abs(res)*1.5
	if res < 1:
		return [255*(1-res), 0, 0]
	return [0, 0, 0]
	
def drawing(w):
	'''
	Calculates the required colour for every pixel on game screen and packs them into an array.
	w: a pair of fluctuation modes
	'''
	res = np.zeros((DIM, DIM, 3), dtype=int)
	for i in range(DIM):
		for j in range(DIM):
			i0,j0 = coords_transform((i,j), 1/DIM)
			res[i][j] = hladni(w[0], w[1], i0, j0)
	return res

def redraw_screen(w=[1, 3]):
	'''
	Processes the array of colours into an image to print on the game screen.
	w: a pair of fluctuation modes
	'''
	data = np.array(drawing(w), dtype=int)
	im = Image.frombytes('RGB', (data.shape[1], data.shape[0]), data.astype('b').tostring())
	photo = ImageTk.PhotoImage(image=im)
	return photo
#numpy.random.random((WIDTH,HEIGHT))*100
#game screen


def main():
	#Game screen construction
	root = tk.Tk()
	fr = tk.Frame(root)
	root.geometry(str(DIM) + 'x' + str(DIM))
	canv = tk.Canvas(root, bg='white')
	canv.pack(fill=tk.BOTH, expand=1)

	#Making the image
	photo = redraw_screen([5, 7])			
	main_img = canv.create_image(0,0,image=photo,anchor=tk.NW)
	
	#Letting the program stay around for a little while
	while True:
		canv.update()
		sleep(1/FPS)

main()
