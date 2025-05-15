import os
from juegos import ppt
from sistema import puntajes
from juegos import generala

def mostrar_menu():
    print("\n--- Bienvenido al bot de juegos ---")
    print("1_ Jugar, piedra o tijeras")
    print("2_ Jugar generala")
    print("3_ Ver puntajes")
    print("4_ Salir")

def main():
    puntajes.cargar_puntajes()

    while True:
        mostrar_menu()
        
        opciones = input("\nElija una opcion: ")

        if opciones == "1":
            jugador = input("Ingrese su nombre: ")
            resultado = ppt.jugar(jugador)
            puntajes.actualizar_puntaje(jugador, resultado)
        elif opciones == "2":
            jugador = input("Ingrese su nombre: ")
            resultado = generala.jugar_turno()
            puntajes.actualizar_puntaje(jugador, resultado)
        elif opciones == "3":
            puntajes.mostrar_puntajes()
        elif opciones == "4":
            print("Gracias por jugar")
            break
        else:
            print("Opción inválida, ingrese un valor valido")
        
if __name__ == "__main__":
    main()