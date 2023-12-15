import pygame
from pygame.locals import *
from config import *



class Entidad(pygame.sprite.Sprite):
    def __init__(self, groups, pos_inicio: tuple, pie: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, golpeado: list, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(groups)
        self.imagen_pie = pie
        self.imagen_corer = corriendo
        self.imagen_salto = saltando
        self.imagen_golpe = golpe
        self.imagen_disparo = disparo
        self.imagen_royectil = proyectil
        self.imagen_caida = golpeado
        self.sprite_actual = 0
        self.image = self.imagen_pie[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos_inicio
        
        self.sonido_caminar = sonido_caminar
        self.sonido_golpeado = sonido_atacado
        self.sonido_ataque = sonido_ataque
        self.sonido_disparo = sonido_disparo
        self.sonido_proyectil = sonido_proyectil

        self.saltar = False
        self.mira_derecha = True
        self.golpear = False
        self.disparar = False
        self.caida = False

        self.ultima_actualizacion = pygame.time.get_ticks()
        self.velocidad = 5
        self.velocidad_caida = 3
        self.plataforma_suelo = 0
        self.actualizacion_salto = 0
        self.actualizacion_golpe = 0
        self.inicio_caida = 0


    def update(self):

        self.gravedad()



    def animacion(self, sprite_accion, tiempo_actual, cantidad, secuencia):
        if self.sprite_actual >= cantidad - 1:
            self.sprite_actual = 0
        if tiempo_actual - self.ultima_actualizacion >= secuencia:
            self.ultima_actualizacion = tiempo_actual
            self.sprite_actual += 1
            if self.mira_derecha:
                self.image = sprite_accion[self.sprite_actual]
            else:
                self.image = pygame.transform.flip(sprite_accion[self.sprite_actual], True, False)


    def gravedad(self):
          # si se pasa de la base vuelve a la base
        if self.rect.bottom >= ALTO:
            self.rect.bottom = ALTO
            self.velocidad_caida = 0
        #si la gravedad es mayor a 0 y no esta saltando
        if self.velocidad_caida > 0 and not self.saltar:
            self.rect.bottom += self.velocidad_caida
            if not self.caida and not self.golpear and not self.disparar:
                self.image = self.imagen_salto[1] if self.mira_derecha and not self.golpear else pygame.transform.flip(self.imagen_salto[1], True, False)
        #si no se paso de la base y esta saltando o la velocidad es mayor a 0
        elif self.saltar:
            self.rect.bottom -= self.velocidad
            if not self.caida and not self.golpear and not self.disparar:
                self.image = self.imagen_salto[0] if self.mira_derecha and not self.golpear else pygame.transform.flip(self.imagen_salto[1], True, False)


    def realizar_accion(self, tiempo_actual, imagen_ataque: list, accion: bool, sonido: pygame.mixer.Sound = None):
        if accion:
            self.animacion(imagen_ataque, tiempo_actual, len(imagen_ataque), len(imagen_ataque) * 20)
        if accion and sonido == pygame.mixer.Sound:
            try:
                sonido.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            

        
 
