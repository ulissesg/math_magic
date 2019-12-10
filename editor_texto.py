import os
import pygame
import tkinter as tk
from pygame.locals import *
from tkinter import messagebox
from htdp_pt_br.universe import *
from screeninfo import get_monitors

#declaracao de variaveis

for m in get_monitors():
    print(m)

ALTURA = m.height - 30
LARGURA = m.width

SIZE = [LARGURA, ALTURA]

TIPO_FONTE = "comicsansms"
TAMANHO_FONTE = ALTURA // 35
COR_FONTE = "dark gray"

COR_INPUT_BOX = Cor("light gray")

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

IMG_MOEDA = carregar_imagem("imagens/moeda.png")
IMG_MOEDA = definir_dimensoes(IMG_MOEDA, ALTURA // 14, ALTURA // 14)

RETANGULO_LADO = retangulo(LARGURA // 3, ALTURA, COR_BRANCO)

INPUT_BOX = retangulo(LARGURA // 8, ALTURA // 25, COR_INPUT_BOX)

NOME_JOGO_BARRA = "MATH MAGIC"
IMG_ICONE = carregar_imagem("imagens/icone.png")

tela = criar_tela_base(LARGURA, ALTURA)
tela=pygame.display.set_mode(SIZE,RESIZABLE)
pygame.display.set_caption(NOME_JOGO_BARRA)
pygame.display.set_icon(IMG_ICONE)

root = tk.Tk()
root.withdraw()

Fases = definir_estrutura("Fases", "fundo, resultado, ajuda")

Jogo = definir_estrutura("Jogo", "Fases, moedas, Texto, inicio, fim, Fase")

IMG_INICIO = carregar_imagem("imagens/inicio.png")
IMG_FIM = carregar_imagem("imagens/fim.png")

IMG_FASE_1= carregar_imagem("imagens/fase1.png")
RESULTADO_FASE_1 = 2
AJUDA_FASE_1 = "Texto de ajuda da fase 1"

IMG_FASE_2= carregar_imagem("imagens/fase2.png")
RESULTADO_FASE_2 = 8
AJUDA_FASE_2 = "Texto de ajuda da fase 2"

IMG_FASE_3= carregar_imagem("imagens/fase3.png")
RESULTADO_FASE_3 = 14
AJUDA_FASE_3 = "Texto de ajuda da fase 3"

IMG_FASE_4= carregar_imagem("imagens/fase4.png")
RESULTADO_FASE_4 = 16
AJUDA_FASE_4 = "Texto de ajuda da fase 4"

IMG_FASE_5= carregar_imagem("imagens/fase5.png")
RESULTADO_FASE_5 = 27
AJUDA_FASE_5 = "Texto de ajuda da fase 5"

FASE_1 = Fases(IMG_FASE_1, RESULTADO_FASE_1, AJUDA_FASE_1)
FASE_2 = Fases(IMG_FASE_2, RESULTADO_FASE_2, AJUDA_FASE_2)
FASE_3 = Fases(IMG_FASE_3, RESULTADO_FASE_3, AJUDA_FASE_3)
FASE_4 = Fases(IMG_FASE_4, RESULTADO_FASE_4, AJUDA_FASE_4)
FASE_5 = Fases(IMG_FASE_5, RESULTADO_FASE_5, AJUDA_FASE_5)

FASES_JOGO = [FASE_1, FASE_2, FASE_3, FASE_4, FASE_5]

JOGO_INICIAL = Jogo(FASES_JOGO[0], 0, "", False, False, 0)

def desenha_texto (t):
    if (t.inicio and not t.fim):
        colocar_imagem(t.Fases.fundo, tela, LARGURA //2, ALTURA //2)
        colocar_imagem(RETANGULO_LADO, tela, LARGURA // 1.2, ALTURA //2)
        colocar_imagem(INPUT_BOX, tela, LARGURA * 0.833333333333, ALTURA // 1.5 )
        colocar_imagem(IMG_MOEDA, tela, LARGURA * 0.815, ALTURA // 10)
        img_texto = texto(str(t.moedas), Fonte(TIPO_FONTE, ALTURA // 18), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.86, ALTURA // 10)
        img_texto = texto(str(t.Texto), Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.833333333333, ALTURA // 1.5)
        img_texto = texto("Pressione Enter para verificar o resultado", Fonte(TIPO_FONTE, ALTURA // 39), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.833333333333, ALTURA // 1.4)
        img_texto = texto("Pressione H para solicitar ajuda", Fonte(TIPO_FONTE, ALTURA // 39), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.833333333333, ALTURA // 1.25)
    elif(not t.inicio and not t.fim):
        colocar_imagem(IMG_INICIO, tela, LARGURA // 2, ALTURA // 2)
        img_texto = texto("Pressione Enter para inicar o jogo", Fonte(TIPO_FONTE, ALTURA // 30), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA * 0.8)
    elif(t.fim):
        colocar_imagem(IMG_FIM, tela, LARGURA // 2, ALTURA // 2)
        img_texto = texto("Prabéns você terminou o jogo", Fonte(TIPO_FONTE, ALTURA // 15), Cor(COR_FONTE), LARGURA //2)
        colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 2)

'''
trata_tecla: Texto, tecla -> Texto
recebe um Texto e uma tecla do teclado(numero) e devolve um Texto
'''
def trata_tecla_texto(t, tecla):
    if (t.inicio and not t.fim):
        if (tecla == pg.K_BACKSPACE):
            if (t.Texto == ''):
                return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase)
            return Jogo(t.Fases, t.moedas, t.Texto[:-1], t.inicio, t.fim, t.Fase)

        if tecla == 13 or tecla == 271:
            if (t.Texto == str(t.Fases.resultado)):
                messagebox.showinfo("Resultado", "Parabéns você acertou !")
                if (t.Fase <= 3):
                    return Jogo(FASES_JOGO[t.Fase + 1], t.moedas.__add__(1), "", t.inicio, t.fim,t.Fase +1)
                elif(t.Fase == 4):
                    return Jogo(t.Fases,t.moedas, "", t.inicio, True,t.Fase)
            messagebox.showinfo("Resultado", "Você errou, mas nao desanime, você pode tentar novamente, ou pedir ajuda !")
            return Jogo(t.Fases,t.moedas, "", t.inicio, t.fim, t.Fase)

        if tecla == 104:
            resposta = messagebox.askquestion("Ajuda","Você realmente deseja continuar, isso irá lhe custar uma moeda !")
            if (resposta == "yes" and t.moedas > 0):
                messagebox.showinfo("Ajuda", t.Fases.ajuda)
                return Jogo(t.Fases, t.moedas - 1, t.Texto, t.inicio, t.fim, t.Fase)
            elif (resposta == "yes" and t.moedas == 0):
                messagebox.showinfo("Ajuda", "Você não tem moedas suficiente !")
            return t

        elif tecla >= 48 and tecla <= 57:
            if str.__len__(t.Texto) < int(LARGURA // 84):
                return Jogo(t.Fases, t.moedas, t.Texto+chr(tecla), t.inicio, t.fim, t.Fase)
            return t
        elif  tecla >= 256 and tecla <= 265 :
            if str.__len__(t.Texto) < int(LARGURA // 84):
                return Jogo(t.Fases, t.moedas, t.Texto+chr(tecla - 208), t.inicio, t.fim, t.Fase)
            return t
        elif tecla == 46 or tecla == 266:
            if str.__len__(t.Texto) < int(LARGURA // 84):
                return Jogo(t.Fases, t.moedas, t.Texto+".", t.inicio, t.fim, t.Fase)
            return t

        else:
            return t
    elif  tecla == 13 or tecla == 271:
        return Jogo(t.Fases, t.moedas, t.Texto, True, t.fim, t.Fase)
    return t

def main(t):

    big_bang(t,tela=tela,
             desenhar= desenha_texto,
             frequencia=30,
             quando_tecla=trata_tecla_texto,
             modo_debug= True)

main(JOGO_INICIAL)
