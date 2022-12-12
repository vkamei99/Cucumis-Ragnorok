from settings import *
import pygame as pg
import sys
from tela_inicial import Tela_inicial
from tela_historia import Tela_historia
from tela_selecao import Tela_selecao
from tela_jogo import Tela_jogo
from tela_vencedor import Tela_vencedor
from tela_historia_1 import Tela_historia_1
from pygame import mixer
from tela_selecao2 import Tela_selecao2
from cronometro  import Cronometro

pg.mixer.init()

class Screen:

    def __init__(self):
        pg.init()
        pg.display.set_caption('Cucumis Ragnarok')
        icon = img(r'./imagens/brasil.png')
        pg.display.set_icon(icon)
        self.cronometro = Cronometro()

        self.tela = pg.display.set_mode((Settings.screen_size))

    def rodar(self):
        
        while True:
            self.selec_screen()
        

    def selec_screen(self):
        for event in pg.event.get():

            if Settings.tela_cont == 1:
                
                ato = Tela_inicial(self.tela)
                #Settings.musica.play()
                ato.rodar()

                
            if Settings.tela_cont == 2:
                
                ato = Tela_historia(self.tela)
                ato.rodar()

            if Settings.tela_cont == 3:
                
                ato = Tela_historia_1(self.tela)
                ato.rodar()
    
            if Settings.tela_cont == 4:
                
                ato = Tela_selecao(self.tela)
                ato.rodar()
                id1 = ato.escolha()

            if Settings.tela_cont == 5:
                
                ato = Tela_selecao2(self.tela)
                ato.rodar()
                id2 = ato.escolha()

            if Settings.tela_cont == 6:
                
                ato = Tela_jogo(self.tela,id1,id2)
                ato.rodar()

            if Settings.tela_cont == 7:
                
                ato = Tela_vencedor(self.tela,ato.p1,ato.p2)
                ato.rodar()

    # def criar_tela(self):
    #     screen1 = pg.display.set_mode(self.screen_size)
    #     screen1.fill((self.cor_tela))
    #     pg.display.flip()

    def desenhar_cronometro(self, tela):
        tempo = Settings.duracao_jogo - self.cronometro.tempo_passado()
        img = self.font.render(f'{tempo:.0f}',
                               True, Settings.cor_cronometro)
        tela.blit(img, (640, Settings.screen_high * 0.15))
        
    
