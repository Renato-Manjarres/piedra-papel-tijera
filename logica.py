import random
import datos

def eleccion_computadora():
    return random.choice(datos.opciones)

def normalizar_eleccion(eleccion):
    abreviaciones = {"p": "piedra", "pa": "papel", "t": "tijera"}
    if eleccion in abreviaciones:
        return abreviaciones[eleccion]
    return eleccion

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"

    if (jugador == "piedra" and computadora == "tijera") or \
       (jugador == "tijera" and computadora == "papel") or \
       (jugador == "papel"  and computadora == "piedra"):
        return "jugador"

    return "computadora"

def actualizar_puntaje(resultado):
    datos.ronda_actual = datos.ronda_actual + 1

    if resultado == "jugador":
        datos.puntaje_jugador = datos.puntaje_jugador + 1
        datos.historial.append("Ronda " + str(datos.ronda_actual) + ": Ganaste")
    elif resultado == "computadora":
        datos.puntaje_computadora = datos.puntaje_computadora + 1
        datos.historial.append("Ronda " + str(datos.ronda_actual) + ": Perdiste")
    else:
        datos.historial.append("Ronda " + str(datos.ronda_actual) + ": Empate")

def hay_ganador():
    return datos.puntaje_jugador >= datos.PUNTOS_PARA_GANAR or \
           datos.puntaje_computadora >= datos.PUNTOS_PARA_GANAR

def reiniciar_puntajes():
    datos.puntaje_jugador = 0
    datos.puntaje_computadora = 0
    datos.ronda_actual = 0
    datos.historial = []
