import mcpi.minecraft as minecraft
import mcpi.block as block

# mc = minecraft.Minecraft.create()

import Image

# mc.setBlocks(-W,0,0,W,H,0,0)

H = 128
W = 128

img = Image.open("Lenna128x128.png", "r")
for row in range(W):
	for col in range(H):
		(r,b,g) = img.getpixel((row,col))
		
		# now find a red, blue and green that match
		
		# mc.setBlock(row,-1*col-H, 0, block.WOOL.id, pixel)
