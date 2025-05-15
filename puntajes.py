import json
import os

ruta = "Bot_Juegos/data/puntajes.json"

def cargar_puntajes():
    if not os.path.exists("Bot_Juegos/data"):
        os.makedirs("Bot_Juegos/data")
    if not os.path.isfile(ruta):
        with open(ruta, "w") as f:
            json.dump({}, f)

def leer_puntajes():
    with open(ruta, "r") as f:
        return json.load(f)
    
def guardar_puntajes(puntajes):
    with open(ruta, "w") as f:
        json.dump(puntajes, f, indent=4)

def actualizar_puntaje(nombre, puntos_sumados):
    puntajes = leer_puntajes()

    if nombre in puntajes:
        puntajes[nombre]["puntos"] += puntos_sumados
    else:
        puntajes[nombre] = {"puntos": puntos_sumados}

    guardar_puntajes(puntajes)

def mostrar_puntajes():
    puntajes = leer_puntajes()
    
    if not puntajes:
        print("\nNo hay puntajes registrados aún.")
    else:
        print("\n--- Puntajes acumulados ---")
        for nombre, datos in puntajes.items():
            print(f"{nombre}: {datos['puntos']} puntos")
