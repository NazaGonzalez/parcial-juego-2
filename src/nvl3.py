import pygame
from archivos import *
from pygame.locals import *
from config import *
from personaje import *
from funciones import *
from jugador import *
from enemigo import *
from proyectil import *
from nivel import *


CAMBIO_DIR_ENEMIGOS = pygame.USEREVENT + 1
pygame.time.set_timer(CAMBIO_DIR_ENEMIGOS, 3000)

class Nvl3(Nivel):
    def __init__(self, ventana: pygame.surface.Surface, fondo: pygame.surface.Surface, quieto: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, caida: list, pos_inicial: tuple, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        super().__init__(ventana, fondo, quieto, corriendo, saltando, golpe, disparo, proyectil, caida, pos_inicial, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil)
        pygame.init
        self.tiempo_ataques = 5000
        self.actualizacion_ataques = 0

        self.kaido1 = Kaido([], (10, -100), kaido2_pie, kaido1_corriendo, kaido1_salto, kaido2_ata1, kaido2_disparo, kaido2_proyectil, kaido1_caida, (350, 100), KAITO_ATAC, ALMIRANTE_DISPARA, KAIDO_CAMINA, KAIDO_GOLPEADO, ALMIRANTE_DISPARA)
        self.kaido2 = Kaido([], (10, ALTO), kaido1_corriendo, kaido1_corriendo, kaido1_salto, kaido1_ata1, kaido1_disparo, kaido1_proyectil, kaido1_caida, (750, ALTO), KAITO_ATAC, ALMIRANTE_DISPARA, KAIDO_CAMINA, KAIDO_GOLPEADO, PROYECTIL_KAIDO)
        self.kaido2.velocidad = 1
        self.kaido3 = Kaido([self.sprites_enemigos], (300, 100), kaido3_pie,  kaido3_pie,  kaido3_pie,  kaido3_pie,  kaido3_pie, kaido3_proyectil,  kaido3_pie, (400, 100), KAITO_ATAC, ALMIRANTE_DISPARA, KAIDO_CAMINA, KAIDO_GOLPEADO, PROYECTIL_KAIDO)

        self.plataforma1 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (450, 50)), (220, 150))
        self.plataforma2 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (300, 50)), (0, 400))
        self.plataforma3 = Plataforma([self.sprites_plataformas], pygame.transform.scale(imagen_plataforma, (300, 50)), (600, 400))
        
        self.laba1 = Moneda([self.sprites_trampas], imagen_laba, (-50, 735))
        self.laba2 = Moneda([self.sprites_trampas], imagen_laba, (190, 735))
        self.laba3 = Moneda([self.sprites_trampas], imagen_laba, (430, 735))
        self.laba4 = Moneda([self.sprites_trampas], imagen_laba, (670, 735))

        self.imagen_final = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_kaido.jpg"), (tam_pantalla))
        self.sonido_final = pygame.mixer.Sound("./src/assets/sounds/franky.mp3")
        self.pantalla_final = PantallaFinal(self.pantalla, self.imagen_final)

    def jugando(self):
        self.en_pausa = False        
        self.en_uso = True
        self.nombre_jugador = input("ingrese su nombre: ")
        if self.sonido_habilitado:
            self.musica.play(-1)
        while self.en_uso:
            tiempo_actual = pygame.time.get_ticks()

            self.actualizar_temporizador(tiempo_actual)

            self.reloj.tick(FPS)
            #-------> detecta eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.en_uso = False
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
                for enemigo in self.sprites_enemigos:
                    if not enemigo.disparar and tiempo_actual - self.actualizacion_ataques >= self.tiempo_ataques:
                        enemigo.actualizacion_golpe = tiempo_actual
                        self.actualizacion_ataques = tiempo_actual
                        enemigo.disparar = True
                    
                    if enemigo == self.kaido1 and enemigo.disparar and len(self.sprites_proyectil_enemigo) == 0:
                        proyectil_enemigo = Proyectil(enemigo.imagen_royectil, enemigo.mira_derecha, enemigo.rect.midbottom)
                        self.sprites_proyectil_enemigo.add(proyectil_enemigo)
                    if enemigo == self.kaido2 and enemigo.disparar and len(self.sprites_proyectil_enemigo) == 0:
                        proyectil_enemigo = Proyectil(enemigo.imagen_royectil, enemigo.mira_derecha, (self.jugador.rect.x, -50), 3)
                        self.sprites_proyectil_enemigo.add(proyectil_enemigo)
                    if enemigo == self.kaido3 and enemigo.disparar and len(self.sprites_proyectil_enemigo) == 0:
                        proyectil_enemigo = Proyectil(enemigo.imagen_royectil, enemigo.mira_derecha, (self.jugador.rect.x, -50), 3)
                        self.sprites_proyectil_enemigo.add(proyectil_enemigo)

                    
                    self.atacar_jugador(enemigo, tiempo_actual)

                    enemigo.actualizar_direccion(self.jugador.rect.x)
                    if enemigo == self.kaido2:
                        enemigo.caminar(tiempo_actual)
                
            
                # disparo e impacto de proyectiles
                if self.jugador.disparar and len(self.sprites_proyectil_jugador) == 0:
                    proyectil_jugador = Proyectil(self.jugador.imagen_royectil, self.jugador.mira_derecha, self.jugador.rect.midbottom)
                    self.sprites_proyectil_jugador.add(proyectil_jugador)
                self.golpe_proyectil(self.sprites_proyectil_jugador, self.sprites_enemigos)
                self.golpe_proyectil(self.sprites_proyectil_enemigo, self.sprites_jugador, False)
                
                # ataque cuerpo a cuerpo
                for enemigo in self.sprites_enemigos:
                    if enemigo.golpear and not self.jugador.caida:
                        self.golpe_mele(self.sprites_enemigos, self.sprites_jugador, False)
                if self.jugador.golpear:
                    self.golpe_mele(self.sprites_jugador, self.sprites_enemigos,)

                if self.kaido3.vidas <= 0:
                    self.sprites_enemigos.add(self.kaido1)
                if self.kaido1.vidas <= 0:
                    self.sprites_enemigos.remove(self.kaido1)
                    self.sprites_enemigos.add(self.kaido2)
                    self.sprites_trampas.empty()
                if self.kaido2.vidas <= 0:
                    self.en_uso = False
                    

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
    

    def pisar_trampa(self):
        item_colicion = pygame.sprite.spritecollide(self.jugador, self.sprites_trampas, False)
        if item_colicion:
            self.jugador.vidas -= 1
            self.jugador.rect.bottomleft = (300, 650)
            self.jugador.caida = True


    def golpe_proyectil(self, entidad: Proyectil, grupo_entidades: pygame.sprite.Group, disparo_jugador: bool = True):
        item_colicion = pygame.sprite.groupcollide(entidad, grupo_entidades, dokilla=True, dokillb=False)
        
        if disparo_jugador and item_colicion:
            self.jugador.puntuacion += 50
            for _, enemigos_colisionados in item_colicion.items():
                for enemigo in enemigos_colisionados:
                    enemigo.vidas -= 1
                    try:
                        enemigo.sonido_golpeado.play()
                    except pygame.error as e:
                        print(f"Error al reproducir sonido: {e}")
                    enemigo.caida = True
                    if enemigo.vidas <= 0:
                        self.sprites_enemigos.remove(enemigo)  # Eliminar físicamente del grupo
                    else:
                        enemigo.rect.bottomleft = enemigo.segunda_pos
                        enemigo.tiempo_caida = pygame.time.get_ticks()


        elif not disparo_jugador and item_colicion and not self.jugador.caida:
            self.jugador.puntuacion = 0
            self.jugador.vidas -= 1
            try:
                self.jugador.sonido_golpeado.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            self.jugador.caida = True

    # Elimina a los almirantes que han perdido todas sus vidas
        for enemigo in list(grupo_entidades):
            if enemigo.vidas <= 0:
                self.sprites_enemigos.remove(enemigo)
                

    def golpe_mele(self, entidad: Proyectil, grupo_entidades: pygame.sprite.Group, ataca_jugador: bool = True):
        item_colicion = pygame.sprite.groupcollide(entidad, grupo_entidades, dokilla=False, dokillb=False)
        
        if ataca_jugador and item_colicion:
            self.jugador.puntuacion += 50
            for _, enemigos_colisionados in item_colicion.items():
                for enemigo in enemigos_colisionados:
                    enemigo.vidas -= 1
                    try:
                        enemigo.sonido_golpeado.play()
                    except pygame.error as e:
                        print(f"Error al reproducir sonido: {e}")
                    enemigo.caida = True
                    if enemigo.vidas <= 0:
                        self.sprites_enemigos.remove(enemigo)  # Eliminar físicamente del grupo
                    else:
                        enemigo.rect.bottomleft = enemigo.segunda_pos
                        enemigo.tiempo_caida = pygame.time.get_ticks()

        elif not ataca_jugador and item_colicion and not self.jugador.caida:
            self.jugador.puntuacion = 0
            self.jugador.vidas -= 1
            try:
                self.jugador.sonido_golpeado.play()
            except pygame.error as e:
                print(f"Error al reproducir sonido: {e}")
            self.jugador.caida = True

    # Elimina a los almirantes que han perdido todas sus vidas
        for enemigo in list(grupo_entidades):
            if enemigo.vidas <= 0:
                self.sprites_enemigos.remove(enemigo)


    def mostrar_pantalla_final(self, nombre_record: str, puntos_record: int, centro_pantalla: tuple, victoria: bool):
        self.pantalla_final.mostrar(self.imagen_final, self.nombre_jugador, self.jugador.puntuacion, nombre_record, puntos_record, centro_pantalla, victoria)



nivel3_luffy = Nvl3(PANTALLA, fondo_lv3, luffy_pie, luffy_corriendo, luffy_salto, luffy_ata1, luffy_disparo, luffy_proyectil, luffy_caida, (600, 450), LUFFY_GOLPE, LUFFY_DISPARO, JUGADOR_CAMINA, JUGADOR_GOLPEADO, LUFFY_DISPARO)
nivel3_law = Nvl3(PANTALLA, fondo_lv3, law_pie, law_corriendo, law_salto, law_ata1, law_disparo, law_proyectil, law_caida, (600, 450), ZORO_DISPARA, LAW_DISPARA, JUGADOR_CAMINA, JUGADOR_GOLPEADO, LAW_DISPARA)






# pygame.transform.flip() girar superficie