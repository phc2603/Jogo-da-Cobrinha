from turtle import Turtle


class Cobra:

    def __init__(self):
        self.lista_objetos = []
        self.criando_cobrinha()
        self.head = self.lista_objetos[0]

    def criando_cobrinha(self):
        posicao_inicial_aux = 0
        for i in range(0, 3):
            tart = Turtle()
            tart.shape("square")
            tart.color("white")
            tart.pensize(width=20)
            tart.penup()
            tart.speed("fastest")
            tart.setpos(posicao_inicial_aux, 0)
            posicao_inicial_aux -= 20
            self.lista_objetos.append(tart)

    def movimento(self):
        for obj_aux in range(len(self.lista_objetos)-1, 0, -1):
            cord_x = self.lista_objetos[obj_aux-1].xcor()
            cord_y = self.lista_objetos[obj_aux-1].ycor()
            self.lista_objetos[obj_aux].goto(cord_x, cord_y)
        self.head.forward(15)

    def cima(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def esquerda(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def direita(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def baixo(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def crescendo_tamanho(self):
        tart = Turtle()
        tart.shape("square")
        tart.color("white")
        tart.pensize(width=20)
        tart.penup()
        tart.speed("fastest")
        tart.goto(self.lista_objetos[-1].position())
        self.lista_objetos.append(tart)
