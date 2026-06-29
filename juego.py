import datos
import logica
import vista

def jugar_partida():
    logica.reiniciar_puntajes()

    while not logica.hay_ganador():
        vista.mostrar_marcador()

        eleccion = vista.pedir_eleccion()
        eleccion = logica.normalizar_eleccion(eleccion)

        if eleccion not in datos.opciones:
            print("Opcion no valida, intenta de nuevo.")
            continue

        pc = logica.eleccion_computadora()
        resultado = logica.determinar_ganador(eleccion, pc)

        logica.actualizar_puntaje(resultado)
        vista.mostrar_resultado_ronda(eleccion, pc, resultado)

    vista.mostrar_marcador()
    vista.mostrar_ganador_partida()
    vista.mostrar_historial()

    if datos.puntaje_jugador >= datos.PUNTOS_PARA_GANAR:
        datos.partidas_ganadas = datos.partidas_ganadas + 1
    else:
        datos.partidas_perdidas = datos.partidas_perdidas + 1

def main():
    vista.mostrar_bienvenida()

    while True:
        jugar_partida()

        if not vista.preguntar_revancha():
            vista.mostrar_estadisticas_sesion()
            print("\nHasta luego!")
            break

main()
