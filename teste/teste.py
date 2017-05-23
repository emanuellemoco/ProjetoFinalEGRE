import pygame
from pygame.locals import * #usando todas as funções do pygame
from sys import exit
from random import randint
import time


pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]