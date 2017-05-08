import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint
pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32) #configurações tela

#adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
background_filename = 'pistadanca2.jpg'
background = pygame.image.load(background_filename).convert()

#adicionando a nave
#foi usado o método alpha pq ela tem partes transparentes
lista_img = ['flechad.jpg','flechae.jpg','flechab.jpg','flechac.jpg']

posicao_y = 460 
posicao_x = 0 
flecha0_position = [0,posicao_y] #posição inicial
flecha1_position = [0-200,posicao_y]
flecha2_position = [0-400,posicao_y]
flecha3_position = [0-600,posicao_y]
flecha4_position = [0-800,posicao_y]
flecha5_position = [0-1000,posicao_y]
i = randint(0,3)
n = randint(0,3)
a = randint(0,3)
b  = randint(0,3)
c = randint(0,3)
d = randint(0,3)
pygame.display.set_caption('Tumbalatum Dance')

clock = pygame.time.Clock()
#loop para atualizar 
while True:
    img0_filename = lista_img[n]
    img1_filename = lista_img[i]
    img2_filename = lista_img[a]
    img3_filename = lista_img[b]
    img4_filename = lista_img[c]
    img5_filename = lista_img[d]
    flecha0 = pygame.image.load(img0_filename).convert_alpha()
    flecha1 = pygame.image.load(img1_filename).convert_alpha()
    flecha2 = pygame.image.load(img2_filename).convert_alpha()
    flecha3 = pygame.image.load(img3_filename).convert_alpha()
    flecha4 = pygame.image.load(img4_filename).convert_alpha()
    flecha5 = pygame.image.load(img5_filename).convert_alpha()

    speed = 10
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    flecha0_position[0] += speed #mudando a posição com o tempo(horizontal)
    flecha1_position[0] += speed
    flecha2_position[0] += speed
    flecha3_position[0] += speed
    flecha4_position[0] += speed
    flecha5_position[0] += speed
    screen.blit(flecha0, flecha0_position) #precisa disso pra nave ficar sobre a tela de fundo e posicionamento
    screen.blit(flecha1, flecha1_position)
    screen.blit(flecha2, flecha2_position)
    screen.blit(flecha3, flecha3_position)
    screen.blit(flecha4, flecha4_position)
    screen.blit(flecha5, flecha5_position)
    pygame.display.update()
    time_passed = clock.tick(30)
    if flecha0_position[0] >= 2000:
        i = randint(0,3)
        n = randint(0,3)
        a = randint(0,3)
        b  = randint(0,3)
        c = randint(0,3)
        d = randint(0,3)
        flecha0_position[0] = 0
        flecha1_position[0] = -200
        flecha2_position[0] = -400
        flecha3_position[0] = -600
        flecha4_position[0] = -800
        flecha5_position[0] = -1000