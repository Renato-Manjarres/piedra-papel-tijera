import random

# Opciones del juego
opciones = ["piedra", "papel", "tijera", "dinamita"]
PUNTOS_PARA_GANAR = 3

print("=====================================")
print("   PIEDRA, PAPEL, TIJERA, DINAMITA   ")
print("=====================================")

seguir_jugando = True

while seguir_jugando:

    # Reiniciar puntajes para cada partida
    puntaje_jugador = 0
    puntaje_computadora = 0

    # Jugar rondas hasta que alguien llegue a 3
    while puntaje_jugador < PUNTOS_PARA_GANAR and puntaje_computadora < PUNTOS_PARA_GANAR:

        print("\n--- MARCADOR ---")
        print("  Jugador     :", puntaje_jugador)
        print("  Computadora :", puntaje_computadora)
        print("----------------")

        print("\nOpciones: piedra | papel | tijera | dinamita ")
        eleccion_jugador = input("Tu eleccion: ").strip().lower()

        if eleccion_jugador not in opciones:
            print("Opcion no valida, intenta de nuevo.")
            continue

        # La computadora elige al azar
        eleccion_pc = random.choice(opciones)

        print("\nTu elegiste  :", eleccion_jugador)
        print("Computadora  :", eleccion_pc)

        # Comparar jugadas
        if eleccion_jugador == eleccion_pc:
            print(">>> Empate en esta ronda.")

        elif eleccion_jugador == "piedra" and eleccion_pc == "tijera":
            print(">>> Ganaste esta ronda!")
            puntaje_jugador = puntaje_jugador + 1

        elif eleccion_jugador == "tijera" and eleccion_pc == "papel":
            print(">>> Ganaste esta ronda!")
            puntaje_jugador = puntaje_jugador + 1

        elif eleccion_jugador == "papel" and eleccion_pc == "piedra":
            print(">>> Ganaste esta ronda!")
            puntaje_jugador = puntaje_jugador + 1

        else:
            print(">>> La computadora gano esta ronda.")
            puntaje_computadora = puntaje_computadora + 1

    # Mostrar marcador final
    print("\n--- MARCADOR FINAL ---")
    print("  Jugador     :", puntaje_jugador)
    print("  Computadora :", puntaje_computadora)
    print("----------------------")

    # Anunciar ganador de la partida
    if puntaje_jugador >= PUNTOS_PARA_GANAR:
        print("\n*** GANASTE LA PARTIDA! Felicitaciones! ***")
    else:
        print("\n*** La computadora gano la partida. Mejor suerte la proxima! ***")

    # Preguntar si quiere jugar de nuevo
    respuesta = input("\nQuieres jugar de nuevo? (s/n): ").strip().lower()

    if respuesta != "s":
        seguir_jugando = False

print("\nHasta luego!")
