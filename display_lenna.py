import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

import Image

def indexed():
	H = 128
	W = 128
	img = Image.open("lenna_16colors_mci128x128.png", "r")
	for row in range(W):
		for col in range(H):
			pixel = img.getpixel((row,col))
			
			mc.setBlock(row,-1*col-H, 0, block.WOOL.id, pixel)

def normal_images():
	W=128
	H=128
	img = Image.open("Lenna128x128.png", "r")
	# img = Image.open("MeGusta128x128.png", "r")
	# img = Image.open("Lenna128x128_nocolor.png", "r")
	# img = Image.open("grumpycat128x128.png", "r")
	# img = Image.open("grumpycat64x64_nocolor.png", "r")
	COLORS = [ 
		(221,221,221),
		(219,125,62),
		(179,80,188),
		(107,138,201),
		(177,166,39),
		(65,174,56),
		(208,132,153),
		(64,64,64),
		(154,161,161),
		(46,110,137),
		(126,61,181),
		(46,56,141),
		(79,50,31),
		(53,70,27),
		(150,52,48),
		(255,22,22)
	]

	mc.setBlocks(-W,0,0,W,H,0,0)

	for row in range(W):
		for col in range(H):
			pixel = img.getpixel((row,col))
			choice = None
			index_total = 1000
			index_choice = -1
			idx = 0
			for c in COLORS:
				val = (c[0]-pixel[0]) + (c[1]-pixel[1]) + (c[2]-pixel[2])
				# print abs(val)
				if abs(val)<index_total:
					index_total = abs(val)
					choice = c
					index_choice = idx
				idx = idx + 1
			
			# check for blue lapis
			special = False

			# check for red redstone!
			rv = abs((255-pixel[0]) + (0-pixel[1]) + (0-pixel[2]))
			if rv < index_total:
				print "should be redstone",row,col
				index_total = rv
				index_choice = 152 # redstone mfer!
				special = True


			bv = abs((0-pixel[0]) + (0-pixel[1]) + (255-pixel[2]))
			if bv <index_total:
				print "lapis", row, col
				index_total = bv
				index_choice = 22 # this is lapis
				special = True

			gv = abs((0-pixel[0]) + (255-pixel[1]) + (0-pixel[2]))
			if gv < index_total:
				print "leaves", row, col
				index_total = gv
				index_choice = 161 #acacia leaves greeeen
				special = True

				
			if special:
				mc.setBlock(row,-1*col-H, 0, index_choice)
			else:
				mc.setBlock(row,-1*col-H, 0, block.WOOL.id, index_choice)

indexed()
