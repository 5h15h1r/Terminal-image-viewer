from PIL import Image
from colorit import init_colorit , background

init_colorit()

image=Image.open(input("enter the path of image:"))

h=input("enter ht")
w=input("enter wth")
image=image.resize((h,w))


for y in range (image.size[1]):
    
    for x in range(image.size[0]):
        
        print(background(" ", image.getpixel((x,y))),end="")
    
    print()
        