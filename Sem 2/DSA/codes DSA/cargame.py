import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *  # Import GLUT
import random

# Initialize pygame and GLUT
pygame.init()
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Rolling Ball Game")

gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, -1.5, -10)
glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering

# Game variables
ball_x, ball_y, ball_z = 0, 0, 0
velocity = 0.1
acceleration = 0.001
score = 0
lives = 3
move_left = move_right = False
obstacles = []

# Generate initial obstacles
def generate_obstacles():
    global obstacles
    obstacles = []
    for i in range(-5, 5):
        obstacles.append([random.choice([-1, 0, 1]), -0.3, i * -6])

generate_obstacles()

def draw_ball(x, y, z):
    glColor3f(1, 0, 0)  # Red ball
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluSphere(quadric, 0.3, 20, 20)
    glPopMatrix()

def draw_track(z_offset):
    glColor3f(0.2, 0.2, 0.2)  # Dark gray track
    glBegin(GL_QUADS)
    glVertex3f(-2, -0.6, 5 + z_offset)
    glVertex3f(2, -0.6, 5 + z_offset)
    glVertex3f(2, -0.6, -50 + z_offset)
    glVertex3f(-2, -0.6, -50 + z_offset)
    glEnd()

def draw_obstacles():
    glColor3f(1, 1, 0)  # Yellow obstacles
    for obs in obstacles:
        glPushMatrix()
        glTranslatef(obs[0], obs[1], obs[2])
        glBegin(GL_QUADS)
        glVertex3f(-0.5, -0.5, 0.5)
        glVertex3f(0.5, -0.5, 0.5)
        glVertex3f(0.5, 0.5, 0.5)
        glVertex3f(-0.5, 0.5, 0.5)
        glEnd()
        glPopMatrix()

def draw_buildings():
    glColor3f(0.5, 0.5, 0.5)  # Gray buildings
    for i in range(-10, 10, 3):
        glPushMatrix()
        glTranslatef(-3, 0, i * -5)
        glScalef(1, 3, 1)
        glutSolidCube(1)
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(3, 0, i * -5)
        glScalef(1, 3, 1)
        glutSolidCube(1)
        glPopMatrix()

def check_collision():
    global lives, obstacles
    for obs in obstacles:
        if abs(ball_x - obs[0]) < 0.5 and abs(ball_z - obs[2]) < 0.5:
            lives -= 1
            obstacles.remove(obs)
            if lives == 0:
                print("Game Over!")
                pygame.quit()
                quit()

def game_loop():
    global ball_x, ball_z, velocity, score, move_left, move_right, obstacles
    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_track(ball_z)
        draw_buildings()
        draw_obstacles()
        draw_ball(ball_x, ball_y, ball_z)
        
        ball_z -= velocity
        velocity += acceleration
        score += 1
        
        if move_left and ball_x > -1.5:
            ball_x -= 0.05
        if move_right and ball_x < 1.5:
            ball_x += 0.05
        
        check_collision()
        
        pygame.display.flip()
        pygame.time.wait(10)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    move_left = True
                elif event.key == K_RIGHT:
                    move_right = True
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    move_left = False
                elif event.key == K_RIGHT:
                    move_right = False
    
    pygame.quit()

game_loop()