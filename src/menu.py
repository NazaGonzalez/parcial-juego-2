import pygame
from pygame.locals import *
from config import *
from funciones import *


import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuraciones


botones = HojaSprites(pygame.image.load("./src/assets/images/botones_cuadrados100,100.png").convert_alpha(), 11, 100, 100).lista_animacion(0.5)
botones2 = HojaSprites(pygame.image.load("./src/assets/images/botones_rect110,50.png").convert_alpha(), 16, 110, 50).lista_animacion()

tecla_spc = [pygame.transform.scale(pygame.image.load("./src/assets/images/boton_spc140,80.png"), (140, 80))]
tecla_flechas = HojaSprites(pygame.image.load("./src/assets/images/botones_flechas150,150.png").convert_alpha(), 2, 150, 150).lista_animacion(0.5)
tecla_habilidades = HojaSprites(pygame.image.load("./src/assets/images/botones_habilidades75,75.png").convert_alpha(), 2, 75, 75).lista_animacion()

botones_personajes = HojaSprites(pygame.image.load("./src/assets/images/select_pj300,340.png").convert_alpha(), 8, 300, 340).lista_animacion(0.8)
botones_nivel = HojaSprites(pygame.image.load("./src/assets/images/carteles_niveles180,160.png").convert_alpha(), 3, 180, 160).lista_animacion(0.5)

fondo_menu_pj = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_menu_pj.jpg"), (tam_pantalla))
fondo_menu = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_menu.jpg"), (tam_pantalla))
fondo_pausa_nv1 = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_buggy.png"), (tam_pantalla))
fondo_pausa_nv2 = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_almirantes.jpg"), (tam_pantalla))
fondo_pausa_nv3 = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_kaido.jpg"), (tam_pantalla))


# Clase para representar un botón
class Boton(pygame.sprite.Sprite):
    def __init__(self, posicion: tuple, imagenes_botones: list, imgen_deseada: int, imagen_activado: int, accion_boton = 0):
        super().__init__()
        self.imagen_boton = imagenes_botones
        self.sprite_normal = imgen_deseada
        self.sprite_acti = imagen_activado
        self.image = self.imagen_boton[self.sprite_normal]
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.accion = accion_boton

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.imagen_boton[self.sprite_acti]
        else:
            self.image = self.imagen_boton[self.sprite_normal]
        


# Clase para representar un menú que contiene botones
            
class Menu(pygame.sprite.Sprite):
    def __init__(self, ventana: pygame.surface.Surface, fondo: pygame.surface.Surface, posicion: tuple = (0, 0), audio: str = "", *botones):
        super().__init__()
        self.fondo = fondo
        self.posicion = posicion
        self.eligiendo = True
        self.pantalla = ventana
        self.botones = pygame.sprite.Group(botones)
        self.rect = pygame.Rect(0, 0, 0, 0)
        for boton in botones:
            self.rect.union_ip(boton.rect)

        self.musica = pygame.mixer.Sound(audio)
        self.sonido_habilitado = True
        


    def elegir(self):
        if self.sonido_habilitado:
            self.musica.play() 
        opcion_seleccionada = None
        while self.eligiendo:
            pygame.time.Clock().tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for boton in self.botones:
                        if boton.rect.collidepoint(event.pos):
                            opcion_seleccionada = boton.accion
                            self.eligiendo = False

            self.update()
            self.dibujar()
            pygame.display.flip()
        pygame.mixer.stop()
        # Reiniciar la variable eligiendo al final del bucle
        self.eligiendo = True
        return opcion_seleccionada

    def dibujar(self):
        self.pantalla.blit(self.fondo, self.posicion)
        self.botones.update()
        self.botones.draw(self.pantalla)



boton_play = Boton((150, 225), botones2, 4, 4, "niveles")
boton_options = Boton((150, 300), botones2, 5, 5, "opciones")
boton_quit = Boton((150, 375), botones2, 9, 9, "salir")
boton_mute = Boton((850, 600), botones, 3, 3, "sonido")

boton_spc = Boton((375, 350), tecla_spc, 0, 0, "_")
boton_flecha_d = Boton((700, 350), tecla_flechas, 1, 1, "_")
boton_flecha_i = Boton((600, 350), tecla_flechas, 0, 0, "_")
boton_e = Boton((200, 350), tecla_habilidades, 0, 0, "_")
boton_r = Boton((100, 350), tecla_habilidades, 1, 1, "_")
boton_atras = Boton((5, 5), botones, 1, 1, "atras")

boton1 = Boton((100, 295), botones_nivel, 0, 0)
boton2 = Boton((400, 295), botones_nivel, 1, 1)
boton3 = Boton((700, 295), botones_nivel, 2, 2)

boton_luffy1 = Boton((25, 50), botones_personajes, 0, 4, "luffy1")
boton_zoro = Boton((25, 350), botones_personajes, 1, 5, "zoro")
boton_luffy2 = Boton((325, 50), botones_personajes, 0, 4, "luffy2")
boton_jimbei = Boton((325, 350), botones_personajes, 2, 6, "jimbei")
boton_luffy3 = Boton((625, 50), botones_personajes, 0, 4, "luffy3")
boton_law = Boton((625, 350), botones_personajes, 3, 7, "law")



menu_juegos = Menu(PANTALLA, fondo_menu_pj, (0, 0), "src/assets/sounds/one-piece-luffy.mp3", boton_luffy1, boton_zoro, boton_luffy2, boton_jimbei, boton_luffy3, boton_law, boton1, boton2, boton3, boton_atras)
menu_principal = Menu(PANTALLA, fondo_menu, (0, 0), "src/assets/sounds/one_pce1.mp3", boton_play, boton_options, boton_quit)
menu_ajustes = Menu(PANTALLA, fondo_menu, (0, 0), "src/assets/sounds/one_pce1.mp3", boton_spc, boton_flecha_d, boton_flecha_i, boton_e, boton_r, boton_atras, boton_mute)


    

