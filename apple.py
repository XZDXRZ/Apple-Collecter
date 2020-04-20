# Need: PyGame

import sys, pygame, random

size = (700,500)
bg_color = (255,255,255)
tick = 10

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size)
screen.fill(bg_color)
MAXNUM = 7
MAXSPEED = 2
apple_num = 0

# Player
miss = 0
did = 0

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./picmuc/apple.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [random.randint(50,size[0]-50),-50]
        self.t = [0,random.randint(1,MAXSPEED)]

    def move(self):
        self.rect = self.rect.move(self.t)
    
    def death(self):
        if self.rect.top>size[1]:
            return True
        return False

class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./picmuc/board.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [size[0]/2, 400]

    def move(self):
        x_pos = pygame.mouse.get_pos()[0]
        self.weith = (self.rect.right-self.rect.left)/2
        x_pos-=self.weith
        if x_pos < 0:
            x_pos = 0
        elif x_pos > size[0]:
            x_pos = size[0]-self.weith
        self.rect.left = x_pos

def animate():
    global apple_num, did, miss, infofont
    screen.fill(bg_color)
    for apple in apples:
        apple.move()
        if apple.death():
            apples.remove(apple)
            apple_num -= 1
            miss += 1
        screen.blit(apple.image, apple.rect)
    board.move()
    didsurface = infofont.render('Did: '+str(did),False,[0,233,0])
    screen.blit(didsurface,[20,20])
    misssurface = infofont.render('Miss: '+str(miss),False,[0,0,233])
    screen.blit(misssurface,[20,45])
    screen.blit(board.image, board.rect)
    if pygame.sprite.spritecollide(board, apples, True):
        did += apple_num - len(apples)
        apple_num = len(apples)
    for i in range(apple_num,MAXNUM):
        apples.add(Apple())
        apple_num+=1
    pygame.display.flip()
    pygame.time.delay(tick)

apples = pygame.sprite.Group()
running = True
board = Board()
pygame.mixer.music.load('./picmuc/music.wav')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
infofont = pygame.font.SysFont('microsoft Yahei',40)

while running:
    animate()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
sys.exit()