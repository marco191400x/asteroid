from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_y = size_y
        self.size_x = size_x
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))

class jugador(GameSprite): 
    def actualizar(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x < vent_h -65:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x >  0:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.y > 0  :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < vent_w -65 :
            self.rect.y += self.speed
    def fire(self):
        Bullet = bala('bullet_bill.png',self.rect.centerx,self.rect.top,15,20, 15 )
        bullet.add(Bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
        
            
class bala(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if 0 > self.rect.y:
            self.kill()   


vent_h = 700
vent_w = 500
ventana = display.set_mode ((vent_h,vent_w))
fondo = transform.scale(image.load("galaxy.jpg") ,(700,500))
nave =  jugador('nave3.png', 0,230,5,15,5)
obtaculo = sprite.Group()
for i in range(1,6):
    ufo = Enemy('ufo.png',randint(0, vent_w - 80),0,80,50,randint(2,4))
    obtaculo.add(ufo)


bullet = sprite.Group()



fin = True
clock = time.Clock()
fps = 60
game = True


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    ventana.blit(fondo,(0,0))
    nave.actualizar()
    bullet.update()
    obtaculo.update()
    obtaculo.draw(ventana)
    
    bullet.draw(ventana)
    nave.reset()
    display.update()
    clock.tick(fps)