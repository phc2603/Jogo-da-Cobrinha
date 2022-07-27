from turtle import Turtle


class Pontuacao(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.pont_atual = 0
        self.hideturtle()
        self.goto(0, 282)
        self.color("white")
        self.atualizando_pontuacao()

    def atualizando_pontuacao(self):
        self.write(f"Pontuação {self.pont_atual}", align="center", font=("Courier", 12, "normal"))

    def aumentando_pontuacao(self):
        self.clear()
        self.pont_atual += 1
        self.atualizando_pontuacao()

    def derrota(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Courier", 12, "normal"))

    def recorde_batido(self):
        self.goto(0, -80)
        self.write("Parabéns, você bateu o recorde da máquina!", align="center", font=("Courier", 12, "normal"))

    def recorde_nao_batido(self, maior_pnt):
        self.goto(0, -80)
        self.write(f"Maior pontuação da máquina: {maior_pnt}", align="center", font=("Courier", 12, "normal"))


