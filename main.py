import turtle as t
import random

t.colormode(255)
# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(244, 251, 249), (219, 232, 242), (196, 158, 135), (134, 171, 195), (160, 59, 113),
 (197, 142, 158), (20, 116, 161), (130, 29, 69), (218, 77, 108), (141, 188, 175), (84, 35, 58), (250, 223, 108),
 (30, 175, 204), (222, 65, 45), (23, 123, 83), (92, 147, 105), (59, 52, 142), (232, 168, 177), (189, 185, 208),
 (14, 54, 95), (232, 172, 171), (150, 93, 86), (158, 209, 201), (5, 115, 73), (149, 209, 220), (112, 110, 171),
 (67, 52, 52), (73, 59, 59)]

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()


