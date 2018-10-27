from PIL import Image
from collections import Counter

im = Image.open("image.jpg")
width, height = im.size
x = 0
y = 0
pic = im.load()

R = []
G = []
B = []

while (x < width - 1):
	x += 1
	r, g, b = im.getpixel((x, y))
	R.append(r)
	G.append(g)
	B.append(b)

while (y < height - 1):
	y += 1
	r, g, b = im.getpixel((x, y))
	R.append(r)
	G.append(g)
	B.append(b)

for contents in R,G,B:
        print ((contents),"\n")

length = len(R+G+B)
countR = Counter(R).most_common(5)
countG = Counter(G).most_common(5)
countB = Counter(B).most_common(5)

print ("Number of entries in list(s):",(length))
print ("Image dimensions:", (im.size))
print ("Most prominent colors in image:")
print ("        R:", countR)
print ("        G:", countG)
print ("        B:", countB,"\n")

#img = Image.new("RGB", (width, height), color = (R,G,B)
#img.save("image2.png")
