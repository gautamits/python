import turtle
pen=turtle.Pen()
j=10
angle=70
pen.speed(100)
for i in range(100):
	pen.color("red")
	pen.forward(j)
	pen.right(angle)
	pen.color("green")
	pen.forward(j)
	pen.right(angle)
	j=j+1
	pen.color("yellow")
	pen.forward(j)
	pen.right(angle)
	pen.color("blue")
	pen.forward(j)
	pen.right(angle)
	j=j+1
raw_input()
