from PIL import Image

im = Image.open("image.jpg")
width, height = im.size
x = 0
y = 0
R = []
G = []
B = []
overflow = []
pic = im.load()
while (x < width - 1):
	x += 1
	r, g, b = im.getpixel((x, y))
	R.append(r)
	G.append(g)
	B.append(b)
	#[xy_list.append(pic[x,y]) for v in overflow if v not in xy_list]
while (y < height - 1):
	y += 1
	r, g, b = im.getpixel((x, y))
	R.append(r)
	G.append(g)
	B.append(b)
	#xy_list.append(pic[x,y])
for contents in R,G,B:
	print ((contents),"\n")
length = len(R+G+B)
print ("Number of entries in list(s):",(length))
print ("Coords stopped at:",x,",",y)
print ("Image dimensions:", (im.size))
#print ("Pixel color at X & Y:", pic[x,y])
#pic[x,y] = (255,0,0)
#im.save("image2.png")
