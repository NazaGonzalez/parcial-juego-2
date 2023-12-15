import pygame
from pygame.locals import *
from random import *
from config import *
from personaje import *
from funciones import *
from jugador import *
from enemigo import *
from proyectil import *
from menu import *




class Nivel():
    def __init__(self, ventana: pygame.surface.Surface, fondo: pygame.surface.Surface, quieto: list, corriendo: list, saltando: list, golpe: list, disparo: list, proyectil: list, caida: list, pos_inicial: tuple, sonido_ataque: pygame.mixer.Sound, sonido_disparo: pygame.mixer.Sound, sonido_caminar: pygame.mixer.Sound, sonido_atacado: pygame.mixer.Sound, sonido_proyectil: pygame.mixer.Sound):
        pygame.init
        self.reloj = pygame.time.Clock()
        self.pantalla = ventana 
        pygame.display.set_caption("Juego_2") 
        self.en_uso = False
        self.completado = False
        self.fondo = fondo

        self.tiempo_inicio = 0
        self.tiempo_limite = 60000
        self.tiempo_restante = self.tiempo_limite

        self.sprites_proyectil_jugador = pygame.sprite.Group()
        self.sprites_proyectil_enemigo = pygame.sprite.Group()
        
        self.sprites_jugador = pygame.sprite.Group() # creo grupo de sprites
        self.jugador = Jugador([self.sprites_jugador], pos_inicial, quieto, corriendo, saltando, golpe, disparo, proyectil, caida, sonido_ataque, sonido_disparo, sonido_caminar, sonido_atacado, sonido_proyectil) # cero un jugador y la indico el grupo al que pertenece
        self.marcador = FUENTE.render(":" + str(self.jugador.puntuacion), True, NEGRO)
        self.marco_marcador = self.marcador.get_rect()
        self.marco_marcador.topleft = (0, 0)

        self.sprites_enemigos = pygame.sprite.Group()
        
        self.sprites_plataformas = pygame.sprite.Group()
        self.sprites_trampas = pygame.sprite.Group()

        self.sprites_monedas = pygame.sprite.Group()
        self.moneda_r = Moneda([self.sprites_monedas], imagen_moneda_r, (425, 100))

        self.musica = pygame.mixer.Sound("./src/assets/sounds/poder_son.mp3")
        self.musica.set_volume(0.5)
        self.sonido_habilitado = True

        self.imagen_final = pygame.surface.Surface
        self.sonido_final = pygame.mixer.Sound

        self.imagen_pausa = fondo_pausa
        self.menu_pausa = Menu(
                self.pantalla,
                self.imagen_pausa,
                (center_pantalla[0] - ANCHO // 4, center_pantalla[1] - ALTO // 4),   # Puedes personalizar la apariencia del fondo del menú de pausa
                "src/assets/sounds/one-piece-sanji.mp3",  # Puedes agregar un archivo de sonido para el menú de pausa
                Boton((230, 180), botones, 1, 1, self.atras),
                Boton((620, 450), botones, 3, 3, self.sonido),
                Boton((400, 350), botones2, 9, 9, self.salir),
                Boton((400, 450), botones2, 5, 5, self.opciones)
                )
        self.en_pausa = True

        self.nombre_jugador = ""
        

    def jugando(self):
       

            self.dibujar()

            self.actualizar()
            
            
    def dibujar(self):
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.marcador, self.marco_marcador)

        self.sprites_plataformas.draw(self.pantalla)
        self.sprites_trampas.draw(self.pantalla)
        self.sprites_monedas.draw(self.pantalla)
        self.sprites_jugador.draw(self.pantalla)
        self.sprites_enemigos.draw(self.pantalla)
        self.sprites_proyectil_jugador.draw(self.pantalla)
        self.sprites_proyectil_enemigo.draw(self.pantalla)


    def actualizar(self):

        self.marcador = FUENTE.render("Marcador:" + str(self.jugador.puntuacion) + "  Vidas: " + str(self.jugador.vidas) + "    Tiempo" + str(self.tiempo_restante//1000), True, NEGRO)

        self.pisar_plataforma(self.jugador)
        for enemigo in self.sprites_enemigos:
            self.pisar_plataforma(enemigo)
        self.pisar_trampa()

        self.traga_monedas(self.sprites_jugador, self.sprites_monedas)

        self.sprites_plataformas.update()
        self.sprites_trampas.update()
        self.sprites_monedas.update()
        self.sprites_jugador.update()
        self.sprites_enemigos.update()
        self.sprites_proyectil_jugador.update()
        self.sprites_proyectil_enemigo.update()

        pygame.display.flip()


    def cerrar(self):
        pass


    def pisar_plataforma(self, entidad):
        item_colicion = pygame.sprite.spritecollide(entidad, self.sprites_plataformas, False)

        for plataforma in item_colicion:
            entidad.plataforma_suelo = plataforma
        if type(entidad.plataforma_suelo) != int:
            if entidad.rect.bottom >= entidad.plataforma_suelo.rect.top + 20 and not entidad.saltar:
                entidad.velocidad_caida = 0
                entidad.rect.bottom = entidad.plataforma_suelo.rect.top + 20
            if entidad.rect.right < entidad.plataforma_suelo.rect.left or entidad.rect.left > entidad.plataforma_suelo.rect.right:
                entidad.velocidad_caida = 3
                entidad.plataforma_suelo = 0

        
    def pisar_trampa(self):
        item_colicion = pygame.sprite.spritecollide(self.jugador, self.sprites_trampas, False)
        if item_colicion:
            self.jugador.vidas -= 1


    def traga_monedas(self, jugador: pygame.sprite.Group, monedas: pygame.sprite.Group):
        item_colicion =  pygame.sprite.groupcollide(jugador, monedas, dokilla = False, dokillb = True)
        if item_colicion:
            self.jugador.puntuacion += 50
        for _ , enemigos_colisionados in item_colicion.items():
                for enemigo in enemigos_colisionados:
                    if enemigo == self.moneda_r:
                        self.jugador.poder_ataque = True


    def atacar_jugador(self, enemigo, tiempo_actual: int):
        if (
            not enemigo.golpear
            and enemigo.rect.centery >= self.jugador.rect.top
            and enemigo.rect.centery <= self.jugador.rect.bottom
            and abs(enemigo.rect.x - self.jugador.rect.x) <= 150
            and tiempo_actual - self.actualizacion_ataques == 10000
            ):
            enemigo.actualizacion_golpe = tiempo_actual
            self.actualizacion_ataques = tiempo_actual
            enemigo.golpear = True


    def atras(self):
        self.en_pausa = False

    def salir(self):
        self.en_uso = False

    def sonido(self):
        self.sonido_habilitado = False if self.sonido_habilitado else True
        self.menu_pausa.sonido_habilitado = self.sonido_habilitado

    def opciones(self):
        menu_ajustes.elegir()


    def realizar_accion(self, opcion_seleccionada):
        if opcion_seleccionada:
            opcion_seleccionada()
    

    def actualizar_temporizador(self, tiempo_actual):

        if not self.en_pausa and self.en_uso:
            tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
            self.tiempo_restante -= tiempo_transcurrido

        #if self.tiempo_restante <= 0:
        #   self.jugador.vidas = 0

        self.tiempo_inicio = tiempo_actual



