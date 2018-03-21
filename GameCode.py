import pygame
from pygame.locals import *
from weatherAPI import *
import random
import math

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self). __init__()
        
        self.xvelocity = 0
        self.yvelocity = 0
        self.frame = 0
        self.frames = [pygame.image.load('mjordan1.png').convert(), pygame.image.load('mjordan2.png').convert(), pygame.image.load('mjordan.png').convert()]
        self.image = self.frames[2]
        self.image.set_colorkey((153, 217, 234), RLEACCEL)
        self.rect = pygame.Rect((10, 500),(self.image.get_rect()[2],self.image.get_rect()[3]))           
        self.start = True
    def update(self, pressed_keys, time, intro):
        #if pressed_keys[K_UP]:
            #self.yvelocity=-10
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0, 1)
        self.time = time%(60*.5)
        if self.time == 0 and intro == True:
            
            
            self.image = self.frames[self.frame%2]
            self.image.set_colorkey((153, 217, 234), RLEACCEL)
            self.rect = pygame.Rect((self.rect.left,self.rect.top),(self.image.get_rect()[2],self.image.get_rect()[3]))
            self.frame += 1
            
        elif intro == False and self.start:
            self.image = self.frames[2]
            self.image.set_colorkey((153, 217, 234), RLEACCEL)
            self.rect = pygame.Rect((self.rect.left,self.rect.top),(self.image.get_rect()[2],self.image.get_rect()[3]))
            self.start = False

            new_cloud = Cloud("grey")
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            new_cloud = Cloud("grey")
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            new_cloud = Cloud("grey")
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            new_cloud = Cloud("grey")
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
            
        if pressed_keys[K_RIGHT]:
            self.xvelocity=10
        if pressed_keys[K_LEFT]:
            self.xvelocity= -10
            
            

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800-player.rect.width/2:
            self.rect.right = 800-player.rect.width/2
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.yvelocity=0

        self.rect.move_ip(self.xvelocity, self.yvelocity)
        self.xvelocity *= 0.8
        if self.xvelocity < 1:
            self.xvelocity = 0
        self.yvelocity+=1

        if intro == True:
            self.xvelocity = 10
        

class Cloud(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Cloud, self).__init__()
        if color == "grey":
            self.image = pygame.image.load('rsz_greycloud.png').convert_alpha()

        else:
            self.image.load('rsz_whitecloud.png').convert_alpha()

        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(lastCloud-100,600))
        )
    def update(self):
        self.rect.move_ip(cloudSpeed, 0)
        if self.rect.right < 0:
            self.kill()

class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super(Rain, self).__init__()
        self.image = pygame.image.load('raindrop.jpg').convert_alpha()

        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.image.get_rect(
            center = (random.randint(0, 800), random.randint(100,200))
            )
    def update(self):
        self.rect.move_ip(0, 1)
        if self.rect.top > 600:
            self.kill()
               
        
    
            
display_width = 800
display_height = 600

pygame.init()

screen = pygame.display.set_mode((display_width,display_height))

player = Player()

background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))

introBackground = pygame.image.load('NBAcourtfixed.png').convert_alpha()
exitBackground = pygame.image.load('lebronJames.png').convert_alpha()
exitBackground1 = pygame.image.load('jordanexit.jpg').convert_alpha()
exitBackground1 = pygame.transform.scale(exitBackground1, (800, 600))
exitBackground2 = pygame.image.load('jordanvlebron.png').convert_alpha()
exitBackground2 = pygame.transform.scale(exitBackground2, (800, 600))

welcome = True
while welcome:
    
    introBackground1 = pygame.image.load('mjvlbj.jpg').convert_alpha()
    introBackground1 = pygame.transform.scale(introBackground1, (800, 600))
    screen.blit(introBackground1, (0,0))
    
    basicfont1 = pygame.font.SysFont('AzureoN', 50)
    text1 = basicfont1.render('Welcome to The Game', True, (255, 255, 255))
    textrect1 = text1.get_rect()
    textrect1.centerx = screen.get_rect().centerx
    textrect1.centery = screen.get_rect().centery - 115
    screen.blit(text1, textrect1)

    basicfont2 = pygame.font.SysFont('Quango', 50)
    text2 = basicfont2.render('(Press S to Begin)', True, (255, 255, 255))
    textrect2 = text2.get_rect()
    textrect2.centerx = screen.get_rect().centerx
    textrect2.centery = screen.get_rect().centery + 115
    screen.blit(text2, textrect2)
    

    basicfont3 = pygame.font.SysFont('Quango', 50)
    text3 = basicfont3.render('Michael Jordan Needs to Defend His Crown!', True, (255, 255, 255))
    textrect3 = text3.get_rect()
    textrect3.centerx = screen.get_rect().centerx
    textrect3.centery = screen.get_rect().centery - 20
    screen.blit(text3, textrect3)
       

    basicfont4 = pygame.font.SysFont('Quango', 50)
    text4 = basicfont4.render('Use Arrows to Control', True, (255, 255, 255))
    textrect4 = text4.get_rect()
    textrect4.centerx = screen.get_rect().centerx
    textrect4.centery = screen.get_rect().centery + 50
    screen.blit(text4, textrect4)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            welcome = False

players = pygame.sprite.Group()
clouds = pygame.sprite.Group()
raindrops = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

ADDCLOUD = ''
ADDRAIN = ''
ADDGREYCLOUD = ''

ADDCLOUD = pygame.USEREVENT + 1
cloud_time = 2500
pygame.time.set_timer(ADDCLOUD, cloud_time)

ADDRAINDROP = pygame.USEREVENT + 2
raindrop_time = 10000
pygame.time.set_timer(ADDRAINDROP, raindrop_time)



rainy_condition = ["Drizzle", "Rain", "Rain Mist", "Rain Showers", "Thunderstorms and Rain"]

cloudy_conditions = ["Partly Cloudy", "Scattered Cloud", "Mostly Cloudy", "Overcast"]



wc = getWeatherCondition(station_data)

#if wc in rainy_condition:
    #raindrops = pygame.sprite.Group()

if wc == cloudy_conditions[2] or wc == cloudy_conditions[3]:
    pygame.time.set_timer(ADDCLOUD, 500)
    background.fill((211, 211, 211))

if wc in rainy_condition:
    ADDRAINDROP = pygame.USEREVENT + 3
    background.fill((211, 211, 211))

    ADDGREYCLOUD = pygame.USERVENT + 5
    pygame.time.set_timer(ADDGREYCLOUD, 100)

time = 0
            
            
level = 1

intro = True
lastCloud = 500
new_cloud2 = Cloud("grey")
clouds.add(new_cloud2)
all_sprites.add(new_cloud2)
new_cloud2.rect = new_cloud2.image.get_rect(center=(900, 550))
        


running = True

while running:
    pygame.time.Clock().tick(60)
    moveOnCloud = 1
    cloudSpeed = -2 * math.log(level + 1)/math.log(2)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                print("escape")
        elif event.type == QUIT:
            running = False
            print("Quit")

        elif(event.type == ADDCLOUD and intro == False):
            new_cloud = Cloud("grey")
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            lastCloud = new_cloud.rect.y

        #elif event.type == ADDRAINDROP:
            #new_rain = Rain()
            #all_sprites.add(new_rain)
            #raindrops.add(new_rain)

    time += 1
    pressed_keys = pygame.key.get_pressed()
    for cloud in clouds:
        if (player.rect.bottom+15>cloud.rect.top and player.rect.bottom-15<cloud.rect.top and player.rect.right>cloud.rect.left and player.rect.left<cloud.rect.right and player.yvelocity>=0):
            player.yvelocity=0
            if pressed_keys[K_UP]:
                player.yvelocity=-25

            player.rect.bottom=cloud.rect.top
            if moveOnCloud == 1:
                moveOnCloud = 0
                
                player.rect.move_ip(cloudSpeed,0)
    if player.rect.bottom>=599 and pressed_keys[K_UP]:
        player.yvelocity=-25
        player.rect.move_ip(0,-1)

        
    if intro == False:
        screen.blit(background,(0,0))

    
    player.update(pressed_keys, time, intro)
    
    clouds.update()

    if (time % 600) == 0:
        level += 1

    basicfont1 = pygame.font.SysFont(None, 48)
    text1 = basicfont1.render("Level " + str(level), True, (0, 0, 0))
    screen.blit(text1, (25, 25))
    if wc in rainy_condition:
        raindrops.update()

    if player.rect.left > screen.get_width()/2 + 230 and intro==True:
        player.rect.move_ip(0,-50)
    if player.rect.top < 0:
        intro = False

    #screen.blit(player.surf, player.rect)

    #draw surf onto screen
    #screen.blit(surf, (400, 400))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if (player.rect.bottom > display_height):
        player.kill()
        killed = True
        running = False
    if intro == True:
        screen.blit(introBackground, (0, 0))
        screen.blit(player.image, player.rect)
    pygame.display.flip()

while killed:
    basicfont = pygame.font.SysFont('AzureoN', 52)

    if level <= 8:
        screen.blit(exitBackground, (0, 0))
        pygame.time.Clock().tick(60)
        text = basicfont.render('I am the King Now MJ!', True, (255, 255,255))
        textrect = text.get_rect()
        textrect.centerx = 600
        textrect.centery = 50
        screen.blit(text, textrect)
        
        text = basicfont.render('Ha! Only Level ' + str(level) + '!', True, (255, 255,255))
        textrect = text.get_rect()
        textrect.centerx = 625
        textrect.centery = 90
        screen.blit(text, textrect)
        
    if level >= 9 and level < 14:
        screen.blit(exitBackground2, (0, 0))
        pygame.time.Clock().tick(60)
        text = basicfont.render('We Are Still Battling', True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = 300
        textrect.centery = 50
        screen.blit(text, textrect)
        
        text = basicfont.render('Level ' + str(level), True, (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = 300
        textrect.centery = 90
        screen.blit(text, textrect)

    if level >= 15:
        screen.blit(exitBackground1, (0, 0))
        pygame.time.Clock().tick(60)
        text = basicfont.render('All Hail the King!', True, (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = 625
        textrect.centery = 50
        screen.blit(text, textrect)
        
        text = basicfont.render('Wow! Level ' + str(level) + '!', True, (0, 0, 0))
        textrect = text.get_rect()
        textrect.centerx = 625
        textrect.centery = 90
        screen.blit(text, textrect)
    



    
    pygame.display.flip()

    
        
        

pygame.quit()
