from settings import Settings
from pygame import font
import pygame as pg
import sys
from tela_jogo import *

class Tela_vencedor:
    def __init__(self,tela,p1,p2):
        pg.init()
        self.p1 = p1
        self.p2 = p2
        self.tela = tela
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
                pass

    def draw(self):
   
        self.tela.fill((0,0,0))
        

        if self.p1.vida < self.p2.vida:
            self.p2.desenha(self.tela)
            txt = 'Vencedor Player 2'
            pg.font.init()

            fonte = pg.font.get_default_font()              ##### carrega com a fonte padrão
            fontesys = pg.font.SysFont(fonte, 60) 
            txttela = fontesys.render(txt, 1, (255,255,255))
            self.tela.blit(txttela,(400,100))

        elif self.p2.vida < self.p1.vida:
            self.p1.desenha(self.tela)
            txt = 'Vencedor Player 1'
            fonte = pg.font.get_default_font()              ##### carrega com a fonte padrão
            fontesys = pg.font.SysFont(fonte, 60) 
            txttela = fontesys.render(txt, 1, (255,255,255))
            self.tela.blit(txttela,(400,100))

        elif self.p1.vida == self.p2.vida:
            self.p1.desenha(self.tela)
            self.p2.desenha(self.tela)
            txt ='Empate'
            fonte = pg.font.get_default_font()              ##### carrega com a fonte padrão
            fontesys = pg.font.SysFont(fonte, 60) 
            txttela = fontesys.render(txt, 1, (255,255,255))
            self.tela.blit(txttela,(550,100))
        
        


        
        pg.display.flip()
        pg.display.update()
