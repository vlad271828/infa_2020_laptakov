import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


rect(screen, (0,0,100), (0,0,400,50))
rect(screen, (120,80,210), (0,50,400,30))
rect(screen, (230,130,240), (0,80,400,50))
rect(screen, (200,100,170), (0,130,400,50))
rect(screen, (230,120,70), (0,180,400,40))
rect(screen, (0,100,200), (0,220,400,200))
pi = 3.14
arc(screen, (255,255,255), (50, 50, 100, 80), 0.3*pi, 0.8*pi,3)
arc(screen, (255,255,255), (100, 50, 130, 80), 0.25*pi, 0.7*pi,3)

arc(screen, (255,255,255), (150, 100, 100, 80), 0.3*pi, 0.8*pi,3)
arc(screen, (255,255,255), (200, 100, 130, 80), 0.25*pi, 0.7*pi,3)

arc(screen, (255,255,255), (200, 200, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (220, 200, 50, 100), 0.4*pi, 0.67*pi,3)

arc(screen, (255,255,255), (100,70, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (120, 70, 50, 100), 0.4*pi, 0.67*pi,3)

arc(screen, (255,255,255), (120, 200, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (140, 200, 50, 100), 0.4*pi, 0.67*pi,3)

arc(screen, (255,255,255), (160, 80, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (180, 80, 50, 100), 0.4*pi, 0.67*pi,3)

arc(screen, (255,255,255), (180, 65, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (200, 65, 50, 100), 0.4*pi, 0.67*pi,3)

arc(screen, (255,255,255), (300, 150, 70, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (320, 150, 70, 100), 0.3*pi, 0.6*pi,3)

arc(screen, (255,255,255), (270, 180, 70, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (290, 180, 70, 100), 0.3*pi, 0.6*pi,3)

arc(screen, (255,255,255), (250, 120, 70, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (270, 120, 70, 100), 0.3*pi, 0.6*pi,3)

arc(screen, (255,255,255), (50, 170, 100, 80), 0.3*pi, 0.8*pi,3)
arc(screen, (255,255,255), (100, 170, 130, 80), 0.25*pi, 0.7*pi,3)

arc(screen, (255,255,255), (150,150, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (170,150, 50, 100), 0.4*pi, 0.67*pi,3)

arc(screen, (255,255,255), (120,120, 50, 100), 0.4*pi, 0.7*pi,3)
arc(screen, (255,255,255), (140,120, 50, 100), 0.4*pi, 0.67*pi,3)

def fish(x0, y0, a, l):
    k = 220 / l
    sfish = pygame.Surface((220, 115))
    polygon(sfish, (102, 99, 112), ((160, 60),(171, 58), (196, 73), (168, 88)), 0)
    arc(sfish, (71, 136, 147), (65, 33, 148, 50), 0.4, 2.74, 30)
    arc(sfish, (71, 136, 147), (65, 13, 148, 50), 3.44, 6, 30)
    polygon(sfish, (71, 136, 147), ((67, 45),(14, 80), (4, 35)), 0) # хвост рыбы
    polygon(sfish, (102, 99, 112), ((135, 33), (94, 0), (164, 15),(172, 24), (171, 35)),0) # верхний плавник
    polygon(sfish, (102, 99, 112), ((97, 59),(80, 79), (112, 84), (114, 62)), 0) # нижний плавник
    circle(sfish, (2, 57, 147), (170, 47), 7, 0) # глаз
    circle(sfish, (5, 64, 85), (170, 47), 5, 0)

    sfish = pygame.transform.rotate(sfish, a)
    sfish = pygame.transform.rotozoom(sfish, 0, k)
    sfish.set_colorkey((0, 0, 0))
    screen.blit(sfish, (x0, y0))


fish(300,300,0,600)
fish(0,350,0,600)
fish(260,350,360,550)

def gos(x0,y0,a,l):
    k=220/l
    sgos = pygame.Surface((400, 450))
    polygon(sgos,(255,255,5),((255,290),(295,283),(305,290),(295,297)))
    polygon(sgos,(255,255,255),((130,315),(100,275),(90,310),(130,335)))
    polygon(sgos,(255,255,255),((170,330),(173,325),(178,320),(180,300),(183,280),(184,270),(184,260),(182,250),(180,245),(170,243),
           (165,241),(160,240),(155,238),(150,236),(145,235),(140,232),(135,228),(130,224),(125,220),(120,216),(115,214),(110,210),
                                (105,205),(100,205),(95,208),(94,209),(96,211),(98,218),(102,222),(110,227),(115,235),(125,245),(135,265),
                                (140,280),(145,290),(150,300)))
    line(sgos,(28,28,28),(256,290),(302,290),1)
    ellipse(sgos,(255,255,255),(200,295,60,25))
    ellipse(sgos,(255,255,255),(240,280,40,23))
    ellipse(sgos,(255,255,255),(120,300,120,50))
    arc(sgos,(255,255,5),(240,380,50,100),1,2,2)
    arc(sgos,(255,255,5),(235,380,50,170),1,2,3)
    arc(sgos,(255,255,5),(230,375,80,170),1,2,2)
    arc(sgos,(255,255,5),(230,375,80,170),2,2.3,2)

    arc(sgos,(255,255,5),(240,400,50,100),1,2,2)
    arc(sgos,(255,255,5),(235,400,50,170),1,2,3)
    arc(sgos,(255,255,5),(230,395,80,170),1,2,2)
    arc(sgos,(255,255,5),(230,395,80,170),2,2.3,2)

    circle(sgos,(28,28,28),(270,290),5) #глаз
    

    
    ss=pygame.Surface((400, 400)) #нога
    ellipse(ss,(255,255,255),(250,200,60,25))
    ellipse(ss,(255,255,255),(260,220,60,25))
    ss=pygame.transform.rotate(ss, 300)
    ss = pygame.transform.rotozoom(ss, 0, k)
    ss.set_colorkey((0, 0, 0))
    screen.blit(ss, (x0-110,y0-5))

    ss1=pygame.Surface((400, 400)) #нога бедро1 
    ellipse(ss1,(255,255,255),(250,200,70,15))
    ss1=pygame.transform.rotate(ss1, 340)
    ss1 = pygame.transform.rotozoom(ss1, 0, k)
    ss1.set_colorkey((0, 0, 0))
    screen.blit(ss1, (x0-110,y0+100))
    
    ss2=pygame.Surface((400, 400)) #нога2 бедро2
    ellipse(ss2,(255,255,255),(250,200,70,15))
    ss2=pygame.transform.rotate(ss2, 340)
    ss2 = pygame.transform.rotozoom(ss2, 0, k)
    ss2.set_colorkey((0, 0, 0))
    screen.blit(ss2, (x0-100,y0+80))

    
    

    
    

    sgos = pygame.transform.rotate(sgos, a)        
    sgos = pygame.transform.rotozoom(sgos, 0, k)
    sgos.set_colorkey((0, 0, 0))
    screen.blit(sgos, (x0, y0))       

gos(-70,-20,0,220)


















pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()







