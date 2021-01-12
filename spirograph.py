import turtle as t
import random
# Создаем объект по имени timmy_the_turtle класса Turtle() и обращаемся к классу, через объект
tim = t.Turtle()
tim.shape('turtle')
tim.color('black')
tim.pen(speed=10, pensize=7)
t.colormode(255)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3, 15):
#     draw_shape(shape_side_n)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.pencolor(random_color())
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
# Создаем объект screen класса Screen(). Если запустить скрипт сразу после создания объекта timmy_the_turtle, тогда
# На мониторе можно увидеть очень быстрое белое мерцание - это дополнительный интерфейс, который открывается и сразу
# закрывается, так как в открытом состоянии он может оставаться, если увидет метод .exitonclick(), Для этого здесь-
# ниже мы и обращаемся к методу .exitonclick() через объект screen класса  Screen()
screen = t.Screen()
screen.exitonclick()

