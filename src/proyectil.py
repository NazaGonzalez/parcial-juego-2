import pygame
from pygame.locals import *
from random import *
from config import *
from personaje import *
from funciones import *


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, imagen_proyectil: list, apunta_derecha: bool, pos_inicio: tuple, tipo_proyectil: int = 1, sonido: pygame.mixer.Sound = None):
        super().__init__()
        self.imagen_proyectil = imagen_proyectil
        self.sprite_actual = 0
        self.image = self.imagen_proyectil[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.apunta_derecha = apunta_derecha
        self.apunta_abajo = True
        self.rect.midbottom = pos_inicio
        self.rect.x = self.rect.x + 50 if self.apunta_derecha else self.rect.x - 50
        self.ultima_actualizacion = pygame.time.get_ticks()
        self.velocidad = 4
        self.tipo = tipo_proyectil
        self.sonido = sonido



    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        self.animacion(self.imagen_proyectil, tiempo_actual, len(self.imagen_proyectil), len(self.imagen_proyectil) * 15)
        if self.sonido:
            self.sonido.play()
        if self.tipo == 1:
            self.rect.left = self.rect.x + self.velocidad if self.apunta_derecha else  self.rect.x - self.velocidad
            if (self.apunta_derecha and self.rect.right >= ANCHO) or (not self.apunta_derecha and self.rect.left <= 0):
                self.kill()
        elif self.tipo == 2:
            self.rect.left = self.rect.x + self.velocidad if self.apunta_derecha else  self.rect.x - self.velocidad
            self.rect.top = self.rect.y + self.velocidad if self.apunta_abajo else  self.rect.y - self.velocidad
            
            if self.apunta_derecha and self.rect.right >= ANCHO:
                self.apunta_derecha = False
            if not self.apunta_derecha and self.rect.left <= 0:
                self.apunta_derecha = True 
            if self.apunta_abajo and self.rect.bottom >= ALTO:
                self.apunta_abajo = False 
            if not self.apunta_abajo and self.rect.top <= 0:
                self.apunta_abajo = True
        
        elif self.tipo == 3:
            self.rect.y += self.velocidad
            if self.rect.top >= ALTO:
                self.kill()
            



    def animacion(self, sprite_accion, tiempo_actual, cantidad, secuencia):
        if self.sprite_actual >= cantidad - 1:
            self.sprite_actual = 0
        if tiempo_actual - self.ultima_actualizacion >= secuencia:
            self.ultima_actualizacion = tiempo_actual
            self.sprite_actual += 1
            if self.apunta_derecha:
                self.image = sprite_accion[self.sprite_actual]
            else:
                self.image = pygame.transform.flip(sprite_accion[self.sprite_actual], True, False)


    