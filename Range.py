import pygame
import random

Width = 400
Height = 500

Y = (255, 255, 0)
G = (67, 130, 67)
R = (222, 100, 60)
B = (10, 10, 10)

pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Тир")
clock = pygame.time.Clock()
   
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(G)
        self.rect = self.image.get_rect()
        self.rect.centerx = Width // 2
        self.rect.bottom = Height - 30
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.rect.x += self.speedx
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        sprite.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(R)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(Width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 9)
        self.speedx = random.randrange(-2, 4)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > Height + 10 or self.rect.left < -25 or self.rect.right > Width + 20:
            self.rect.x = random.randrange(Width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(Y)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self): 
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

sprite = pygame.sprite.Group()
enemy = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
sprite.add(player)
for i in range(8):
    e = Enemy()
    sprite.add(e)
    enemy.add(e)

run = True
while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot()

    sprite.update()

    hits = pygame.sprite.groupcollide(enemy, bullets, True, True)
    for hit in hits:
        e = Enemy()
        sprite.add(e)
        enemy.add(e)
    if hits:
        run = True

    screen.fill(B)
    sprite.draw(screen)
    pygame.display.flip()

pygame.quit()
