import pygame as pg
import time
import random
class Game_Box():
    def __init__(self, window_width=600) -> None:
        """
        Параметры:
        window_width - ширина квадратного окна для pygame
        border - расстояние между клеточками
        """
        super().__init__()
        
        #Параметры окна pygame
        self.window_width = window_width #Ширина квадратного окна
        self.window_height = window_width

    def draw(self) -> None:
        #Берем стартовое время
        self.start_time = time.time()
        #Отрисовка первого решения через PyGame
        pg.init()#Инициализируем
        running = 1
        #создаем квадратное окошко размером window_width
        sc = pg.display.set_mode((self.window_width, self.window_height))
        
        #Создадим телегу
        wagon = Wagon(0, 50)
        wagon_rect = pg.Rect(wagon.pos_x, self.window_height-wagon.pos_y, 100, 50)
        #Лист медведей
        list_of_bears = []
        #Кол-во fps
        clock = pg.time.Clock()
        #Кол-во очков
        cnt = 0
        #Шрифт, которым рисую буковки
        font = pg.font.SysFont(None, 24)
        """
        random_time и past работают в совокупности, потому что 
        при использовании одного лишь random_time медведи спавнятся каждый кадр, выходит очень уж много.
        Поэтому я ограничиваю переменной past время последнего спавна
        """
        
        #Время, прошедшее с последнего спавна
        past = 0
        #Ловим события на доске
        while running:
            clock.tick(30)
            #Индексы тех медведей, которых следует удалить
            bad_indexes = []
            #Раз в какое время должны появляться медведи
            random_time = random.randint(2,3)
            #Получаю нынешнее время
            self.finish_time = time.time()
            #Получаю разницу в секундах от старта до нынешнего времени, до десятых
            now = round(self.finish_time-self.start_time, 1)
            #Спавню медведей в количестве 1-2 штуки раз в 2-3 секунды
            if now%random_time==0 and now - past > 0.5:
                for i in range(random.randint(1,2)):
                    b = Bear(random.randint(0, self.window_width), 10+random.randint(-250,0), 5, self.window_height-50)
                    list_of_bears.append(b)
                past = now
            #двигаю каждого медведя
            for i in list_of_bears:
                i.pos_y += i.speed
            #Получаю события на экране
            for event in pg.event.get():
                if event.type == pg.MOUSEMOTION:
                    # Определяем x, y нажатия на доске
                    x, y = event.pos
                    #двигаю корыто на экране
                    wagon_rect.center = (x,  self.window_height-wagon.pos_y)
            
            #Закрашиваю фон белым, чтобы не оставалось следов
            sc.fill((255,255,255))
            #Проверка на ряд условий: выход за границы, касания медведей
            for i in range(len(list_of_bears)):
                if list_of_bears[i].pos_y > list_of_bears[i].dead_line:
                    bad_indexes.append(i)
                elif pg.Rect(list_of_bears[i].pos_x, list_of_bears[i].pos_y, 30, 30).colliderect(wagon_rect):
                    cnt+=1
                    bad_indexes.append(i)
                else:
                    pg.draw.rect(sc, list_of_bears[i].color, (list_of_bears[i].pos_x, list_of_bears[i].pos_y, 30, 30))
            #Удаление элементов, которые удовлетворили прошлым условиям
            for i in range(len(bad_indexes)):
                del list_of_bears[bad_indexes[i]-i]
            #Рисую корыто
            pg.draw.rect(sc, wagon.color, wagon_rect)
            #Вырисовываю очки
            img = font.render('Ваши очки: '+str(cnt), True, (0,0,0))
            sc.blit(img, (10,10,40,10))
            #Вырисовываю время:
            time_render = font.render("Время: "+str(int(self.finish_time-self.start_time)), True, (0,0,0))
            sc.blit(time_render, (10,30,40,10))
            #Обновляю экран
            pg.display.update()

class Bear():
    def __init__(self, pos_x:int, pos_y:int, speed:int, dead_line:int,color=(160, 62, 41)) -> None:
        self.time_start = time.time()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.speed = speed
        self.dead_line = dead_line
    
    def moving(self, speed):
        self.pos_y += speed
        if self.pos_y <= self.dead_line:
            self.color = (255,255,255)
        return self

class Wagon():
    def __init__(self, pos_x, pos_y, color=(101, 66, 22)) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

mw = Game_Box(600)
mw.draw()

            
