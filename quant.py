
# see here 
# http://stackoverflow.com/questions/236692/how-do-i-convert-any-image-to-a-4-color-paletted-image-using-the-python-imaging

import Image
filename = "Lenna512x512.png"

img = Image.open(filename, "r")

# try simple quantize first
img2 = img.quantize(16)
img2.save("lenna_16colors.png")

# minecraft color list
color_list = [
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
    (25,22,22)
    ]
mci = Image.new("P", (1,1))
# mci.putpalette(color_list)
mci.putpalette( (221,221,221,
219,125,62,
179,80,188,
107,138,201,
177,166,39,
65,174,56,
208,132,153,
64,64,64,
154,161,161,
46,110,137,
126,61,181,
46,56,141,
79,50,31,
53,70,27,
150,52,48,
25,22,22) + (0,0,0)*(256-16))

# quantize with our palette
# this should be the best really
img3 = img.quantize(palette = mci)
img3.save("lenna_16colors_mci.png")

# try adaptive
img4 = img.convert("P", palette=Image.ADAPTIVE, colors=16)
img4.save("lenna_16adaptive.png")
