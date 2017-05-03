import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint
pygame.init()

screen = pygame.display.set_mode((956, 560), 0, 32) #configurações tela

#adicionando imagem de fundo e mudando a configuração 956,560 tamanho img
background_filename = 'bg_big.png'
background = pygame.image.load(background_filename).convert()

#adicionando a nave
#foi usado o método alpha pq ela tem partes transparentes
lista_img = ['flechad.jpg','flechae.jpg','flechab.jpg','flechac.jpg']

flecha_position = [0,280] #posição inicial
flecha1_position = [-1000,280]
i = randint(0,3)
n = randint(0,3)
pygame.display.set_caption('Hello World')

clock = pygame.time.Clock()
#loop para atualizar 
while True:
    
    img1_filename = lista_img[i]
    img_filename = lista_img[n]
    flecha1 = pygame.image.load(img1_filename).convert_alpha()
    flecha = pygame.image.load(img_filename).convert_alpha()
    speed = 10
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0,0))
    flecha_position[0] += speed #mudando a posição com o tempo(horizontal)
    flecha1_position[0] += speed
    screen.blit(flecha, flecha_position) #precisa disso pra nave ficar sobre a tela de fundo e posicionamento
    screen.blit(flecha1, flecha1_position)
    pygame.display.update()
    time_passed = clock.tick(30) 
