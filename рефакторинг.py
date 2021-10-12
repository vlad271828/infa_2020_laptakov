import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

back_color = (255, 255, 0) # Цвет пляжа
sea_colour = (0, 0, 255) #цвет моря

screen.fill(back_color)#весь экран становится цвета пляжа, позже поверх появляются другие элементы

def multicloud (main_cloud_x, main_cloud_y, cloud_radius, ro_cloud, cv):# изображает облако в виде нескольких белых кружочков
    #par main_cloud_x: координата х центра облака
    #par main_cloud_y: координата у цетра облака
    #par cloud+radius: радиус однго круга, из которых состоит облако
    #par ro_cloud: расстояние между кружками(их густота), из которых состоит облако
    #par cv: градация от черного(0) до белого(255)
	circle(screen, (0, 0, 0), (main_cloud_x, main_cloud_y), cloud_radius + 1) #Cloud0
	circle(screen, (cv, cv, cv), (main_cloud_x, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x - ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud1
	circle(screen, (cv, cv, cv), (main_cloud_x - ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 3, main_cloud_y), cloud_radius + 1) #Cloud2
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 3, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud3
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 2, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 6, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud4
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 6, main_cloud_y + ro_cloud * 3), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 8, main_cloud_y), cloud_radius + 1) #Cloud5
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 8, main_cloud_y), cloud_radius)
	circle(screen, (0, 0, 0), (main_cloud_x + ro_cloud * 10, main_cloud_y + ro_cloud * 3), cloud_radius + 1) #Cloud6
	circle(screen, (cv, cv, cv), (main_cloud_x + ro_cloud * 10, main_cloud_y + ro_cloud * 3), cloud_radius)

def umbrella(left_upper_x, left_upper_y, dx_umb, h_umb, umb_radius, umb_start, deltha, colour_up, colour_down): #изображает пляжный зонтик
    #par left_upper_x: координата х левого края столба зонтика
    #par left_upper_y: координата у самой вершины зонтика
    #par dx_umb: толщина столба зонтика
    #par h_umb: высота столба зонтика
    #par umb_radius: радиус шапки зонтика
    #par umb_start: длина зонтика по у (от верхней точки зонтика и вниз)
    #par deltha: расстояние между спицами (не делать больше par umb_radius)
    #par colour_up: цвет шапки зонтика в RGB
    #par colour_down: цвет столба в RGB
	rect(screen, (colour_down), (left_upper_x, left_upper_y, dx_umb, h_umb)) #Столб зонтика(экран, цвет RGB, координаты многоугольника)
	polygon(screen, (colour_up), [(left_upper_x + dx_umb, left_upper_y),
	 (left_upper_x + dx_umb, left_upper_y + umb_start), (left_upper_x + dx_umb + umb_radius, left_upper_y + umb_start)])
	#рисует правый треугольник шапки зонтика
	polygon(screen, (colour_up), [(left_upper_x, left_upper_y),
	 (left_upper_x, left_upper_y + umb_start), (left_upper_x - umb_radius, left_upper_y + umb_start)])
	#рисует левый треугольник шапки треугольника
	rect(screen, (colour_up), (left_upper_x, left_upper_y, dx_umb, umb_start))
	#исправляет цвет шапки зонтика в ее пересечении со столбом (чтобы столб не выделялся)
	
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 1 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 2 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x - umb_radius + 3 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 3 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 2 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb + umb_radius - 1 * deltha, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x + dx_umb, left_upper_y), (left_upper_x + dx_umb, left_upper_y + umb_start))
	aaline(screen, (0, 0, 0), (left_upper_x, left_upper_y), (left_upper_x, left_upper_y + umb_start))
	#спицы зонтика
	
def draw_deck(boat_0_x, boat_0_y, proportion,deck_color): #изображает корпус корабля
        #par boat_0_x: координата х левого края прямоугоьного основания
        #par boat_0_y: координата у верхней части корпуса
        #par proporotion: пазмер корпуса с сохранением пропорций
        #par deck_colour: цвет корпуса
	circle(screen, deck_color, (boat_0_x, boat_0_y), proportion * 7)
	rect(screen, sea_colour, (boat_0_x - proportion * 7, boat_0_y - proportion * 7, proportion * 7 * 2, proportion * 7))
	rect(screen, sea_colour, (boat_0_x, boat_0_y, proportion * 7, proportion * 7))
	rect(screen, (0, 0, 0), (boat_0_x, boat_0_y, proportion * 28 + 2, proportion * 7))
	rect(screen, deck_color, (boat_0_x + 1, boat_0_y, proportion * 28, proportion * 7))
	polygon(screen, (0, 0, 0), [(boat_0_x + proportion * 28 + 2, boat_0_y),
	 (boat_0_x + proportion * 28 + 2, boat_0_y + proportion * 7 - 1), (boat_0_x + proportion * 43, boat_0_y)])
	polygon(screen, deck_color, [(boat_0_x + proportion * 28 + 2, boat_0_y),
	 (boat_0_x + proportion * 28 + 2, boat_0_y + proportion * 7 - 1), (boat_0_x + proportion * 43, boat_0_y)])
	circle(screen, (0, 0, 0), (boat_0_x + proportion * 33, boat_0_y + proportion * 3 - 2), proportion * 2)
	circle(screen, (255, 255, 255), (boat_0_x + proportion * 33, boat_0_y + proportion * 3 - 2), proportion * 2 - 3)


	
def draw_sail(sail_x, sail_y, sail_color, proportion): #рисует один флаг
        #par sail_x: координата х самой левой части флага
        #par sail_y: координата у самой верхней части флага
        #par sail_colour: цвет флага
        #par prorotion: размер флага с сохранением пропорций
	rect(screen, (0, 0, 0), (sail_x, sail_y, proportion * 2 - 2,  2 * 10 * proportion))
	polygon(screen, sail_color, [(sail_x + proportion * 2 - 2, sail_y),
	 (sail_x + proportion * 6, sail_y + proportion * 10), (sail_x + proportion * 14, sail_y + proportion * 10)])
	polygon(screen, sail_color, [(sail_x + proportion * 2 - 2, sail_y + proportion * 10 * 2),
	 (sail_x + proportion * 6, sail_y + proportion * 10), (sail_x + proportion * 14, sail_y + proportion * 10)])
	aaline(screen, (0, 0, 0), (sail_x + proportion * 6, sail_y + proportion *10), (sail_x + proportion * 14, sail_y + proportion * 10))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 6, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 14, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 6, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y + 2 * 10 * proportion))
	aaline(screen, (0, 0, 0), (sail_x + proportion * 14, sail_y + proportion *10), (sail_x + proportion * 2 - 2, sail_y + 2 * 10 * proportion))


def draw_sin (w_start, w_stop, y_wave, h_wave): #изображает одну волну песка(сегмент)
        #par w_start: координата х начала волны
        #par w_stop: координата х конца волны
        #par y_wave: координата у волны
        #par h_wave: высота волны
        
        
	d_wave = (w_stop - w_start)/90 
	for i in range(89):
		polygon(screen, back_color , [(w_start + d_wave * i, y_wave), 
		(w_start + d_wave * (i + 1), y_wave), (w_start + d_wave * i, y_wave - np.sin(np.pi * i / 90) * h_wave), 
		(w_start + d_wave * (i + 1), y_wave - np.sin(np.pi * (i + 1) / 90) * h_wave)])
		#функция аппроксимирует волну многоугольником с большим колиством сторон

def anti_sin (w_start, w_stop, y_wave, h_wave): # рисует морскую волну (cегмент)
        
        #par w_start: координата х начала волны
        #par w_stop: координата х конца волны
        #par y_wave: координата у волны
        #par h_wave: высота волны
        
	d_wave = (w_stop - w_start)/90
	for i in range(89):
		polygon(screen, sea_colour, [(w_start + d_wave * i, y_wave), 
		(w_start + d_wave * (i + 1), y_wave), (w_start + d_wave * i, y_wave + np.sin(np.pi * i / 90) * h_wave),
		 (w_start + d_wave * (i + 1), y_wave + np.sin(np.pi * (i + 1) / 90) * h_wave)])
	#функция аппроксимирует волну многоугольником с большим колиством сторон

def sun(R, r, sunlights, x, y,colour):
        #par R: радиус солнца
        #par r: длина лучиков солнца
        #par sunlights: количесвто лучиков
        #par x: оордината х центра солнца
        #par y: координата у центра солнца
        #par colour: цвет солнца в RGB
        circle(screen, colour, (x,y), R) 
        for i in range(sunlights):
                polygon(screen, colour, [(x + R * np.sin ( 2 * i * np.pi / sunlights), 
	y - R * np.cos (2 * i * np.pi / sunlights)), (x + R * np.sin ( (2 * i + 1) * np.pi / sunlights),
	 y - R * np.cos ((2 * i + 1) * np.pi / sunlights)), ((x + (R + r) * np.sin ((2 * i + 0.5) * np.pi / sunlights),
	  y - (R + r) * np.cos ((2 * i + 0.5) * np.pi / sunlights)))])

rect(screen, sea_colour, (0, 0, 600, 260))
#создает море, где у=260 - его нижняя граница

for i in range (7):
	draw_sin (43 * i * 2, 43 * (i * 2 + 1), 260, 10) #par y_wave должен совпадать с нижней границей моря
	anti_sin (43 * (i * 2 + 1), 43 * (i * 2 + 2), 260, 10) #par y_wave должен совпадать с нижней границей моря
	#изображает 14 сегментов цвета моря и песка,из-за чего складывается иллюзия волны


draw_deck(360, 190, 5,(255, 0, 255))
draw_deck(185, 170, 2,(139, 80, 20))
#изображает корабли


rect(screen, (129, 218, 247), (0, 0, 600, 160)) #рисует небо

sun(40, 8, 20, 540, 60,(255, 255, 0)) #рисует солнце

multicloud(50, 40, 15, 5, 255)
multicloud(306, 30, 25, 8, 255)
multicloud(156, 70, 25, 8, 255)
# изображает облака

draw_sail(500, 90,(255, 0, 0), 5)
draw_sail(425, 70, (0, 0, 255), 6)
draw_sail(350, 90, (255, 255, 255), 5)
draw_sail(215, 130, (218, 173, 128), 2)
#изображает флаги к кораблям







umbrella(110, 220, 8, 140, 54, 25, 15,(249,96,75),(210,110,34))
umbrella(240, 245, 4, 96, 28, 28, 7,(249,96,75), (210,110,34))
#изображает зонтики


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
