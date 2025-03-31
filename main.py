import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import wire_cube
import math


def main():
    pygame.init()
    # Configurações da janela
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
    glClearColor(0.4600, 0.6895, 0.5502, 1)
    pygame.display.set_caption("Cubo com Reflexo e Transformações")

    gluPerspective(45, (screen_width / screen_height), 0.1, 50.0)
    glTranslatef(0, 0, -10)

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    move_x = -2.0
    move_direction = 1
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Tempo para a escala pulsante e rotação
        t = (pygame.time.get_ticks() - start_ticks) / 1300.0
        pulsate = 1.0 + 0.5 * math.sin(t * math.pi * 2)
        angle = t * 50

        # Cubo Principal: Rotação, Translação e Escala
        glPushMatrix()
        move_x += 0.02 * move_direction
        if move_x > 2 or move_x < -2:
            move_direction *= -1
        glTranslatef(move_x, 0, 0)
        glRotatef(angle, 1, 1, 0)
        glScalef(pulsate, pulsate, pulsate)
        wire_cube()
        glPopMatrix()

        # Reflexo do Cubo: Inversão no Eixo X
        glPushMatrix()
        move_x += 0.02 * move_direction
        glTranslatef(move_x, -2.5, 0)  # Reflexo abaixo do cubo original
        glRotatef(angle, 1, 1, 0)
        glScalef(-pulsate, pulsate, pulsate)
        wire_cube()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
