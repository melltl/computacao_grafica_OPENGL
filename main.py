import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import wireCube

pygame.init()

# Configurações da tela
screen_width = 1000
screen_height = 800
background_color = (0.5, 0.6, 0.3, 1)
drawing_color = (0, 0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL - Transformações Fixas')

def initialise():
    glClearColor(*background_color)
    glColor(*drawing_color)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Aplicando transformações fixas:

    # 1. Translação:
    glTranslatef(0.5, 0.5, -10)

    # 2. Espelhamento
    glScalef(-1, 1, 1)

    # 3. Escala
    glScalef(2.5, 2.5, 2.5)
    
    wireCube()

initialise()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
