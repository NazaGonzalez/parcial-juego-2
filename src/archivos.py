import os
import json

def cargar_record(archivo_json: str, nivel: str, puntuacion_actual: int, nombre_jugador: str) -> tuple:
    if os.path.exists(archivo_json):
        with open(archivo_json, "r") as archivo:
            lector = json.load(archivo)
            registros_niveles = lector.get("niveles", {})
            
            # Obtener el record actual del nivel
            record_nivel = registros_niveles.get(nivel, {"nombre": "", "puntos": 0})
            
            nombre_record = record_nivel["nombre"]
            puntuacion_record = record_nivel["puntos"]
        if puntuacion_actual > puntuacion_record:
            nombre_record = nombre_jugador
            puntuacion_record = puntuacion_actual
            
            # Actualizar el record del nivel
            registros_niveles[nivel] = {"nombre": nombre_record, "puntos": puntuacion_record}
                
                # Actualizar el archivo JSON
            with open(archivo_json, "w") as archivo:
                lector["niveles"] = registros_niveles
                json.dump(lector, archivo)
    else:
        with open(archivo_json, "w") as archivo:
            nombre_record = nombre_jugador
            puntuacion_record = puntuacion_actual
                
            # Crear un nuevo registro para el nivel
            registros_niveles = {nivel: {"nombre": nombre_record, "puntos": puntuacion_record}}
                
                # Guardar en el archivo JSON
            datos = {"niveles": registros_niveles}
            json.dump(datos, archivo)

    return nombre_record, puntuacion_record




