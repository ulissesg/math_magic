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

ALTURA = m.height - 60
LARGURA = m.width
SIZE = [LARGURA, ALTURA]

TIPO_FONTE = "comicsansms"
TAMANHO_FONTE = ALTURA // 40
# FONTE_PADRAO = pygame.font.Font(TIPO_FONTE, TAMANHO_FONTE)
COR_FONTE = "white"

COR_INPUT_BOX = Cor("light gray")

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

IMG_MOEDA = carregar_imagem("moeda.png")
IMG_MOEDA = definir_dimensoes(IMG_MOEDA, ALTURA // 14, ALTURA // 14)

RETANGULO = retangulo(LARGURA // 2, ALTURA // 2, Cor("black"))

INPUT_BOX = retangulo(LARGURA // 6, ALTURA // 18, COR_INPUT_BOX)

NOME_JOGO_BARRA = "MATH MAGIC"
IMG_ICONE = carregar_imagem("icone.png")

tela = criar_tela_base(LARGURA, ALTURA)
tela=pygame.display.set_mode(SIZE,RESIZABLE)
pygame.display.set_caption(NOME_JOGO_BARRA)
pygame.display.set_icon(IMG_ICONE)

root = tk.Tk()
root.withdraw()

Fases = definir_estrutura("Fases", "fundo, resultado, ajuda")

Jogo = definir_estrutura("Jogo", "Fases, moedas, Texto, inicio, fim, Fase, acertou, conf_acertou, conf_ajuda, ajuda, errou, conf_errou, nomoeda")

IMG_INICIO = carregar_imagem("inicio.png")
IMG_INICIO = definir_dimensoes(IMG_INICIO, LARGURA, ALTURA)
IMG_FIM = carregar_imagem("fim.png")
IMG_FIM = definir_dimensoes(IMG_FIM, LARGURA, ALTURA)

IMG_FASE_1= carregar_imagem("fase1.png")
IMG_FASE_1 = definir_dimensoes(IMG_FASE_1, LARGURA, ALTURA)
RESULTADO_FASE_1 = 6
AJUDA_FASE_1 = "6 x 5 = 30"

IMG_FASE_2= carregar_imagem("fase2.png")
IMG_FASE_2 = definir_dimensoes(IMG_FASE_2, LARGURA, ALTURA)
RESULTADO_FASE_2 = 11
AJUDA_FASE_2 = "É o mesmo que 6 + 5"

IMG_FASE_3= carregar_imagem("fase3.png")
IMG_FASE_3 = definir_dimensoes(IMG_FASE_3, LARGURA, ALTURA)
RESULTADO_FASE_3 = 64
AJUDA_FASE_3 = "É o mesmo que 8 x 8"

IMG_FASE_4= carregar_imagem("fase4.png")
IMG_FASE_4 = definir_dimensoes(IMG_FASE_4, LARGURA, ALTURA)
RESULTADO_FASE_4 = 1650
AJUDA_FASE_4 = "É o mesmo que 25 x 66"

IMG_FASE_5= carregar_imagem("fase5.png")
IMG_FASE_5 = definir_dimensoes(IMG_FASE_5, LARGURA, ALTURA)
RESULTADO_FASE_5 = 27
AJUDA_FASE_5 = "Texto de ajuda da fase 5"

IMG_INTERFACE= carregar_imagem("Interface.png")
IMG_INTERFACE = definir_dimensoes(IMG_INTERFACE, LARGURA, ALTURA)

FASE_1 = Fases(IMG_FASE_1, RESULTADO_FASE_1, AJUDA_FASE_1)
FASE_2 = Fases(IMG_FASE_2, RESULTADO_FASE_2, AJUDA_FASE_2)
FASE_3 = Fases(IMG_FASE_3, RESULTADO_FASE_3, AJUDA_FASE_3)
FASE_4 = Fases(IMG_FASE_4, RESULTADO_FASE_4, AJUDA_FASE_4)
FASE_5 = Fases(IMG_FASE_5, RESULTADO_FASE_5, AJUDA_FASE_5)

FASES_JOGO = [FASE_1, FASE_2, FASE_3, FASE_4, FASE_5]

JOGO_INICIAL = Jogo(FASES_JOGO[0], 0, "", False, False, 0, False, False, False, False, False, False, False)

def desenha_texto (t):
    if (t.inicio and not t.fim):
        colocar_imagem(t.Fases.fundo, tela, LARGURA //2, ALTURA //2)
        colocar_imagem(IMG_INTERFACE, tela, LARGURA // 2, ALTURA // 2)
        colocar_imagem(INPUT_BOX, tela, LARGURA * 0.845, ALTURA // 1.45 )
        colocar_imagem(IMG_MOEDA, tela, LARGURA * 0.815, ALTURA // 10)

        img_texto = texto(str(t.moedas), Fonte(TIPO_FONTE, ALTURA // 18), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.86, ALTURA // 10)

        img_texto = texto(str(t.Texto), Fonte(TIPO_FONTE, ALTURA // 19), Cor("black"))
        colocar_imagem(img_texto, tela, LARGURA * 0.845, ALTURA // 1.45)

        img_texto = texto("Digite o resultado no campo abaixo", Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.845, ALTURA // 1.6)

        img_texto = texto("Pressione Enter para verificar o resultado", Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.845, ALTURA // 1.3)

        img_texto = texto("Pressione H para solicitar ajuda", Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE))
        colocar_imagem(img_texto, tela, LARGURA * 0.845, ALTURA // 1.18)
        if (t.acertou):
            colocar_imagem(RETANGULO, tela, LARGURA // 2, ALTURA // 2)

            img_texto = texto("Parabéns, você acertou !", Fonte(TIPO_FONTE, ALTURA //22), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA //2, ALTURA // 2.1)

            img_texto = texto("Pressione Enter para continuar", Fonte(TIPO_FONTE, ALTURA // 30), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 1.8)

        if (t.errou):
            colocar_imagem(RETANGULO, tela, LARGURA // 2, ALTURA // 2)

            img_texto = texto("Você errou, mas não desanime, você pode tentar denovo, ou pedir ajuda !", Fonte(TIPO_FONTE, ALTURA // 22), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 2.2)

            img_texto = texto("Pressione Enter para continuar", Fonte(TIPO_FONTE, ALTURA // 30 ), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 1.6)

        if(t.conf_ajuda):
            colocar_imagem(RETANGULO, tela, LARGURA // 2, ALTURA // 2)

            img_texto = texto("Você realmente quer ajuda ?, isso lhe custará uma moeda !",
                              Fonte(TIPO_FONTE, ALTURA // 22), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 2.2)

            img_texto = texto("Pressione Y para continuar e N para voltar ao jogo", Fonte(TIPO_FONTE, ALTURA // 30), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 1.6)

        if(t.ajuda):
            colocar_imagem(RETANGULO, tela, LARGURA // 2, ALTURA // 2)

            img_texto = texto(t.Fases.ajuda,
                              Fonte(TIPO_FONTE, ALTURA // 22), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 2.1)

            img_texto = texto("Pressione Enter para continuar", Fonte(TIPO_FONTE, ALTURA // 30),
                              Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 1.8)
        if(t.nomoeda):
            colocar_imagem(RETANGULO, tela, LARGURA // 2, ALTURA // 2)

            img_texto = texto("Você não tem moedas suficiente !",
                              Fonte(TIPO_FONTE, ALTURA // 22), Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 2.2)

            img_texto = texto("Pressione Enter para continuar", Fonte(TIPO_FONTE, ALTURA // 30),
                              Cor(COR_FONTE), LARGURA // 2.5)
            colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 1.6)

    elif(not t.inicio and not t.fim):
        colocar_imagem(IMG_INICIO, tela, LARGURA // 2, ALTURA // 2)
        img_texto = texto("Pressione Enter para inicar o jogo", Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE))

        colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA * 0.8)
        img_texto = texto("Desenvolvido por Ulisses Genguini e Marcos Eduardo Plank", Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE), LARGURA // 4.5)

        colocar_imagem(img_texto, tela, LARGURA *0.83, ALTURA * 0.9)

    elif(t.fim and t.conf_acertou):
        colocar_imagem(IMG_FIM, tela, LARGURA // 2, ALTURA // 2)
        img_texto = texto("Prabéns você terminou o jogo", Fonte(TIPO_FONTE, ALTURA // 15), Cor(COR_FONTE), LARGURA //2)

        colocar_imagem(img_texto, tela, LARGURA // 2, ALTURA // 2)
        img_texto = texto("Desenvolvido por Ulisses Genguini e Marcos Eduardo Plank", Fonte(TIPO_FONTE, ALTURA // 45),Cor(COR_FONTE), LARGURA // 4.5)

        colocar_imagem(img_texto, tela, LARGURA * 0.83, ALTURA * 0.9)

'''
trata_tecla: Texto, tecla -> Texto
recebe um Texto e uma tecla do teclado(numero) e devolve um Texto
'''
def trata_tecla_texto(t, tecla):
    print(tecla)
    if (t.inicio and not t.fim):

        if (t.conf_ajuda and tecla == 121 or tecla == 89):
            if (t.moedas > 0):
                return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou, False,
                        True, t.errou, t.conf_errou, t.nomoeda)
            else:
                return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou, False,
                        t.ajuda, t.errou, t.conf_errou, True)


        if (t.conf_ajuda and tecla == 78 or tecla == 110):
            return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou, False,
                        t.ajuda, t.errou, t.conf_errou, t.nomoeda)

        if (tecla == pg.K_BACKSPACE):
            if (t.Texto == ''):
                return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)
            return Jogo(t.Fases, t.moedas, t.Texto[:-1], t.inicio, t.fim, t.Fase, t.acertou,t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)

        if tecla == 13 or tecla == 271:
            if (t.acertou):
                return Jogo(FASES_JOGO[t.Fase + 1], t.moedas.__add__(1), "", t.inicio, t.fim, t.Fase + 1, False,
                            True, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)

            if (t.errou):
                return Jogo(t.Fases, t.moedas, "", t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou,
                            t.conf_ajuda,
                            t.ajuda, False, True, t.nomoeda)

            if (t.ajuda):
                return Jogo(t.Fases, t.moedas - 1, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou,
                            t.conf_ajuda,
                            False, t.errou, t.conf_errou, t.nomoeda)

            if (t.nomoeda):
                return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou,
                            t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, False)

            if (t.Texto == str(t.Fases.resultado)):
                if (t.Fase <= 3):
                    return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim,t.Fase, True, t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)
                elif(t.Fase == 4):
                    return Jogo(t.Fases,t.moedas, t.Texto, t.inicio, True,t.Fase, True,t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)
            return Jogo(t.Fases,t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou,t.conf_acertou, t.conf_ajuda, t.ajuda, True, t.conf_errou, t.nomoeda)

        if tecla == 104 or tecla == 72:
            return Jogo(t.Fases, t.moedas, t.Texto, t.inicio, t.fim, t.Fase, t.acertou, t.conf_acertou, True, t.ajuda, t.errou, t.conf_errou, t.nomoeda)

        elif tecla >= 48 and tecla <= 57:
            if str.__len__(t.Texto) < int(LARGURA // 130):
                return Jogo(t.Fases, t.moedas, t.Texto+chr(tecla), t.inicio, t.fim, t.Fase, t.acertou,t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)
            return t

        elif  tecla >= 256 and tecla <= 265 :
            if str.__len__(t.Texto) < int(LARGURA // 130):
                return Jogo(t.Fases, t.moedas, t.Texto+chr(tecla - 208), t.inicio, t.fim, t.Fase, t.acertou,t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)
            return t
        elif tecla == 46 or tecla == 266:
            if str.__len__(t.Texto) < int(LARGURA // 130):
                return Jogo(t.Fases, t.moedas, t.Texto+".", t.inicio, t.fim, t.Fase, t.acertou,t.conf_acertou, t.conf_ajuda, t.ajuda, t.errou, t.conf_errou, t.nomoeda)
            return t

        else:
            return t

    elif tecla == 13 or tecla == 271:
        return Jogo(t.Fases, t.moedas, t.Texto, True, t.fim, t.Fase, t.acertou,t.conf_acertou, t.conf_ajuda, t.ajuda, 
                    t.errou, t.conf_errou, t.nomoeda)
    return t

def main(t):

    big_bang(t,tela=tela,
             desenhar= desenha_texto,
             frequencia=30,
             quando_tecla=trata_tecla_texto)

main(JOGO_INICIAL)
