import pygame
pygame.init()

clock = pygame.time.Clock()
FPS = 60

img = pygame.image.load('files\icon.ico')
pygame.display.set_icon(img)

pygame.display.set_caption("Alone in the Dark")

screen = pygame.display.set_mode((1080,720))
screen.fill((30,30,30))
pygame.display.update()

time_in = 0

while True:
    clock.tick( FPS )
    time_in += 1
    if time_in == 55:
        screen.fill((50,50,50))
        pygame.display.update()
    if time_in == 56:
        screen.fill((80,80,80))
        pygame.display.update()
    if time_in == 57:
        screen.fill((120,120,120))
        pygame.display.update()
    if time_in == 58:
        screen.fill((200,200,200))
        pygame.display.update()
    if time_in == 59:
        img2 = pygame.image.load('files\start.png').convert_alpha()
        screen.blit(img2,(416,236))
        screen.fill((240,240,240))
        pygame.display.update()
    if time_in == 60:
        img2 = pygame.image.load('files\start.png').convert_alpha()
        screen.fill((255,255,255))
        screen.blit(img2,(416,236))
        pygame.display.update()
    if time_in == 180:
        img1a = pygame.transform.scale(img2, (248*.9, 248*.9))
        screen.fill((255,255,255))
        screen.blit(img1a,(416,236))
        pygame.display.update() 
    if time_in == 180:
        img1a = pygame.transform.scale(img2, (248*.85, 248*.85))
        screen.fill((255,255,255))
        screen.blit(img1a,(416,236))
        pygame.display.update() 
    if time_in == 182:
        img1a = pygame.transform.scale(img2, (248*.8, 248*.8))
        screen.fill((255,255,255))
        screen.blit(img1a,(416,236))
        pygame.display.update() 
    if time_in == 184:
        img1a = pygame.transform.scale(img2, (248*.7, 248*.7))
        screen.fill((255,255,255))
        screen.blit(img1a,(400,216))
        pygame.display.update() 
    if time_in == 186:
        img1a = pygame.transform.scale(img2, (248*.55, 248*.55))
        screen.fill((255,255,255))
        screen.blit(img1a,(390,216))
        pygame.display.update() 
    if time_in == 188:
        img1a = pygame.transform.scale(img2, (248*.55, 248*.55))
        screen.fill((255,255,255))
        screen.blit(img1a,(340,195))
        pygame.display.update() 
    if time_in == 190:
        img1a = pygame.transform.scale(img2, (248*.55, 248*.55))
        screen.fill((255,255,255))
        screen.blit(img1a,(265,190))
        pygame.display.update() 
    if time_in == 192:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(180,190))
        pygame.display.update() 
    if time_in == 194:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(130,190))
        pygame.display.update() 
    if time_in == 196:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(100,190))
        pygame.display.update() 
    if time_in == 198:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(80,190))
        pygame.display.update() 
    if time_in == 200:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(65,190))
        pygame.display.update() 
    if time_in == 202:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(60,190))
        pygame.display.update() 
    if time_in == 204:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(64,190))
        pygame.display.update() 
    if time_in == 204:
        img1a = pygame.transform.scale(img2, (248*.5, 248*.5))
        screen.fill((255,255,255))
        screen.blit(img1a,(66,190))
        pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
