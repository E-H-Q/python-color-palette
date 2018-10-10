from PIL import Image

im = Image.open("image.jpg")
width, height = im.size
x = width/2
y = height/2
pic = im.load()
print ("Image dimensions:", (im.size))
pic[x,y] = (255,0,0) #sets pixe color to solid red
print ("Pixel color at X & Y:", pic[x,y])
im.save("Image2.png")
