import turtle
import math
block_size=40.0
line_size=10
def draw(a):
	print a
	if a=='A' or a=='a':
		width=(block_size-1.5*line_size)+block_size
		turtle.forward(width)
		turtle.right(math.atan(block_size/width)*180/3.14)
		turtle.forward(math.sqrt(block_size**2+width**2))
		turtle.right(math.atan(block_size/width)*180/3.14)
		turtle.forward(math.sqrt(line_size**2+(line_size/2)**2))
		turtle.left(180-math.atan(block_size/width)*180/3.14)
		turtle.forward(width)
		turtle.left(180-math.atan(block_size/width)*180/3.14)
		turtle.forward(math.sqrt(line_size**2+(line_size/2)**2))
		turtle.right(180+math.atan(block_size/width)*180/3.14)
		turtle.forward(line_size)
		turtle.right(180+math.atan(block_size/width)*180/3.14)
		turtle.wait()


name=raw_input("input your name ").split()

for titles in name:
	for character in titles:
		draw(character)
	draw('space')
