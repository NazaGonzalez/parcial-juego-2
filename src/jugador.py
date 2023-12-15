import pygame
from pygame.locals import *
from random import *
from config import *
from personaje import *




class Jugador(Entidad, pygame.sprite.Sprite):
    def __init__(self, groups, pos_inicio: tuple, pie: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, golpeado: list, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(groups, pos_inicio, pie, corriendo, saltando, golpe, disparo, proyectil, golpeado, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil)
        self.puntuacion = 0
        self.poder_ataque = False
        self.vidas = 5
        self.sonido_salto = SALTO
        

    def update(self):
        keys = pygame.key.get_pressed()
        tiempo_actual = pygame.time.get_ticks()

        self.gravedad()
        # si esta saltando y el tiempo supera el tiempo de salto indicado
        if self.saltar and tiempo_actual - self.actualizacion_salto >= 500:
            self.velocidad_caida = 3
            self.saltar = False
            self.actualizacion_salto = tiempo_actual

        # animacion estandar
        if self.velocidad_caida == 0 and not self.saltar and not self.golpear and not self.disparar and not keys[K_RIGHT] and not keys[K_LEFT] and not keys[K_SPACE] and not self.caida:
            self.animacion(self.imagen_pie, tiempo_actual, len(self.imagen_pie), len(self.imagen_pie) * 30)
        # animacion derecha
        if keys[K_RIGHT] and self.rect.right <= ANCHO and not self.caida:
            self.mira_derecha = True
            self.rect.left += self.velocidad
            try:
                self.sonido_caminar.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            if self.velocidad_caida == 0 and not self.saltar and not self.golpear and not self.disparar and not self.caida:
                self.animacion(self.imagen_corer, tiempo_actual, len(self.imagen_corer), len(self.imagen_corer) * 25)
        # animacin izquierda        
        elif keys[K_LEFT] and self.rect.left >= 0 and not self.caida:
            self.mira_derecha = False
            self.rect.left -= self.velocidad
            try:
                self.sonido_caminar.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            if self.velocidad_caida == 0 and not self.saltar and not self.golpear and not self.disparar and not self.caida:
                self.animacion(self.imagen_corer, tiempo_actual, len(self.imagen_corer), len(self.imagen_corer) * 25)
        else:
            self.sonido_caminar.stop()



        # animacion salto
        if keys[K_SPACE] and not self.saltar and self.velocidad_caida == 0 and not self.caida:
            self.saltar = True
            self.actualizacion_salto = tiempo_actual
            try:
                self.sonido_salto.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")


        # golpe mele
        if keys[K_e] and not self.golpear and not self.disparar and not self.caida:
            self.golpear = True
            self.actualizacion_golpe = tiempo_actual
        self.realizar_accion(tiempo_actual, self.imagen_golpe, self.golpear, self.sonido_ataque)
        
        if self.golpear and tiempo_actual - self.actualizacion_golpe >= len(self.imagen_golpe) * FPS:
            self.actualizacion_golpe = tiempo_actual
            self.golpear = False


        # ataque de rango
        if keys[K_r] and not self.disparar and not self.golpear and self.poder_ataque and not self.caida:
            self.disparar = True
            self.actualizacion_golpe = tiempo_actual
        self.realizar_accion(tiempo_actual, self.imagen_disparo, self.disparar, self.sonido_disparo)
        
        if self.disparar and tiempo_actual - self.actualizacion_golpe >= len(self.imagen_disparo) * FPS:
            self.actualizacion_golpe = tiempo_actual
            self.disparar = False
            
        # caida
        self.realizar_accion(tiempo_actual, self.imagen_caida, self.caida)

        if self.caida and tiempo_actual - self.inicio_caida >= len(self.imagen_caida) * 100:
            self.inicio_caida = tiempo_actual
            self.caida = False







    
