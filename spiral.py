import turtle
a=10
for i in xrange(20):
	a=a+i
	turtle.color('red')
	turtle.forward(a)
	turtle.color('green')
	turtle.right(98)
	turtle.forward(a)
	turtle.color('blue')
	turtle.right(98)
	a=a+i
	turtle.forward(a)
	turtle.color('pink')
	turtle.right(98)
	turtle.forward(a)
	turtle.right(98)
turtle.wait()
