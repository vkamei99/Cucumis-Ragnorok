import pygame as pg
from settings import *
from pathlib import Path
from personagens import Personagem
from ataques import *


# perso1 = scale(img(r'./imagens/boto.png'), (87, 87))
# perso2 = scale(img(r'./imagens/Mula_Sem_Cabeca.png'), (87, 87))
# perso3 = scale(img(r'./imagens/boitata.png'),(120,120))
# perso4 = scale(img(r'./imagens/brasil.png'),(120,120))

# list_maincaracters = [(perso1,perso2,perso3,perso4)]

caracters_size = (60,60)
basico = Ataque_basico()
cura = Ataque_cura()
mouse = Ataque_mouse()
tiro = Ataque_projetil()
tiro2 = Ataque_projetil()
vazio = Ataque_vazio()
vazio_mouse = Ataque_vaziomouse()
'''slow = Ataque_stunned()'''

boto = Personagem((80,Settings.screen_high//2.7),scale(img(r'./imagens/pers/boto.png'), (caracters_size)),1, 612, basico, 0.2, tiro, 2, vazio_mouse, 3)
mula = Personagem((80,Settings.screen_high//2.7),scale(img(r'./imagens/pers/Mula_Sem_Cabeca.png'), (caracters_size)), 1.5, 700, basico, 0.6, vazio, 3, mouse, 0.03)
saci = Personagem((80,Settings.screen_high//2.7),scale(img(r'./imagens/pers/Saci.png'), (caracters_size)),1, 700, basico, 0.3, cura, 0.1, vazio_mouse, 3)
boitata = Personagem((80,Settings.screen_high//2.7),scale(img(r'./imagens/pers/Boitata.png'), (caracters_size)),0.5, 1000, basico, 5, vazio, 3, vazio_mouse, 3)

boto2 = Personagem((Settings.screen_width-140,Settings.screen_high//1.8),scale(img(r'./imagens/pers/boto.png'), (caracters_size)),1, 612, basico, 0.2, tiro, 2, vazio_mouse, 3)
mula2 = Personagem((Settings.screen_width-140,Settings.screen_high//1.8),scale(img(r'./imagens/pers/Mula_Sem_Cabeca.png'), (caracters_size)),1.5, 700, basico, 0.6, vazio, 3, mouse, 0.03)
saci2 = Personagem((Settings.screen_width-140,Settings.screen_high//1.8),scale(img(r'./imagens/pers/Saci.png'), (caracters_size)),1, 700, basico, 0.3, cura, 0.1, vazio_mouse, 3)
boitata2 = Personagem((Settings.screen_width-140,Settings.screen_high//1.8),scale(img(r'./imagens/pers/Boitata.png'), (caracters_size)),0.5, 1000, basico, 0.5, vazio, 3, vazio_mouse, 3)

list_maincaracters = [boto, mula, saci, boitata]
list_maincaracters2 = [boto2, mula2, saci2, boitata2]
'''caminho = Path(__file__)
imagem = caminho.parent.parent / 'imagens' / 'pers'
listsec = []
for i in imagem.glob('*.png'):
    listsec.append(pg.image.load(i))'''
