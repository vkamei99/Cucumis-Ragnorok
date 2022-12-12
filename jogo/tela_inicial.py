from settings import *
import pygame as pg
import sys

class Tela_inicial:
    def __init__(self,tela):
        pg.init()
        self.tela = tela
        self.background = img(r'./imagens/tela_inicial.png')
        self.seguir = True
        
    def rodar(self):
        while self.seguir:
            self.mudar_tela()
            self.draw()


    def mudar_tela(self):
        
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit(0) 
                
            if (event.type == pg.KEYDOWN and event.key == pg.K_RETURN):
                self.seguir = False
                Settings.tela_cont += 1

    def draw(self):
        self.tela.blit(self.background,(0,0,Settings.screen_width,Settings.screen_high))    
        #self.tela.fill((0,0,0))
        pg.display.flip()
