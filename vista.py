import datos

VERDE    = "\033[92m"
ROJO     = "\033[91m"
AMARILLO = "\033[93m"
AZUL     = "\033[94m"
RESET    = "\033[0m"

def mostrar_bienvenida():
    print(AZUL + "==============================" + RESET)
    print(AZUL + "   PIEDRA, PAPEL O TIJERA"     + RESET)
    print(AZUL + "==============================" + RESET)
    print("  Abreviaciones: p = piedra | pa = papel | t = tijera")

def mostrar_marcador():
    print(AZUL + "\n--- RONDA " + str(datos.ronda_actual + 1) + " | MARCADOR ---" + RESET)
    print("  Jugador     :", VERDE + str(datos.puntaje_jugador)      + RESET)
    print("  Computadora :", ROJO  + str(datos.puntaje_computadora)  + RESET)
    print("  (Primero en llegar a", datos.PUNTOS_PARA_GANAR, "gana)")
    print(AZUL + "------------------------" + RESET)

def pedir_eleccion():
    print("\nOpciones: piedra | papel | tijera  (o p / pa / t)")
    return input("Tu eleccion: ").strip().lower()

def mostrar_resultado_ronda(eleccion_jugador, eleccion_pc, resultado):
    print("\nTu elegiste  :", eleccion_jugador)
    print("Computadora  :", eleccion_pc)

    if resultado == "jugador":
        print(VERDE + ">>> Ganaste esta ronda!" + RESET)
    elif resultado == "computadora":
        print(ROJO + ">>> La computadora gano esta ronda." + RESET)
    else:
        print(AMARILLO + ">>> Empate en esta ronda." + RESET)

def mostrar_historial():
    print(AZUL + "\n--- HISTORIAL DE RONDAS ---" + RESET)
    for entrada in datos.historial:
        print(" ", entrada)
    print(AZUL + "---------------------------" + RESET)

def mostrar_ganador_partida():
    if datos.puntaje_jugador >= datos.PUNTOS_PARA_GANAR:
        print(VERDE + "\n*** GANASTE LA PARTIDA! Felicitaciones! ***" + RESET)
    else:
        print(ROJO + "\n*** La computadora gano la partida. Mejor suerte la proxima! ***" + RESET)

def mostrar_estadisticas_sesion():
    print(AZUL + "\n--- ESTADISTICAS DE LA SESION ---" + RESET)
    print("  Partidas ganadas :", VERDE + str(datos.partidas_ganadas) + RESET)
    print("  Partidas perdidas:", ROJO  + str(datos.partidas_perdidas) + RESET)
    print(AZUL + "---------------------------------" + RESET)

def preguntar_revancha():
    respuesta = input("\nQuieres jugar de nuevo? (s/n): ").strip().lower()
    return respuesta == "s"
