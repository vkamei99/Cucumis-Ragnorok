from settings import Settings
import sys
import pygame as pg
from cronometro import Cronometro
import time



class Ataque_mouse:
    def __init__(self):
        pass 
    def rodar_ataquemouse(self, tela, bobo, posicao):
        
        position = posicao   
        position2 = (bobo.posicao[0] + 30, bobo.posicao[1] + 30)
        distancia = ((position[0]-position2[0])**2 + (position[1]-position2[1])**2)**0.5
        pg.draw.circle(
                    tela,
                    (255, 0, 0),
                    position,
                    60, width=4)
        pg.display.flip()

        if distancia <= 80:
            bobo.vida -= bobo.dano
class Ataque_vaziomouse:
    def __init__(self):
        pass
    def rodar_ataquemouse(self,tela, bobo, posicao):
        pass
    
        
class Ataque_basico:
    def __init__(self):
        pass
    def ataque_melee(self,tela, agressor, bobo):
        position1 = (agressor.posicao[0] + 30, agressor.posicao[1] + 30)
        position2 = (bobo.posicao[0] + 30, bobo.posicao[1] + 30)
        distancia = ((position1[0]-position2[0])**2 + (position1[1]-position2[1])**2)**0.5
        
        pg.draw.circle(
                    tela,
                    (255, 0, 0),
                    position1,
                    50, width=3)
        pg.display.flip()

        if distancia <= 80:
            bobo.vida -= agressor.dano

class Ataque_cura:
    def __init__(self):
        pass
    def especial(self, tela, agressor, bobo):
        self.bobo = bobo
        position1 = (agressor.posicao[0] + 30, agressor.posicao[1] + 30)

        pg.draw.circle(
                tela,
                (0, 255, 0),
                position1,
                50, width=3)
        pg.display.flip()
        if agressor.vida <700:
            agressor.vida += agressor.dano2
    def atualizacao(self, nulo, nulo2):
        pass
    def reset(self):
        pass


class Ataque_vazio:
    def __init__(self):
        pass
    def especial(self,tela, agressor, bobo):
        pass
    def atualizacao(self):
        self
    def reset(self):
        pass

class Ataque_projetil:
    def __init__(self) :
        self.velocidade = 19
        self.list = []

    def especial(self, tela, agressor, bobo):
        if agressor.posicao[0]<= bobo.posicao[0]:
            projetil = Projetil(self.velocidade, (243, 177, 223), agressor.posicao)
        else:
            projetil = Projetil(-self.velocidade, (243, 177, 223), agressor.posicao)
        self.list.append(projetil)
        for projetil in self.list:
            projetil.rodar(tela)
            distancia = ((projetil.posicao[0]-bobo.posicao[0])**2 + (projetil.posicao[1]-(bobo.posicao[1]+30))**2)**0.5
            if distancia <= 30:
                bobo.vida -= agressor.dano2
                self.list.remove(projetil)
        pg.display.flip()


    
    
        

    def reset(self):
        self.list = []


class Projetil:
    def __init__(self, velocidade, cor, posicao):
        self.cor = cor
        self.velocidade = velocidade
        self.posicao = posicao
        
    def tiro(self):
        x,y = self.posicao
        x += self.velocidade
        self.posicao = (x, y)

    def desenha(self, tela):
        if 0<= self.posicao[0] and self.posicao[0] <= Settings.screen_width:
            pg.draw.circle(
                    tela,
                    (255, 0 ,0),
                    (self.posicao),
                    5, width=3)
    
    def rodar(self, tela):
        self.tiro()
        self.desenha(tela)


'''class Ataque_stunned:
    def __init__(self):
        pass
    def especial(self,tela, agressor, bobo):
        position1 = (agressor.posicao[0] + 30, agressor.posicao[1] + 30)
        position2 = (bobo.posicao[0] + 30, bobo.posicao[1] + 30)
        distancia = ((position1[0]-position2[0])**2 + (position1[1]-position2[1])**2)**0.5
        
        pg.draw.circle(
                    tela,
                    (255, 255, 0),
                    position1,
                    50, width=3)
        pg.display.flip()
        y = bobo.velocidade

        if distancia <= 50:
            bobo.vida -= agressor.dano
            bobo.velocidade = 0
        x = 0
        while x<4:
            time.sleep(1)
            bobo.velocidade = y
        
    def atualizacao(self, nulo, nulo2):
        pass
    def reset(self):
        pass'''


    





