from PIL import Image, ImageDraw
from collections import Counter

path = input("Image to open?: ")

if (path == ""): #opens default image on empty input
	path = "image.jpg"

im = Image.open(path)
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

print ("Number of entries in lists:",(length))
print ("Image dimensions:", (im.size))
print ("Most prominent colors in image:")
print ("        R:", countR)
print ("        G:", countG)
print ("        B:", countB,"\n")

x = width/5

img = Image.new("RGB", (width, height))
rect = ImageDraw.Draw(img)
rect.rectangle(((0, 0), (x, height)), fill = (countR[0][0],countG[0][0],countB[0][0]))
rect.rectangle(((x, 0), (x*2, height)), fill = (countR[1][0],countG[1][0],countB[1][0]))
rect.rectangle(((x*2, 0), (x*3, height)), fill = (countR[2][0],countG[2][0],countB[2][0]))
rect.rectangle(((x*3, 0), (x*4, height)), fill = (countR[3][0],countG[3][0],countB[3][0]))
rect.rectangle(((x*4, 0), (x*5, height)), fill = (countR[4][0],countG[4][0],countB[4][0]))
img.save("palette.png")
