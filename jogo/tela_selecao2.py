
from settings import *
import pygame as pg
import sys


class Tela_selecao2:
    def __init__(self,tela):
        pg.init()
        self.tela = tela
        self.background = img(r'./imagens/tela_selecao.png')
        self.seguir = True
        self.large_ini = 10
        self.high_ini = 10       
        self.indmain2 = 0

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
            
            if (event.type == pg.KEYDOWN and event.key == pg.K_s) and self.indmain2 < 3:
                    self.indmain2+=1
                    print(self.indmain2)
            if (event.type == pg.KEYDOWN and event.key == pg.K_w) and self.indmain2 > 0:
                    self.indmain2-=1
                    print(self.indmain2)
    def escolha(self):
        return self.indmain2
            
         




    def draw(self):
        self.tela.blit(self.background,(0,0))      
        #self.tela.fill((255,255,255))
        if self.indmain2 == 0:
            pg.draw.rect(self.tela, [0,0,255], [300,100,217,182], width=3)
        if self.indmain2 == 1:
            pg.draw.rect(self.tela, [0,0,255], [719,142,217,182], width=3)
        if self.indmain2 == 2:
            pg.draw.rect(self.tela, [0,0,255], [730,394,217,182], width=3)
        if self.indmain2 == 3:
            pg.draw.rect(self.tela, [0,0,255], [475,478,217,182], width=3)

        pg.display.flip()

    