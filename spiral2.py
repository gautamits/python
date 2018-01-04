import turtle
turtle.speed(1000)
for i in xrange(100):
	turtle.color('red')
	turtle.circle(i*2)
	turtle.left(30)
	turtle.color('green')
	turtle.circle(i*2)
turtle.done()
