import pygame
from funciones import HojaSprites

pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

ANCHO = 900
ALTO = 675
FPS = 60

tam_pantalla = (ANCHO, ALTO)
center_pantalla = (ANCHO // 2, ALTO // 2)



PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_icon(pygame.image.load("./src/assets/images/gomugomu1.png"))


pygame.init

FUENTE = pygame.font.SysFont("Comic Sans MS", 40)


try: 

    KAITO_ATAC = pygame.mixer.Sound("./src/assets/sounds/ataque_kaido1.mp3")
    KAIDO_CAMINA = pygame.mixer.Sound("./src/assets/sounds/caminar_kaido.mp3")
    KAIDO_GOLPEADO = pygame.mixer.Sound("./src/assets/sounds/kaido_golpeado.mp3")
    PROYECTIL_KAIDO = pygame.mixer.Sound("./src/assets/sounds/proyectil_kaido.mp3")
    ENEMIGO_GOLPEADO = pygame.mixer.Sound("./src/assets/sounds/almirante_golpeado.mp3")
    ALMIRANTE_DISPARA = pygame.mixer.Sound("./src/assets/sounds/disparo_almirante.mp3")
    SALTO = pygame.mixer.Sound("./src/assets/sounds/salto.mp3")
    JUGADOR_CAMINA = pygame.mixer.Sound("./src/assets/sounds/caminar_jugador.mp3")
    JUGADOR_GOLPEADO = pygame.mixer.Sound("./src/assets/sounds/luffy_golpeado.mp3")
    LUFFY_DISPARO = pygame.mixer.Sound("./src/assets/sounds/lufi_gomugomu.mp3")
    LUFFY_GOLPE = pygame.mixer.Sound("./src/assets/sounds/lufi_pistol.mp3")
    AGARRAR_MONEDA = pygame.mixer.Sound("./src/assets/sounds/moneda_son.mp3")
    JIMBEI_DISPARA = pygame.mixer.Sound("./src/assets/sounds/proyectil_jimbei.mp3")
    LAW_DISPARA = pygame.mixer.Sound("./src/assets/sounds/proyectil_law.mp3")
    ZORO_PROYECTIL = pygame.mixer.Sound("./src/assets/sounds/proyectil_zoro.mp3")
    ZORO_DISPARA = pygame.mixer.Sound("./src/assets/sounds/zoro_disparo.mp3")
    GOLPE_ESPADA = pygame.mixer.Sound("./src/assets/sounds/golpe_espada.mp3")
    SONIDO_VICTORIA = pygame.mixer.Sound("./src/assets/sounds/franky.mp3")

except Exception as e:
    print(f"¡Ocurrió un error al cargar los sonidos del juego!: {e}")


try: 
    luffy_pie = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffy_pie45,95.png").convert_alpha(), 6, 45, 95).lista_animacion()
    luffy_corriendo = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffy_correr70,80.png").convert_alpha(), 8, 70, 80).lista_animacion()
    luffy_salto = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffi_salto50,90.png").convert_alpha(), 6, 50, 90).lista_animacion()
    luffy_ata1 = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffy_ataque1_90,50.png").convert_alpha(), 6, 90, 50).lista_animacion(1.5)
    luffy_disparo = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffy_ataque2_110,90.png").convert_alpha(), 11, 110, 90).lista_animacion()
    luffy_proyectil = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffy_proyectil120,100.png").convert_alpha(), 6, 120, 100).lista_animacion()
    luffy_caida = HojaSprites(pygame.image.load("./src/assets/images/luffy/luffi_suelo85,85.png").convert_alpha(), 8, 85, 85).lista_animacion()

    zoro_pie = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_pie82,78.png").convert_alpha(), 6, 82, 78).lista_animacion()
    zoro_corriendo = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_corrier62,60.png").convert_alpha(), 8, 62, 60).lista_animacion(1.5)
    zoro_salto = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_salto93,86.png").convert_alpha(), 3, 93, 86).lista_animacion()
    zoro_ata1 = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_ataque1_45,58.png").convert_alpha(), 11, 45, 58).lista_animacion(2.5)
    zoro_disparo = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_ataque2_57,80.png").convert_alpha(), 8, 57, 80).lista_animacion()
    zoro_proyectil = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_proyectil155,206.png").convert_alpha(), 7, 155, 102).lista_animacion()
    zoro_caida = HojaSprites(pygame.image.load("./src/assets/images/zoro/zoro_suelo81,89.png").convert_alpha(), 16, 81, 89).lista_animacion()

    jimbei_pie = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_pie75,85.png").convert_alpha(), 4, 75, 85).lista_animacion(1.2)
    jimbei_corriendo = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_correr80,90.png").convert_alpha(), 8, 80, 90).lista_animacion(1.2)
    jimbei_salto = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_salto90,90.png").convert_alpha(), 2, 90, 90).lista_animacion(1.2)
    jimbei_ata1 = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_atac1_95,90.png").convert_alpha(), 7, 95, 90).lista_animacion(1.2)
    jimbei_disparo = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_atac2_100,95.png").convert_alpha(), 5, 100, 95).lista_animacion(1.2)
    jimbei_caida = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_suelo80,80.png").convert_alpha(), 8, 80, 80).lista_animacion(1.2)
    jimbei_proyectil = HojaSprites(pygame.image.load("./src/assets/images/jimbei/jimbei_proyectil65,70.png").convert_alpha(), 7, 65, 70).lista_animacion(1.2)

    law_pie = HojaSprites(pygame.image.load("./src/assets/images/law/law_pie55,95.png").convert_alpha(), 4, 55, 95).lista_animacion()
    law_corriendo = HojaSprites(pygame.image.load("./src/assets/images/law/law_corriendo76,100.png").convert_alpha(), 6, 76, 100).lista_animacion()
    law_salto = HojaSprites(pygame.image.load("./src/assets/images/law/law_salto73,94.png").convert_alpha(), 4, 73, 94).lista_animacion()
    law_ata1 = HojaSprites(pygame.image.load("./src/assets/images/law/law_at1_110,105.png").convert_alpha(), 9, 110, 105).lista_animacion()
    law_disparo = HojaSprites(pygame.image.load("./src/assets/images/law/law_at2_70,70.png").convert_alpha(), 6, 70, 70).lista_animacion()
    law_caida = HojaSprites(pygame.image.load("./src/assets/images/law/law_caido75,75.png").convert_alpha(), 8, 75, 75).lista_animacion()
    law_proyectil = HojaSprites(pygame.image.load("./src/assets/images/law/law_explocion80,80.png").convert_alpha(), 4, 80, 80).lista_animacion(1.5)

    buggy_pie = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_pie,50,55.png").convert_alpha(), 3, 50, 55).lista_animacion(1.2)
    buggy_correr = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_correr83,59.png").convert_alpha(), 6, 83, 57).lista_animacion(1.2)
    buggy_salto = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_salto56,77.png").convert_alpha(), 5, 56, 77).lista_animacion(1.2)
    buggy_ata1 = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_ataque1_78,74.png").convert_alpha(), 11, 78, 74).lista_animacion(1.2)
    buggy_disparo = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_ataque2_66,60.png").convert_alpha(), 9, 66, 60).lista_animacion(1.5)
    buggy_proyectil = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_proyectil50,50.png").convert_alpha(), 4, 50, 50).lista_animacion(1.75)
    buggy_suelo = HojaSprites(pygame.image.load("./src/assets/images/buggy/bugy_golpeado57,65.png").convert_alpha(), 8, 57, 65).lista_animacion(1.75)

    akainu_pie = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_pie45,70.png").convert_alpha(), 4, 45, 70).lista_animacion(1.5)
    akainu_corriendo = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_correr80,80.png").convert_alpha(), 16, 80, 80).lista_animacion()
    akainu_salto = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_salto64,93.png").convert_alpha(), 2, 64, 93).lista_animacion(1.2)
    akainu_ata1 = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_atac1_160,100.png").convert_alpha(), 11, 160, 100).lista_animacion(1.5)
    akainu_disparo = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_atac2_70,80.png").convert_alpha(), 6, 70, 80).lista_animacion(1.5)
    akainu_caida = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_suelo80,80.png").convert_alpha(), 14, 80, 80).lista_animacion(2)
    akainu_proyectil = HojaSprites(pygame.image.load("./src/assets/images/akainu/akainu_proyectil35,65.png").convert_alpha(), 17, 35, 65).lista_animacion(2.5)

    kizaru_pie = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_pie45,80.png").convert_alpha(), 5, 45, 80).lista_animacion(1.5)
    kizaru_corriendo = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_correr86,100.png").convert_alpha(), 7, 86, 100).lista_animacion()
    kizaru_salto = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_salto85,88.png").convert_alpha(), 2, 85, 88).lista_animacion(1.5)
    kizaru_ata1 = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_atac1_120,93.png").convert_alpha(), 7, 120, 93).lista_animacion(1.5)
    kizaru_disparo = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_atac2_115,105.png").convert_alpha(), 11, 115, 105).lista_animacion()
    kizaru_caida = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_suelo75,80.png").convert_alpha(), 11, 75, 80).lista_animacion()
    kizaru_proyectil = HojaSprites(pygame.image.load("./src/assets/images/kizaru/kizaru_proyectil39,118.png").convert_alpha(), 4, 39, 118).lista_animacion()

    aokiji_pie = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_pie45,105.png").convert_alpha(), 8, 45, 105).lista_animacion(1.2)
    aokiji_corriendo = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_correr70,70.png").convert_alpha(), 9, 70, 70).lista_animacion()
    aokiji_salto = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_salto90,120.png").convert_alpha(), 2, 90, 120).lista_animacion()
    aokiji_ata1 = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_atac1_70,82.png").convert_alpha(), 15, 70, 82).lista_animacion(2.3)
    aokiji_disparo = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_atac2_70,100.png").convert_alpha(), 5, 70, 100).lista_animacion(1.2)
    aokiji_caida = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_suelo85,118.png").convert_alpha(), 8, 85, 118).lista_animacion()
    aokiji_proyectil = HojaSprites(pygame.image.load("./src/assets/images/aokiji/aokiji_proyectil120,120.png").convert_alpha(), 7, 120, 120).lista_animacion()

    kaido1_pie = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido1_pie125,140.png").convert_alpha(), 4, 120, 140).lista_animacion(1.5)
    kaido1_corriendo = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido1_correr60,60.png").convert_alpha(), 8, 60, 60).lista_animacion(2.5)
    kaido1_salto = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido_salto200,175.png").convert_alpha(), 2, 200, 175).lista_animacion(0.7)
    kaido1_ata1 = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido1_atac1_100,70.png").convert_alpha(), 5, 100, 70).lista_animacion(2)
    kaido1_disparo = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido1_atac2_110,110.png").convert_alpha(), 4, 110, 110).lista_animacion(1.5)
    kaido1_caida = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido_suelo210,160.png").convert_alpha(), 7, 210, 160).lista_animacion()
    kaido1_proyectil = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido_proyectil1_170,100.png").convert_alpha(), 5, 170, 100).lista_animacion(1.5)

    kaido2_pie = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido2_pie110,120.png").convert_alpha(), 4, 110, 120).lista_animacion(1.2)
    kaido2_ata1 = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido2_atac1_80,75.png").convert_alpha(), 6, 80, 75).lista_animacion(2.2)
    kaido2_disparo = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido2_atac2_71,76.png").convert_alpha(), 7, 71, 76).lista_animacion(2)
    kaido2_proyectil = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido_proyectil2_400,300.png").convert_alpha(), 4, 400, 300).lista_animacion(0.5)

    kaido3_proyectil = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido_proyectil3_80,160.png").convert_alpha(), 7, 80, 160).lista_animacion()
    kaido3_pie = HojaSprites(pygame.image.load("./src/assets/images/kaido/kaido3_pie273,167.png").convert_alpha(), 12, 273, 167).lista_animacion(1.2)


    imagen_plataforma = pygame.image.load("./src/assets/images/tablon505,70.png")
    fondo_lv1 = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo1.png"), (tam_pantalla))
    fondo_lv2 = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo2.jpg"), (tam_pantalla))
    fondo_lv3 = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo3.jpg"), (tam_pantalla))
    fondo_pausa = pygame.transform.scale(pygame.image.load("./src/assets/images/fondo_pausa.jpg"), ((ANCHO // 2, ALTO // 2)))

    imagen_moneda_r = HojaSprites(pygame.image.load("./src/assets/images/monedaR100,138.png").convert_alpha(), 9, 100, 138).lista_animacion(0.5)
    imagen_laba = HojaSprites(pygame.image.load("./src/assets/images/laba80,40.png").convert_alpha(), 8, 80, 40).lista_animacion(3)

except Exception as e:
    print(f"¡Ocurrió un error al cargar las imagenes del juego!: {e}")









