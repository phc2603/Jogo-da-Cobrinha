from turtle import Screen
from cobra import Cobra
from comida import Comida
from pontuacao import Pontuacao
import time
tela = Screen()
tela.tracer(0)


def configuracoes_iniciais_tela():
    tela.setup(width=600, height=600)
    tela.bgcolor("black")
    tela.title("Jogo da Cobrinha")


def maior_pontuacao(pnt):
    arquivo = open("maior_pontuacao.txt", "r")
    for linha in arquivo.readline():
        if pnt > int(linha):
            pontuacao.recorde_batido()
            atualizacao_arquivo = open("maior_pontuacao.txt", "w")
            x = str(pnt)
            atualizacao_arquivo.write(x)
            atualizacao_arquivo.close()
        else:
            pontuacao.recorde_nao_batido(int(linha))
    arquivo.close()


configuracoes_iniciais_tela()
cobra = Cobra()
comida = Comida()
pontuacao = Pontuacao()
jogando = True


def movimentacao_usuario():
    tela.listen()
    tela.onkey(cobra.cima, "Up")
    tela.onkey(cobra.direita, "Right")
    tela.onkey(cobra.baixo, "Down")
    tela.onkey(cobra.esquerda, "Left")


while jogando:
    tela.update()
    time.sleep(0.1)
    '#atualizando a posição da cobrinha'
    movimentacao_usuario()
    cobra.movimento()
    '#verificando se comeu a bolinha'
    if cobra.head.distance(comida) <= 14:
        comida.nova_coordenada()
        pontuacao.aumentando_pontuacao()
        cobra.crescendo_tamanho()
    '#verificando se a cobra atingiu alguma extremidade e se caso tenha atingido, mudando a posição de extremidade'
    if cobra.head.xcor() > 285:
        cobra.lista_objetos[0].setpos(-285, cobra.head.ycor())
    elif cobra.head.xcor() < -285:
        cobra.lista_objetos[0].setpos(285, cobra.head.ycor())
    elif cobra.head.ycor() < -285:
        cobra.lista_objetos[0].setpos(cobra.head.xcor(), 285)
    elif cobra.head.ycor() > 285:
        cobra.lista_objetos[0].setpos(cobra.head.xcor(), -285)

    '#vefificando se a cobra atingiu o seu próprio corpo'
    for i in cobra.lista_objetos[1:]:
        if cobra.head.distance(i) < 10:
            pontuacao.derrota()
            jogando = False
            maior_pontuacao(pontuacao.pont_atual)

tela.exitonclick()
