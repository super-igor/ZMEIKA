import pygame as pg
import random as rnd
import os

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0,0,0)
GRAY = (35,30,25)

WIDTH = 1000
HEIGHT = 600
#Кадры в секунду
FPS = 60

IMG_HERO = os.path.join('img', 'hero.png') 
IMG_APPLE = os.path.join('img', 'apple.png')


#----------------
class Obj(pg.sprite.Sprite):
    def __init__(self, goto, size_1, size_2, file_name):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((size_1, size_2))
        self.image = pg.image.load(file_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (goto)
        self.direction = 1
        self.speed = 0

    def set_dir(self, new):
        self.direction = new
#вправо-влево
    def GO_RL(self):
        self.rect.x += self.speed       
#вверх-вниз
    def GO_UD(self):
        self.rect.y += self.speed

    def go_out(self):
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 1000
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = 600



    
#----------------
        
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()

#ОБЬЕКТЫ
player = Obj((WIDTH/2, HEIGHT/2), 30, 30, IMG_HERO)
apple = Obj((rnd.randint(10, WIDTH), rnd.randint(10, HEIGHT)), WIDTH, HEIGHT, IMG_APPLE)

all_sprites.add(player)
all_sprites.add(apple)



global_speed = 10
   
# Бесконечный цикл
while True:
    pg.time.delay(FPS)
    screen.fill(WHITE)
    
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_RIGHT:
                player.set_dir(90)
            elif i.key == pg.K_LEFT:
                player.set_dir(-90)
            elif i.key == pg.K_UP:
                player.set_dir(0)
            elif i.key == pg.K_DOWN:
                player.set_dir(180)
    if  player.direction == 90:
        player.speed = global_speed
        player.GO_RL()    
    elif player.direction == -90:
        player.speed = -global_speed
        player.GO_RL() 
    elif player.direction == 180:
        player.speed = global_speed
        player.GO_UD() 
    elif player.direction == 0:
        player.speed = -global_speed
        player.GO_UD() 

    player.go_out() 

    #BLITS      
    screen.blit(player.image, player.rect)     
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    
    pg.display.update()

pg.quit()
