from turtle import Turtle
import random


class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.nova_coordenada()

    def nova_coordenada(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))