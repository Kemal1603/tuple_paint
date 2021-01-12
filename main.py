import turtle
import random
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 6)
# for color in colors:
# 	r = color.rgb.r
# 	g = color.rgb.g
# 	b = color.rgb.b
# 	new_color = (r, g, b)
# 	rgb_colors.append(new_color)
# print(rgb_colors)
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
colors = [(255, 0, 0), (3, 0, 0), (253, 161, 187), (0, 66, 254), (0, 246, 0), (223, 217, 103)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots + 1):
	tim.dot(20, random.choice(colors))
	tim.forward(50)
	if dots % 10 == 0:
		tim.setheading(90)
		tim.forward(50)
		tim.setheading(180)
		tim.forward(500)
		tim.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
