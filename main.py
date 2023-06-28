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

red_player = Player((WIDTH/3, GROUND), True, (255, 100, 100), [K_a, K_SPACE, K_d])
blue_player = Player(((WIDTH/3)*2, GROUND), False, (100, 100, 255), [K_LEFT, K_UP, K_RIGHT])
floor = Floor()

sprite_group = pygame.sprite.Group()

sprite_list = [
    floor,
    red_player,
    blue_player
]

for entity in sprite_list:
    sprite_group.add(entity)


def check_rel_position():
    if red_player.pos[0] > blue_player.pos[0]:
        red_player.facing_right = False
        blue_player.facing_right = True
    else:
        red_player.facing_right = True
        blue_player.facing_right = False


def fall():
    if red_player.pos[1] < GROUND:
        red_player.pos[1] += 7
    elif red_player.pos[1] > GROUND:
        red_player.pos[1] = GROUND
    if blue_player.pos[1] < GROUND:
        blue_player.pos[1] += 7
    elif blue_player.pos[1] > GROUND:
        blue_player.pos[1] = GROUND

def wall_collision():
    if red_player.pos[0] > WIDTH - 30:
        red_player.pos[0] = WIDTH - 30
    elif red_player.pos[0] < 0:
        red_player.pos[0] = 0
    if blue_player.pos[0] > WIDTH - 30:
        blue_player.pos[0] = WIDTH - 30
    elif blue_player.pos[0] < 0:
        blue_player.pos[0] = 0
    
def apply_physics():
    check_rel_position()
    fall()
    wall_collision()

