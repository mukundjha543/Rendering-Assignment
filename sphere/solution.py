import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *  # Ensure GLUT is imported
import random

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (10, 10, 10, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1, 1, 1, 1))
    glMaterialf(GL_FRONT, GL_SHININESS, 50)

def setup_scene():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1)
    setup_lighting()

def draw_sphere(x, y, z, color):
    glPushMatrix()
    glTranslate(x, y, z)
    glColor3fv(color)
    glutSolidSphere(0.5, 32, 32)  # Now correctly referenced
    glPopMatrix()

def draw_grid():
    start_x, start_y = -5, -5
    spacing = 2.0
    for i in range(6):
        for j in range(6):
            x = start_x + i * spacing
            y = start_y + j * spacing
            draw_sphere(x, y, 0, sphere_color)

def main():
    global sphere_color
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

    setup_scene()

    sphere_color = [1.0, 0.0, 0.0] # Initial color of the spheres

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Change sphere color to a random color on mouse click
                sphere_color = [random.random() for _ in range(3)]

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_grid()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
