
import random

opciones = ["piedra", "papel", "tijera"]

def jugar(nombre):
    print("\n--- Piedra, Papel o Tijera ---")
    eleccion_usuario = input("Elegí piedra, papel o tijera: ").lower()
    
    if eleccion_usuario not in opciones:
        print("Opción inválida.")
        return 0

    eleccion_bot = random.choice(opciones)
    print(f"{nombre} eligió: {eleccion_usuario}")
    print(f"Bot eligió: {eleccion_bot}")

    if eleccion_usuario == eleccion_bot:
        print("¡Empate!")
        return 1
    elif (eleccion_usuario == "piedra" and eleccion_bot == "tijera") or \
         (eleccion_usuario == "papel" and eleccion_bot == "piedra") or \
         (eleccion_usuario == "tijera" and eleccion_bot == "papel"):
        print("¡Ganaste!")
        return 10
    else:
        print("Perdiste.")
        return 0
