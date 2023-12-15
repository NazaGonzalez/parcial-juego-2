import pygame
from config import*
from nivel import *
from menu import *
from nvl1 import *
from nvl2 import *
from nvl3 import *

pygame.init

class Juego():
    def __init__(self, ventana: pygame.surface.Surface, fondo: pygame.surface.Surface):
        self.reloj = pygame.time.Clock()
        self.pantalla = ventana 
        pygame.display.set_caption("Juego_2") 
        self.in_progress = True
        self.fondo = fondo
        self.menu_principal = menu_principal
        self.menu_nivel = menu_juegos
        self.menu_ajustes = menu_ajustes
        self.nivel1_a = nivel1_luffy
        self.nivel1_b = nivel1_zoro
        self.nivel2_a = nivel2_luffy
        self.nivel2_b = nivel2_jimbei
        self.nivel3_a = nivel3_luffy
        self.nivel3_b = nivel3_law

        self.opcion_principal = ""
        self.nivel_deseado = None

        self.sonido_habilitado = True

        


    def ejecucion(self):

        
        while self.in_progress:
            self.reloj.tick(FPS)
            #-------> detecta eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.in_progress = False

            self.menu_principal.sonido_habilitado = self.sonido_habilitado 
            self.menu_nivel.sonido_habilitado = self.sonido_habilitado
            self.menu_ajustes.sonido_habilitado = self.sonido_habilitado
            self.nivel1_a.sonido_habilitado = self.sonido_habilitado 
            self.nivel1_b.sonido_habilitado = self.sonido_habilitado 
            self.nivel2_a.sonido_habilitado = self.sonido_habilitado 
            self.nivel2_b.sonido_habilitado = self.sonido_habilitado 
            self.nivel3_a.sonido_habilitado = self.sonido_habilitado 
            self.nivel3_b.sonido_habilitado = self.sonido_habilitado 


            self.ver_menu_principal()

            self.ver_ajustes()

            self.elegir_nivel()


            self.reproducir_nivel()
            pygame.display.flip()
            


    def ver_menu_principal(self):
        if self.opcion_principal == "":
            opcion_seleccionada = self.menu_principal.elegir()
            if opcion_seleccionada == "niveles":
                self.opcion_principal = "niveles"
            elif opcion_seleccionada == "opciones":
                self.opcion_principal = "opciones"
            elif opcion_seleccionada == "salir":
                pygame.quit()
                sys.exit()


    def ver_ajustes(self):
        if self.opcion_principal == "opciones":
            opcion_seleccionada = self.menu_ajustes.elegir()
            if opcion_seleccionada == "sonido":
                self.sonido_habilitado = False if self.sonido_habilitado else True
            elif opcion_seleccionada == "atras":
                self.opcion_principal = ""


    def elegir_nivel(self):
        opcion_personaje_nivel = ""
        if self.opcion_principal == "niveles":
            opcion_personaje_nivel = self.menu_nivel.elegir()
            if opcion_personaje_nivel == "atras":
                self.opcion_principal = ""
            elif opcion_personaje_nivel == "luffy1":
                self.nivel_deseado = self.nivel1_a
            elif opcion_personaje_nivel == "zoro":
                self.nivel_deseado = self.nivel1_b
            elif opcion_personaje_nivel == "luffy2":
                if self.nivel1_a.completado or self.nivel1_b.completado:
                    self.nivel_deseado = self.nivel2_a
            elif opcion_personaje_nivel == "jimbei":
                if self.nivel1_a.completado or self.nivel1_b.completado:
                    self.nivel_deseado = self.nivel2_b
            elif opcion_personaje_nivel == "luffy3":
                if self.nivel2_a.completado or self.nivel2_b.completado:
                    self.nivel_deseado = self.nivel3_a
            elif opcion_personaje_nivel == "law":
                if self.nivel2_a.completado or self.nivel2_b.completado:
                    self.nivel_deseado = self.nivel3_b


    def reproducir_nivel(self):
        if self.nivel_deseado:
            self.nivel_deseado.jugando()
            self.nivel_deseado = ""


juego = Juego(PANTALLA, fondo_menu)
juego.ejecucion()








