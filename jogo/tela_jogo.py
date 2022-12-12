from settings import *
import pygame as pg
import sys
from lista_personagem import *
from personagens import Personagem
from cronometro import Cronometro
from tela_selecao import *
from tela_selecao2 import *
from ataques import *
from tiles import *




class Tela_jogo:
    
    def __init__(self,tela,id1,id2):

        global TILESIZE
        self.mapa = []
        self.Pedra = []
        self.Grama = []
        self.Agua = []
        self.Areia = []
        self.GramaTerreno = []
        self.PedraQuebravel = []

        pg.init()
        self.tela = tela
 
        self.seguir = True
        self.p1 = list_maincaracters[id1]
        self.p2 = list_maincaracters2[id2]

        self.posicao_x = self.p1.posicao[0]
        self.posicao_y = self.p1.posicao[1]

        self.posicao_x = self.p2.posicao[0]
        self.posicao_y = self.p2.posicao[1]


        self.cronometro = Cronometro()
        self.font = pg.font.SysFont(None, 50)
        self.cria_mapa()

        
    def rodar(self):
        while self.seguir:
            self.atualizar_movimento()
            self.draw()
            self.mudar_tela()
            self.movimento()
            


    def mudar_tela(self):
        
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit(0) 
                
        if  (self.cronometro.tempo_passado() > Settings.duracao_jogo):
            self.seguir = False
            Settings.tela_cont += 1
        if  (self.p1.vida <= 0) or (self.p2.vida <= 0):
            self.seguir = False
            Settings.tela_cont +=1
    
    def movimento(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        if(pg.key.get_pressed()[pg.K_w]):
            self.p1.mover_para_cima()
            
        elif(pg.key.get_pressed()[pg.K_s]) :
            self.p1.mover_para_baixo()

        else:
            self.p1.parar_y()

        if(pg.key.get_pressed()[pg.K_d]):
            self.p1.direita = True
            self.p1.esquerda = False
            self.p1.mover_para_direita()
            
        
        elif(pg.key.get_pressed()[pg.K_a]):
            self.p1.esquerda = True
            self.p1.direita = False
            self.p1.mover_para_esquerda()
        

        else:
            self.p1.parar_x() 
        
            
        
        
        if(pg.key.get_pressed()[pg.K_i]):
            self.p2.mover_para_cima()

        elif(pg.key.get_pressed()[pg.K_k]) :
            self.p2.mover_para_baixo()
        
        else:
            self.p2.parar_y()

        if(pg.key.get_pressed()[pg.K_l]) :
            self.p2.direita = True 
            self.p2.esquerda = False
            self.p2.mover_para_direita()


        elif(pg.key.get_pressed()[pg.K_j]) :
            self.p2.esquerda = True
            self.p2.direita = False
            self.p2.mover_para_esquerda() 

        

        else:
            self.p2.parar_x()
            

    def atualizar_movimento(self):
        self.p1.atualizar_posicao(self.mapa)
        self.p2.atualizar_posicao(self.mapa)


       
    def limite_tela(self):
        pass
    

    def cria_mapa(self):
        global TILESIZE
        global tilemap
        for fileira_index, fileira in enumerate(tilemap):
            for coluna_index, coluna in enumerate(fileira):
                x = coluna_index * TILESIZE
                y = fileira_index * TILESIZE
                if coluna == 1:
                    self.Pedra.append(Pedra((x,y)))
                if coluna == 2:
                    self.Grama.append(Grama((x,y)))
                if coluna == 3:
                    self.Agua.append(Agua((x,y)))
                if coluna == 4:
                    self.Areia.append(Areia((x,y)))
                if coluna == 5:
                    self.PedraQuebravel.append(PedraQuebravel((x,y)))
                if coluna == 6:
                    self.GramaTerreno.append(GramaTerreno((x,y)))

        self.mapa = [self.Pedra, self.Grama, self.Agua, self.Areia, self.PedraQuebravel, self.GramaTerreno]
        self.blocos_rigidos = [self.Pedra, self.PedraQuebravel]

    def desenha_mapa(self):
        for tipo_bloco_index, tipo_bloco in enumerate(self.mapa):
            for bloco_index, bloco in enumerate(tipo_bloco):
                self.mapa[tipo_bloco_index][bloco_index].desenha(self.tela)


    def draw(self):
  
        self.desenha_mapa()

        
        self.p1.desenha(self.tela) 
        self.p2.desenha(self.tela) 
       
        tempo = Settings.duracao_jogo - self.cronometro.tempo_passado()
        img = self.font.render(f'{tempo:.0f}',
                               True, Settings.cor_cronometro)
        self.tela.blit(img, (620 , Settings.screen_high * 0.10))

        life = self.p1.vida
        life2 = self.p2.vida
        img = self.font.render(f'{life:.0f}x{life2:.0f}',
                               True, Settings.cor_cronometro)
        self.tela.blit(img, (570 , 700))
    
    
        if(pg.key.get_pressed()[pg.K_e]):
            self.p1.classe1.ataque_melee(self.tela, self.p1, self.p2)
        if(pg.key.get_pressed()[pg.K_o]):
            self.p2.classe1.ataque_melee(self.tela, self.p2, self.p1)
        

        if(pg.key.get_pressed()[pg.K_q]):
            self.p1.classe2.especial(self.tela, self.p1, self.p2)
        if not(pg.key.get_pressed()[pg.K_q]):
            self.p1.classe2.reset()
            
        
        if(pg.key.get_pressed()[pg.K_u]):
            self.p2.classe2.especial(self.tela, self.p2, self.p1)
        if not(pg.key.get_pressed()[pg.K_u]):
            self.p2.classe2.reset()
        if  (pg.mouse.get_pressed()[0]) :
            position1 = pg.mouse.get_pos()
            self.p1.classe3.rodar_ataquemouse(self.tela, self.p2, position1)
        
        if  (pg.mouse.get_pressed()[0]) :
            position1 = pg.mouse.get_pos()
            self.p2.classe3.rodar_ataquemouse(self.tela, self.p1, position1)



        pg.display.flip()
