import random
import os

def lanzar_dados():
    dados = []
    for i in range(5):
        numero = random.randint(1, 6)
        dados.append(numero)
    return dados

def contar_dados(dados):
    conteo = {}
    for numero in dados:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1
    return conteo


def evaluar_jugada(dados):
    conteo = contar_dados(dados)
    valores = list(conteo.values())
    dados_ordenados = sorted(dados)

    if 5 in valores:
        return "Generala"
    elif 4 in valores:
        return "Poker"
    elif 3 in valores:
        return "Full"
    elif dados_ordenados == [1, 2, 3, 4, 5] or dados_ordenados == [2, 3, 4, 5, 6]:
        return "Escalera"
    else:
        return "Nada"

def mostrar_dados(dados):
    print("Tus dados son: ")
    for i, dado in enumerate(dados):
        print(f"[{i}] {dado}")

def jugar_turno():
    dados = lanzar_dados()
    
    for tiro in range(3):
        print(f"\nTiro {tiro + 1}:")
        mostrar_dados(dados)

        if tiro < 2:
            eleccion = input("¿Qué dados querés guardar? (escribí los índices separados por coma, o enter para tirar todos): ")
            if eleccion:
                indices = [int(i.strip()) for i in eleccion.split(",")]
                dados_guardados = [dados[i] for i in indices]
                # Tirar los dados que faltan
                nuevos_dados = lanzar_dados()
                dados = dados_guardados + nuevos_dados[len(dados_guardados):]
            else:
                dados = lanzar_dados()
        else:
            print("Fin del turno.")

    mostrar_dados(dados)
    jugada = evaluar_jugada(dados)
    print(f"\n¡Tu jugada fue: {jugada}!")
    if jugada == "Generala":
        return 100
    elif jugada == "Escalera":
        return 80
    elif jugada == "Full":
        return 60
    elif jugada == "Poker":
        return 40
    elif jugada == "Nada":
        return 0
