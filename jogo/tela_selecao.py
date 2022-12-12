from settings import *
import pygame as pg
import sys


class Tela_selecao:
    def __init__(self,tela):
        pg.init()
        self.tela = tela
        self.background = img(r'./imagens/tela_selecao.png') 
        self.seguir = True
        self.large_ini = 475
        self.high_ini = 478     
        self.indmain = 0

    def rodar(self):
        while self.seguir:
            self.mudar_tela()
            self.draw()
            


    def mudar_tela(self):
        
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.seguir = False
                Settings.tela_cont -= 1 
                
            if (event.type == pg.KEYDOWN and event.key == pg.K_RETURN):
                self.seguir = False
                Settings.tela_cont += 1
            
            if (event.type == pg.KEYDOWN and event.key == pg.K_s) and self.indmain < 3:
                    self.indmain+=1
                    print(self.indmain)
            if (event.type == pg.KEYDOWN and event.key == pg.K_w) and self.indmain > 0:
                    self.indmain-=1
                    print(self.indmain)


    def escolha(self):
        print(self.indmain)
        return self.indmain
         




    def draw(self):
        self.tela.blit(self.background,(0,0))      
        #self.tela.fill((0,0,255))

        if self.indmain == 0:
            pg.draw.rect(self.tela, [255,0,0], [300,100,217,182], width=3)
        if self.indmain == 1:
            pg.draw.rect(self.tela, [255,0,0], [719,142,217,182], width=3)
        if self.indmain == 2:
            pg.draw.rect(self.tela, [255,0,0], [730,394,217,182], width=3)
        if self.indmain == 3:
            pg.draw.rect(self.tela, [255,0,0], [475,478,217,182], width=3)

        pg.display.flip()

