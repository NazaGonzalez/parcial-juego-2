import pygame
from pygame.locals import *
from random import *
from config import *
from personaje import *
from funciones import *



class Buggy(Entidad, pygame.sprite.Sprite):
    def __init__(self, groups, pos_inicio: tuple, pie: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, golpeado: list, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(groups, pos_inicio, pie, corriendo, saltando, golpe, disparo, proyectil, golpeado, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil)
        self.cambio_dir = 500
        self.ataque1 = True
        self.ataque2 = False
        

    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        
        self.gravedad()
        
        #cambio direccion enemigos
        if self.rect.right >= ANCHO:
            self.mira_derecha = False
        if self.rect.left <= 0:
            self.mira_derecha = True


        # animacion estandar
        if self.velocidad_caida == 0 and not self.saltar and not self.ataque2:
            self.animacion(self.imagen_pie, tiempo_actual, 3, 175)
        # animacion derecha
        if self.mira_derecha and self.rect.right < ANCHO and self.ataque1:
            self.rect.left += self.velocidad
            if not self.saltar:
                self.animacion(self.imagen_golpe, tiempo_actual, 11, 150)
        # animacin izquierda        
        if not self.mira_derecha and self.rect.left > 0 and self.ataque1:
            self.rect.left -= self.velocidad
            if not self.saltar:
                self.animacion(self.imagen_golpe, tiempo_actual, 11, 150)


        if self.ataque2 and self.velocidad_caida == 0 and not self.saltar:
            self.animacion(self.imagen_disparo, tiempo_actual, len(self.imagen_disparo), len(self.imagen_disparo) * 50)
            self.sonido_disparo.play()



    def gravedad(self):
        # si se pasa de la base vuelve a la base
        if not self.ataque1:
            if self.rect.bottom >= ALTO:
                self.rect.bottom = ALTO
                self.velocidad_caida = 0
            #si la gravedad es mayor a 0 y no esta saltando
            if self.velocidad_caida > 0 and not self.saltar:
                self.rect.bottom += self.velocidad_caida
                self.image = self.imagen_salto[1] if self.mira_derecha else pygame.transform.flip(self.imagen_salto[1], True, False)












class Almirante(Entidad, pygame.sprite.Sprite):
    def __init__(self, groups, pos_inicio: tuple, pie: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, golpeado: list, posicion_secundaria: tuple, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(groups, pos_inicio, pie, corriendo, saltando, golpe, disparo, proyectil, golpeado, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil)
        self.vidas = 2
        self.segunda_pos = posicion_secundaria
        self.cambio_dir = 500


    def update(self):
        tiempo_actual = pygame.time.get_ticks()

        self.gravedad()

        
        self.realizar_accion(tiempo_actual, self.imagen_disparo, self.disparar, self.disparar)
        if self.disparar and tiempo_actual - self.actualizacion_golpe >= len(self.imagen_disparo) * FPS:
            self.actualizacion_golpe = tiempo_actual
            self.disparar = False

        self.realizar_accion(tiempo_actual, self.imagen_golpe, self.golpear, self.sonido_ataque)
        if self.golpear and tiempo_actual - self.actualizacion_golpe >= len(self.imagen_golpe) * FPS:
            self.actualizacion_golpe = tiempo_actual
            self.golpear = False

        if self.velocidad_caida == 0 and not self.saltar and not self.golpear and not self.disparar and not self.caida:
            self.animacion(self.imagen_pie, tiempo_actual, len(self.imagen_pie), len(self.imagen_pie) * 30)


        self.realizar_accion(tiempo_actual, self.imagen_caida, self.caida, self.sonido_golpeado)
        if self.caida and tiempo_actual - self.inicio_caida >= len(self.imagen_caida) * 100:
            self.inicio_caida = tiempo_actual
            self.caida = False

        if self.vidas <= 0:
            self.kill()

        
    def actualizar_direccion(self, jugador_x):
        if jugador_x > self.rect.x:
            self.mira_derecha = True
        elif jugador_x < self.rect.x:
            self.mira_derecha = False




class Kaido(Entidad, pygame.sprite.Sprite):
    def __init__(self, groups, pos_inicio: tuple, pie: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, golpeado: list, posicion_secundaria: tuple, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(groups, pos_inicio, pie, corriendo, saltando, golpe, disparo, proyectil, golpeado, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil)
        self.vidas = 4
        self.segunda_pos = posicion_secundaria
        self.cambio_dir = 500


    def update(self):
        tiempo_actual = pygame.time.get_ticks()

        self.gravedad()

        
        self.realizar_accion(tiempo_actual, self.imagen_disparo, self.disparar, self.sonido_disparo)
        if self.disparar and tiempo_actual - self.actualizacion_golpe >= len(self.imagen_disparo) * FPS:
            self.actualizacion_golpe = tiempo_actual
            self.disparar = False

        self.realizar_accion(tiempo_actual, self.imagen_golpe, self.golpear, self.sonido_ataque)
        if self.golpear and tiempo_actual - self.actualizacion_golpe >= len(self.imagen_golpe) * FPS:
            self.actualizacion_golpe = tiempo_actual
            self.golpear = False


        if self.velocidad_caida == 0 and not self.saltar and not self.golpear and not self.disparar and not self.caida:
            self.animacion(self.imagen_pie, tiempo_actual, len(self.imagen_pie), len(self.imagen_pie) * 30)


        self.realizar_accion(tiempo_actual, self.imagen_caida, self.caida, self.sonido_golpeado)
        if self.caida and tiempo_actual - self.inicio_caida >= len(self.imagen_caida) * 100:
            self.inicio_caida = tiempo_actual
            self.caida = False

        if self.vidas <= 0:
            self.kill()

        


        
    def actualizar_direccion(self, jugador_x):
        if jugador_x > self.rect.x:
            self.mira_derecha = True
        elif jugador_x < self.rect.x:
            self.mira_derecha = False

    def caminar(self, tiempo_actual):
        if self.mira_derecha and not self.disparar and not self.golpear:
            self.rect.x += self.velocidad
            self.animacion(self.imagen_corer, tiempo_actual, len(self.imagen_corer), len(self.imagen_corer) * 25)
        elif not self.mira_derecha and not self.disparar and not self.golpear:
            self.rect.x -= self.velocidad
            self.animacion(self.imagen_corer, tiempo_actual, len(self.imagen_corer), len(self.imagen_corer) * 25)
        self.sonido_caminar.play()
