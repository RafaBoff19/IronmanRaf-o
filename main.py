import pygame
import random
import os
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Iron Man do Rafão")
branco = (255,255,255)
preto = (0, 0, 0)
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load ("assets/fundo.png")
missel = pygame.image.load ("assets/missile.png")
posicaoXPersona = 400
posicaoYPersona = 300
movimentoXPersona = 0
movimentoYPersona = 0
posicaoXmissel = 400
posicaoYmissel = -240
velocidadeYmissel = 1
missileSound = pygame.mixer.Sound("assets/missile.wav")
pygame.mixer.Sound.play(missileSound)
fonte = pygame.font.SysFont("comicsans", 14)
pygame.mixer.music.load("assets/ironsound.mp3")
pygame.mixer.music.play(1)
pontos = 0
larguraXPersona = 250
alturaPersona = 127
larguraMissel = 50
alturaMissel = 250
dificuldade = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            movimentoXPersona = -5 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
            movimentoXPersona = 0
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            movimentoYPersona = -5
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            movimentoYPersona = 5 
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            movimentoYPersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            movimentoYPersona = 0

    posicaoXPersona = posicaoXPersona + movimentoXPersona
    posicaoYPersona = posicaoYPersona + movimentoYPersona
    if posicaoXPersona < 0:
        posicaoXPersona = 10
    elif posicaoXPersona >570:
        posicaoXPersona = 565

    if posicaoYPersona < 0:
        posicaoYPersona = 10
    elif posicaoYPersona >473:
        posicaoYPersona = 465
    tela.fill(branco)
   # pygame.draw.circle(tela,preto, (posicaoXPersona,posicaoYPersona), 40,0 )
    tela.blit(fundo, (0,0))
    tela.blit(iron, (posicaoXPersona, posicaoYPersona))
    tela.blit(missel, (posicaoXmissel, posicaoYmissel))
    posicaoYmissel = posicaoYmissel + velocidadeYmissel
    if posicaoYmissel > 600:
        posicaoYmissel = -240
        pontos = pontos + 1
        velocidadeYmissel = velocidadeYmissel +1
        posicaoXmissel = random.randint (0, 800)
        pygame.mixer.Sound.play(missileSound)
    texto = fonte.render("Pontos: " +str(pontos), True, branco)
    tela.blit(texto,(10, 20))

    pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraXPersona))
    pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona + alturaPersona))
    pixelsMisselX = list(range(posicaoXmissel, posicaoXmissel + larguraMissel))
    pixelMisselY = list(range(posicaoYmissel, posicaoYmissel + alturaMissel))



    os.system ("cls")
    print ( len (list(set (pixelsMisselX).intersection(set(pixelsPersonaX)))))
    if len (list(set (pixelMisselY).intersection(set(pixelsPersonaY)))) > dificuldade:
        if len (list(set (pixelsMisselX).intersection(set(pixelsPersonaX)))) > dificuldade:
            print("Morreu")
        else:
            print(" ainda vivo mas por pouco")
    else:
        print ("vivo")
    pygame.display.update()
    relogio.tick(60)
