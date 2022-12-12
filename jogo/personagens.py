
from typing import Tuple
import pygame as pg
from settings import Settings
from lista_personagem import *

class Personagem:
    def __init__(self, posicao, sprite, velocidade, vida, classe1, dano, classe2, dano2, classe3, dano3):       #size
        
        self.velocidade = velocidade
        self.classe3 = classe3
        self.dano3 = dano3
        self.classe2 = classe2
        self.dano2 = dano2
        self.vida = vida
        self.dano = dano
        self.classe1 = classe1
        self.posicao = posicao
        self.muda_x = velocidade
        self.muda_y = velocidade
        self.velocidade_y = 0
        self.velocidade_x = 0
        self.hitbox = pg.Rect(self.posicao[0], self.posicao[1], 32, 50)
        self.sprite = sprite
        self.direita = False
        self.esquerda = False
        self.velocidade_reset = velocidade

    def mover_para_cima(self):
        self.velocidade_y = -self.velocidade

    def mover_para_baixo(self):
        self.velocidade_y = self.velocidade
    
    def mover_para_direita(self):
        self.velocidade_x = self.velocidade
    
    def mover_para_esquerda(self):
        self.velocidade_x = -self.velocidade

    def parar_x(self):
        self.velocidade_x = 0

    def parar_y(self):
        self.velocidade_y = 0


    def atualizar_posicao(self, mapa):
        x, y = self.posicao
        self.colisao_slow(mapa)
        novo_y = y + self.velocidade_y
        self.colisao("vertical", mapa)
        novo_x = x + self.velocidade_x
        self.colisao("horizontal", mapa)

        if ((novo_x >= 0) and ((novo_y + 30) <= Settings.screen_high)) and ((novo_y >= 0) and ((novo_x + 64) <= Settings.screen_width)):
            self.posicao = (novo_x, novo_y)


    def desenha(self, tela):

        self.hitbox = pg.Rect(self.posicao[0], self.posicao[1],  50, 50)
        #tela.blit(pg.flip(self.sprite,(self.x,self.y)))
        if not self.direita and not self.esquerda:
            tela.blit(self.sprite,(self.posicao))
        elif self.direita:
            tela.blit(self.sprite,(self.posicao))
        elif self.esquerda:
            tela.blit(pg.transform.flip(self.sprite,True, False), (self.posicao))
        
        

        
        #pg.draw.rect(tela,(0,255,0), self.hitbox, 2)

    def rect(self) -> Tuple[float, float, float, float]:
        """ retorna os dados da barra como os retangulos sao representados 
            no pg, i.e., como uma tupla do tipo (px, py, largura, altura).
        """
        return self.posicao + (Settings.largura_personagem, Settings.altura_personagem)

    def colisao(self, direcao, mapa):
        x, y = self.posicao
        blocos_colidiveis = []
        for tipo_bloco_index, tipo_bloco in enumerate(mapa):
            for bloco_index, bloco in enumerate(tipo_bloco):
                if tipo_bloco_index == 0:
                    blocos_colidiveis.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())
                if tipo_bloco_index == 4:
                    blocos_colidiveis.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())

        if direcao == 'horizontal':
            for index, bloco in enumerate(blocos_colidiveis):
                if self.hitbox.colliderect(blocos_colidiveis[index]):
                    if self.velocidade_x > 0:
                        self.velocidade = 0.05
                    if self.velocidade_x < 0:
                        self.velocidade = 0.05

        if direcao == 'vertical':
            for index, bloco in enumerate(blocos_colidiveis):
                if self.hitbox.colliderect(blocos_colidiveis[index]):
                    if self.velocidade_y > 0:
                        self.velocidade = 0.05
                    if self.velocidade_y < 0:
                        self.velocidade = 0.05
        self.posicao = (x, y)
                    
    def colisao_slow(self, mapa):
        blocos_especiais = []
        for tipo_bloco_index, tipo_bloco in enumerate(mapa):
            for bloco_index, bloco in enumerate(tipo_bloco):
                if tipo_bloco_index == 2:
                    blocos_especiais.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())
                if tipo_bloco_index == 3:
                    blocos_especiais.append(mapa[tipo_bloco_index][bloco_index].retorna_rect())
        if self.hitbox.collidelistall(blocos_especiais):
            self.velocidade = self.velocidade/2
            if self.velocidade < self.velocidade_reset/2:
                self.velocidade = self.velocidade_reset/2
        else:
            self.velocidade = self.velocidade_reset