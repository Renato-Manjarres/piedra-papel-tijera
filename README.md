# Piedra, Papel o Tijera

**Estudiante:** Renato Manjarres  
**Fecha:** Junio 2026

---

## Objetivo del sistema

Desarrollar un juego de Piedra, Papel o Tijera en Python donde el jugador compite contra la computadora. El primero en llegar a 3 puntos gana la partida.

---

## Descripcion de funcionalidades

- El jugador elige entre piedra, papel o tijera (tambien acepta abreviaciones: `p`, `pa`, `t`)
- La computadora elige su jugada de forma aleatoria
- Se comparan las jugadas y se determina el ganador de cada ronda
- El marcador se actualiza automaticamente despues de cada ronda
- Se muestra el numero de ronda actual durante la partida
- Al terminar cada partida se muestra el historial de rondas
- Al salir del juego se muestran las estadisticas de la sesion (partidas ganadas y perdidas)
- El jugador puede jugar varias partidas seguidas

---

## Como ejecutar

```
python3 juego.py
```

---

## Estructura del proyecto

El proyecto esta dividido en 3 capas:

| Archivo | Capa | Descripcion |
|---|---|---|
| `datos.py` | Datos | Variables y estado del juego |
| `logica.py` | Logica | Reglas del juego y calculo del ganador |
| `vista.py` | Vista | Todo lo que se muestra en pantalla |
| `juego.py` | Principal | Conecta las 3 capas y controla el flujo |

---

## Diagramas

### Diagrama de Casos de Uso
![Diagrama de casos de uso](imagenes/diagrama-casos-de-uso.png)

### Diagrama de Flujo
![Diagrama de flujo](imagenes/diagrama-flujo.png)

### Diagrama de Arquitectura
![Diagrama de arquitectura](imagenes/diagrama-arquitectura.png)
