import pygame as pg

TILESIZE = 32
PLAYER_LAYER = 3
GROUND_LAYER = 1
BLOCK_LAYER = 2
QUEBRAVEL = False

tilemap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,4,4,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,6,6,6,6,2,2,2,2,4,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,6,5,5,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,6,5,5,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,6,5,5,6,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,6,5,5,6,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,5,5,6,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,5,5,6,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,1],
[1,2,2,2,2,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,3,3,2,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class Settings:
    screen_width = 1280
    screen_high = 768
    tela_cont = 1
    cor_tela1 = (255, 255, 255)
    largura_personagem = screen_width * 0.5
    altura_personagem = screen_high * 0.5
    personagem_size = ((largura_personagem,altura_personagem))
    screen_size = (screen_width,screen_high)
    cor_cronometro = (0, 0, 0)
    tamanho_cronometro = 450
    duracao_jogo = 120
    cor_bola_de_pantano = (112, 84, 62)
    cor_tiro = (255, 0, 0)
    contador = 1
    imagem_agua = pg.image.load("agua.png")
    imagem_pedra = pg.image.load("pedra.png")
    imagem_areia = pg.image.load("areia.png")
    imagem_grama = pg.image.load("grama.png")
    
    #pg.mixer.init()
    #musica = pg.mixer.Sound(r'./music/ds3.wav')
    #pg.mixer.Sound.set_volume(musica, .5)
    


def img(diretorio):
    return pg.image.load(diretorio)
def scale(png, escala):
    return pg.transform.scale(png, escala)



