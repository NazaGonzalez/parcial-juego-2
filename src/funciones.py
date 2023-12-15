import pygame
import os
import json
import sys
from pygame.locals import *
from config import *

ANCHO = 900
ALTO = 675

class HojaSprites():
    def __init__(self, imagen: pygame.surface.Surface, cantidad: int, ancho: int, alto: int):
        self.image = imagen
        self.frames = cantidad
        self.ancho = ancho
        self.alto = alto
        self.lista_imagenes = []

        
    def lista_animacion(self, escala: int = 1):

        self.image = pygame.transform.scale(self.image, (self.image.get_width() * escala, self.image.get_height() * escala))
        self.ancho *= escala
        self.alto *= escala

        for indice in range(self.frames):
            self.lista_imagenes.append(self.image.subsurface((indice * self.ancho, 0, self.ancho, self.alto)))
        return self.lista_imagenes
        
    

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, groups, imagen: pygame.surface.Surface, pos: tuple):
        super().__init__(groups)
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]



class Moneda(pygame.sprite.Sprite):
    def __init__(self, groups, imagen_moneda: list, pos_inicio: tuple):
        super().__init__(groups)
        self.imagen_moneda = imagen_moneda
        self.sprite_actual = 0
        self.image = self.imagen_moneda[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos_inicio
        self.ultima_actualizacion = pygame.time.get_ticks()

    
    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        self.animacion(self.imagen_moneda, tiempo_actual, len(self.imagen_moneda), len(self.imagen_moneda) * 25)


    def animacion(self, sprite_accion, tiempo_actual, cantidad, secuencia):
        if self.sprite_actual >= cantidad - 1:
            self.sprite_actual = 0
        if tiempo_actual - self.ultima_actualizacion >= secuencia:
            self.ultima_actualizacion = tiempo_actual
            self.sprite_actual += 1
            self.image = sprite_accion[self.sprite_actual]



class PantallaFinal:
    def __init__(self, ventana: pygame.surface.Surface, fondo: pygame.surface.Surface):
        self.fuente = pygame.font.SysFont("Comic Sans MS", 60)
        self.pantalla = ventana
        self.fondo = fondo



    def cargar_puntuacion_mas_alta(self):
        archivo_json = "puntuacion_mas_alta.json"
        if os.path.exists(archivo_json):
            with open(archivo_json, "r") as archivo:
                datos = json.load(archivo)
                return datos["nombre"], datos["puntos"]
        else:
            return None, 0


    def actualizar_puntuacion_mas_alta(self, nombre: str, puntuacion: int):
        archivo_json = "puntuacion_mas_alta.json"
        datos = {"nombre": nombre, "puntos": puntuacion}

        with open(archivo_json, "w") as archivo:
            json.dump(datos, archivo)


    def mostrar(self, imagen: pygame.surface.Surface, nombre: str, puntos: int, nombre_record: str, puntos_record: int, centro_pantalla: tuple, victoria: bool, color_fuente: tuple = (155, 0, 0)):
        self.eligiendo = True
        while self.eligiendo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.eligiendo = False
            self.dibujar(imagen, nombre, puntos, nombre_record, puntos_record, centro_pantalla, victoria, color_fuente)
            pygame.display.flip()


        pygame.display.flip()


    
    def dibujar(self,imagen: pygame.surface.Surface, nombre: str, puntos: int, nombre_record: str, puntos_record: int, centro_pantalla: tuple, victoria: bool = True, color_fuente: tuple = (0, 0, 0)):
        self.pantalla.blit(imagen, (0, 0))  # Rellenar la pantalla con un color (puedes cambiarlo)
        
        # Añadir aquí la lógica para dibujar el mensaje en la pantalla
        # Por ejemplo:
        if victoria:
            self.crear_cartel("¡Felicidades " + nombre + ", has ganado!", (centro_pantalla[0], centro_pantalla[1] // 3), color_fuente)
            self.crear_cartel("has conseguido " + str(puntos) + " puntos", (centro_pantalla[0], centro_pantalla[1] // 2), color_fuente)
            self.crear_cartel("el recor es de " + nombre_record, (centro_pantalla[0], centro_pantalla[1]), color_fuente)
            self.crear_cartel("consiguio " + str(puntos_record) + " puntos", (centro_pantalla[0], centro_pantalla[1] * 1.5), color_fuente)
        else:
            self.crear_cartel("Ya perdiste ¡Volve a probar!", (centro_pantalla))

        # ... (agrega aquí cualquier otro elemento que quieras mostrar)

        pygame.display.flip()  # Actualizar la pantalla


    def crear_cartel (self, texto: str, coordenadas: tuple, color_fuente: tuple = (0, 0, 0)):

        sup_texto = self.fuente.render(texto, True, color_fuente)
        rect_texto = sup_texto.get_rect()
        rect_texto.center = coordenadas
        self.pantalla.blit(sup_texto, rect_texto)


    





