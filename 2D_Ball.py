import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(1000,800)
wn.title("Bouncing with Physics")
wn.tracer(0)
wn.listen()

balls = []

for _ in range(10):
	balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "orange", "green", "white", "purple", "pink", "brown", "grey"]
shapes = ["circle"]

for ball in balls:
	ball.shape(random.choice(shapes))
	ball.color(random.choice(colors))
	ball.penup()
	ball.speed(0)
	x = random.randint(-290,290)
	y = random.randint(200, 400)
	ball.goto(x,y)
	ball.dy = 0
	ball.dx = random.randint(-3,3)
	ball.da = random.randint(-5,5)

gravity = 2.4
friction_air = 0.05
friction_ground = 0.05
while True:
	wn.update()

	for ball in balls:
		ball.rt(ball.da)
		
		ball.dy -= gravity
		ball.dy -= (ball.dy*friction_air)
		ball.sety(ball.ycor() + ball.dy)
		ball.setx(ball.xcor() + ball.dx)
		time.sleep(0.001)
		# Duvar carpismalari.
		if ball.xcor() > 300:
			ball.dx *= -1
			ball.da *= -1

		# Zıplama kontrolu.
		if ball.xcor() < -300:
			ball.dx *= -1
			ball.da *= -1

		if ball.ycor() < -300:
			ball.sety(-300)
			ball.dy *= -1
			ball.da *= -1

		if ball.ycor() == -300:
			ball.dx -= (ball.dx*friction_ground)
			ball.setx(ball.xcor() + ball.dx)


	# Toplar arasi carpismalar.
	for i in range(0, len(balls)):
		for j in range(i+1, len(balls)):
			# Carpisma Kontrolu.
			if balls[i].distance(balls[j]) < 20:
				balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
				balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy