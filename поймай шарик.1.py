import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

#объявляем возможные цвета шариков 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
j=0

def new_ball(): #функция, создающая новый шарик случайного цвета, размера и в случайном месте
    global x, y, r, color, j
    x = randint(100,1100)
    y = randint(100,600)
    r = randint(30,50)
    color = COLORS[randint(0, 3)]
    circle(screen, color, (x, y), r)
    balls_coordinate.append([x,y])
    balls_radius.append(r)
    balls_colours.append(color)
    balls_speed.append([randint(-5,5),randint(-5,5)])

balls_speed=[] #кортеж скоростей шариков
balls_coordinate=[] #кортеж координат шариков 
balls_radius=[] #кортеж радиусов шариков
balls_colours=[] #кортеж цветов шариков

def click(event): #событие клик мышки
    global j, score # score - подсчет очков, j - количество шариков
    for i in range(j):
        if (balls_coordinate[i][0]-event.pos[0])**2+(balls_coordinate[i][1]-event.pos[1])**2<=(balls_radius[i])**2: #условие того, что мы попали в круг
            score+=1
            balls_coordinate[i]=[randint(100,1100),randint(100,600)]
            balls_radius[i]=randint(30,50)
            balls_speed[i]=[randint(-5,5),randint(-5,5)]
            balls_colours[i]=COLORS[randint(0, 5)]
            break
   


pygame.display.update()
clock = pygame.time.Clock()
finished = False


    
def move(screen):
    for i in range(j):
        if balls_coordinate[i][0]+balls_radius[i]>=1200 or balls_coordinate[i][0]-balls_radius[i]<=0: #условие того, что шарик коснулся левой или правой стены
            balls_speed[i][0]=-balls_speed[i][0]       
        if balls_coordinate[i][1]+balls_radius[i]>=700 or balls_coordinate[i][1]-balls_radius[i]<=0:  #условие того, что шарик коснулся верхней или нижней стены
            balls_speed[i][1]=-balls_speed[i][1]
        balls_coordinate[i][0]+=balls_speed[i][0] #осуществляет движение шарика по горизонтали 
        balls_coordinate[i][1]+=balls_speed[i][1] #осуществляет движение шарика по вертикали 
        circle(screen, balls_colours[i], (balls_coordinate[i][0], balls_coordinate[i][1]), balls_radius[i])


score=0 #начальный счет 0
k=10 #к - количество шаров
for i in range(k): 
    new_ball()
    j+=1
    
FONT = pygame.font.Font(None, 50)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN: #если событие == клик мыши
            click(event) #проверяем, попали ли мы в круг

    move(screen) #двигаем шарики
  
 

    score_display = FONT.render(str(score), True, (255, 255, 255))
    screen.blit(score_display, (10, 10))
    pygame.display.update()
    screen.fill(BLACK)
    
pygame.quit()
