#!/usr/bin/env python3
from datetime import datetime
import turtle


def define_clock():
    clock = turtle.Turtle()
    clock.ht()
    # clock.speed(1)
    clock.penup()
    clock.setposition(0, 200)
    clock.pendown()
    # create circle with hr markers
    for hr in range(12):
        clock.penup()
        clock.circle(-200, 5)
        clock.pendown()
        clock.circle(-200, 20)
        clock.penup()
        clock.circle(-200, 5)
        clock.write(str(hr + 1), False, align="Center")
    clock.penup()
    clock.left(90)
    clock.forward(30)
    clock.write("Analog Clock", False, align="Center", font='Arial')


def hour_hand():
    hr = turtle.Turtle()
    hr.ht()
    hr.degrees(360)
    hr.penup()
    hr.left(90)
    hr.right((30 * datetime.now().hour) + (.5 * datetime.now().minute))
    hr.pensize(5)
    hr.pendown()
    hr.backward(15)
    hr.forward(115)


def minute_hand():
    min = turtle.Turtle()
    min.ht()
    min.pensize(3)
    min.degrees(360)
    min.left(90)
    min.right(6 * datetime.now().minute)
    min.backward(15)
    min.forward(195)

def second_hand():
    sec = turtle.Turtle()
    sec.color("red")
    sec.ht()
    sec.pensize(1)
    sec.degrees(360)
    sec.left(90)
    sec.right(6 * datetime.now().second)
    sec.backward(30)
    sec.forward(190)

def load_clock():
    my_screen = turtle.Screen()
    my_screen.delay(0)
    define_clock()
    hour_hand()
    minute_hand()
    second_hand()
    my_screen.screensize(5, 5)
    turtle.done()

if __name__ == '__main__':
    load_clock()
