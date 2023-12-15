import pygame
from archivos import *
from pygame.locals import *
from random import *
from config import *
from personaje import *
from funciones import *
from jugador import *
from enemigo import *
from proyectil import *
from nivel import *
from menu import *


CAMBIO_DIR_ENEMIGOS = pygame.USEREVENT + 1
pygame.time.set_timer(CAMBIO_DIR_ENEMIGOS, 3000)
pygame.init()

class Nvl1(Nivel):
    def __init__(self, ventana: pygame.surface.Surface, fondo: pygame.surface.Surface, quieto: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, caida: list, pos_inicial: tuple, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(ventana, fondo, quieto, corriendo, saltando, golpe, disparo, proyectil, caida, pos_inicial, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil)
        pygame.init

        self.buggy1 = Buggy([self.sprites_enemigos], (450, 300), buggy_pie, buggy_correr, buggy_salto, buggy_ata1, buggy_disparo, buggy_proyectil, buggy_suelo, ZORO_DISPARA, ZORO_DISPARA, JUGADOR_CAMINA, JUGADOR_GOLPEADO, ZORO_PROYECTIL)
        self.buggy2 = Buggy([self.sprites_enemigos], (450, 500), buggy_pie, buggy_correr, buggy_salto, buggy_ata1, buggy_disparo, buggy_proyectil, buggy_suelo, ZORO_DISPARA, ZORO_DISPARA, JUGADOR_CAMINA, JUGADOR_GOLPEADO, ZORO_PROYECTIL)
        self.buggy2.mira_derecha = False
        self.buggy3 = Buggy([], (400, -100), buggy_pie, buggy_correr, buggy_salto, buggy_ata1, buggy_disparo, buggy_proyectil, buggy_suelo, ZORO_DISPARA, ZORO_DISPARA, JUGADOR_CAMINA, JUGADOR_GOLPEADO, ZORO_PROYECTIL)
        self.buggy3.ataque1 = False
        self.buggy3.ataque2 = True
        self.buggy3.mira_derecha = choice((True, False))

        self.plataforma1 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (350, 50)), (0, 500))
        self.plataforma2 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (350, 50)), (550, 500))
        self.plataforma3 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (250, 50)), (0, 300))
        self.plataforma4 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (250, 50)), (650, 300))
        self.plataforma5 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (200, 50)), (350, 100))

        self.imagen_final = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_buggy.png"), (tam_pantalla))
        self.sonido_final = pygame.mixer.Sound("./src/assets/sounds/franky.mp3")
        
        self.pantalla_final = PantallaFinal(self.pantalla, self.imagen_final)


    def jugando(self):
        self.en_pausa = False
        self.en_uso = True
        self.nombre_jugador = input("Ingrese su nombre: ")
        if self.sonido_habilitado:
            self.musica.play(-1)
        while self.en_uso:
            tiempo_actual = pygame.time.get_ticks()
            self.actualizar_temporizador(tiempo_actual)


            self.reloj.tick(FPS)
            # -------> detecta eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.en_uso = False
                if event.type == CAMBIO_DIR_ENEMIGOS and self.buggy3 in self.sprites_enemigos and len(
                        self.sprites_proyectil_enemigo) <= 4:
                    self.buggy3.mira_derecha = choice((True, False))
                    proyectil_buggy = Proyectil(buggy_proyectil, self.buggy3.mira_derecha, self.buggy3.rect.midbottom, 2, self.buggy3.sonido_proyectil)
                    self.sprites_proyectil_enemigo.add(proyectil_buggy)
                # -------> actualizar elementos
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        if not self.en_pausa:
                            pygame.mixer.pause()
                            self.tiempo_pausa = tiempo_actual
                            self.en_pausa = True
                        else:
                            self.musica.play(-1)
                            tiempo_pausa_transcurrido = tiempo_actual - self.tiempo_pausa
                            self.tiempo_inicio += tiempo_pausa_transcurrido
                            self.en_pausa = False

            if self.en_pausa:
                opcion_seleccionada = self.menu_pausa.elegir()
                self.musica.play(-1)
                tiempo_pausa_transcurrido = pygame.time.get_ticks() - self.tiempo_pausa
                self.tiempo_inicio += tiempo_pausa_transcurrido
                self.realizar_accion(opcion_seleccionada)
            else:
                # cargar 3er enemigo
                if not len(self.sprites_enemigos):
                    self.sprites_enemigos.add(self.buggy3)

                # disparo e impacto de proyectiles
                if self.jugador.disparar and len(self.sprites_proyectil_jugador) == 0:
                    proyectil_jugador = Proyectil(self.jugador.imagen_royectil, self.jugador.mira_derecha,self.jugador.rect.midbottom, 1, self.jugador.sonido_proyectil)
                    self.sprites_proyectil_jugador.add(proyectil_jugador)
                self.golpe_proyectil(self.sprites_proyectil_jugador, self.sprites_enemigos, self.jugador)
                self.golpe_proyectil(self.sprites_proyectil_enemigo, self.sprites_jugador, self.jugador, False)

                # ataque cuerpo a cuerpo
                for enemigo in self.sprites_enemigos:
                    if enemigo.ataque1 and not self.jugador.caida:
                        self.golpe_mele(self.sprites_enemigos, self.sprites_jugador, False)
                if self.jugador.golpear:
                    self.golpe_mele(self.sprites_jugador, self.sprites_enemigos)

                if self.jugador.vidas <= 0:
                    self.en_uso = False

            self.dibujar()
            self.actualizar()

        pygame.mixer.stop()

        if self.jugador.vidas <= 0 or len(self.sprites_enemigos) > 0:
            self.mostrar_pantalla_final(self.nombre_jugador, self.jugador.puntuacion, center_pantalla, False)
        else:
            self.completado = True
            nombre_record, puntuacion_record = self.pantalla_final.cargar_puntuacion_mas_alta()
            if self.jugador.puntuacion > puntuacion_record:
                self.pantalla_final.actualizar_puntuacion_mas_alta(self.nombre_jugador, self.jugador.puntuacion)
            self.mostrar_pantalla_final(nombre_record, puntuacion_record, center_pantalla, True)

        


        


    def cerrar(self):
        pass
    


    def golpe_proyectil(self, entidad: Proyectil, grupo_entidades: pygame.sprite.Group, jugador: Jugador, disparo_jugador: bool = True):
        item_colicion =  pygame.sprite.groupcollide(entidad, grupo_entidades, dokilla = True, dokillb = disparo_jugador)
        if disparo_jugador and item_colicion:
            jugador.puntuacion += 50
            for _ , enemigos_colisionados in item_colicion.items():
                for enemigo in enemigos_colisionados:
                    try:
                        enemigo.sonido_golpeado.play()
                    except pygame.error as e:
                        print(f"Error al reproducir sonido: {e}")
                    if enemigo == self.buggy3:
                        self.en_uso = False
        elif not disparo_jugador and item_colicion and not self.jugador.caida:
            jugador.puntuacion = 0
            jugador.vidas -= 1
            try:
                self.jugador.sonido_golpeado.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            self.jugador.caida = True
        

    def golpe_mele(self, atacante: pygame.sprite.Group, victima: pygame.sprite.Group, ataca_jugador: bool = True):
        item_colicion =  pygame.sprite.groupcollide(atacante, victima, dokilla = False, dokillb = ataca_jugador)
        if ataca_jugador and item_colicion:
            self.jugador.puntuacion += 50
            for _ , enemigos_colisionados in item_colicion.items():
                for enemigo in enemigos_colisionados:
                    try:
                        enemigo.sonido_golpeado.play()
                    except pygame.error as e:
                        print(f"Error al reproducir sonido: {e}")
                    if enemigo == self.buggy3:
                        self.en_uso = False
        elif not ataca_jugador and item_colicion and not self.jugador.caida:
            self.jugador.puntuacion = 0
            self.jugador.vidas -= 1
            try:
                self.jugador.sonido_golpeado.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            self.jugador.caida = True


    def mostrar_pantalla_final(self, nombre_record: str, puntos_record: int, centro_pantalla: tuple, victoria: bool):
        self.pantalla_final.mostrar(self.imagen_final, self.nombre_jugador, self.jugador.puntuacion, nombre_record, puntos_record, centro_pantalla, victoria)


    


nivel1_zoro = Nvl1(PANTALLA, fondo_lv1, zoro_pie, zoro_corriendo, zoro_salto, zoro_ata1, zoro_disparo, zoro_proyectil, zoro_caida, (0, ALTO), ZORO_DISPARA, ZORO_DISPARA, JUGADOR_CAMINA, JUGADOR_GOLPEADO, ZORO_PROYECTIL)
nivel1_luffy = Nvl1(PANTALLA, fondo_lv1, luffy_pie, luffy_corriendo, luffy_salto, luffy_ata1, luffy_disparo, luffy_proyectil, luffy_caida, (0, ALTO), LUFFY_GOLPE, LUFFY_DISPARO, JUGADOR_CAMINA, JUGADOR_GOLPEADO, LAW_DISPARA)






# pygame.transform.flip() girar superficie