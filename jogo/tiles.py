import pygame as pg
from settings import *


class Pedra:
    def __init__(self, pos):
        self.imagem = Settings.imagem_pedra
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect
    
class Agua:
    def __init__(self, pos):
        self.imagem = Settings.imagem_agua
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class Areia:
    def __init__(self, pos):
        self.imagem = Settings.imagem_areia
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class PedraQuebravel:
    def __init__(self, pos):
        self.imagem = Settings.imagem_pedra
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class Grama:
    def __init__(self, pos):
        self.imagem = Settings.imagem_grama
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect

class GramaTerreno:
    def __init__(self, pos):
        self.imagem = Settings.imagem_grama
        self.rect = self.imagem.get_rect(topleft = pos)

    def desenha(self, tela):
        tela.blit(self.imagem, self.rect)

    def retorna_rect(self):
        return self.rect 