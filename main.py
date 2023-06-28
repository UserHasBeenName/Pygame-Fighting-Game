import pygame
import sys
from pygame import *

pygame.init()
vector = pygame.math.Vector2
clock = pygame.time.Clock()

# Game Variables
ACC = 0.5
FRICTION = -0.12
FPS = 60

WIDTH = 700
HEIGHT = 400
GROUND = HEIGHT - 67

class Player():
    def __init__(self, location, facing_right, colour, controls):
        super().__init__()
        self.location = location
        self.facing_right = facing_right
        self.controls = controls
        self.is_jumping = 0
        
        self.surf = pygame.Surface((30, 60))
        self.surf.fill(colour)
        self.rect = self.surf.get_rect()


        self.pos = vector((location))
        self.acceleration = 0
    
    def move(self):
        keys = pygame.key.get_pressed()
        if self.facing_right:
            if keys[self.controls[0]]:
                self.acceleration = 0
                self.pos[0] -= 2
            if keys[self.controls[2]]:
                self.pos[0] += 1 + (self.acceleration / 10)
                if self.acceleration < 30:
                    self.acceleration += 1
            elif not keys[self.controls[0]] and not keys[self.controls[2]]:
                self.acceleration = 0 

        if not self.facing_right:
            if keys[self.controls[0]]:
                self.pos[0] -= 1 + (self.acceleration / 10)
                if self.acceleration < 30:
                    self.acceleration += 1
            if keys[self.controls[2]]:
                self.acceleration = 0
                self.pos[0] += 2
            elif not keys[self.controls[0]] and not keys[self.controls[2]]:
                self.acceleration = 0

        if keys[self.controls[1]]:
            if self.pos[1] == GROUND:
                self.is_jumping = 20
    
    def jump(self):
        if self.is_jumping != 0:
            self.pos[1] -= 1 + self.is_jumping 
            self.is_jumping -= 1

class Floor():
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 15))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT))
