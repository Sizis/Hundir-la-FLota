from functions import *
import variables as vars
import numpy as np


print(vars.mensage_reglas)
# inicializar tableros
t_oponente = clss.Tablero('Oponente')
t_jugador = clss.Tablero('Jugador', jugador=True)
tableros = [t_oponente, t_jugador]
turno = np.random.randint(2) # 0->Opponente, 1->Jugador
print(f'{tableros[turno].id} empieza jugando\n')

while True:
    if tableros[turno].jugador:
        # turno del jugador
        mostrar_tableros(tableros)
        eleccion = input('Selecciona una casilla o 0 para rendirte: ')
        if eleccion == '0':
            print('Te has rendido, Game Over')
            break
        try:
            eleccion = formatear_eleccion(eleccion)
        except:
            print('Formato incorrecto')
            continue
        if 0 > eleccion[0] > vars.DIMENSION_TABLERO-1 or \
            0 > eleccion[1] > vars.DIMENSION_TABLERO-1:
            print('Coordenadas fuera del tablero. Prueba otra vez')
            continue
    else:
        # turno del oponente
        eleccion = np.random.randint(10, size=2)

    casilla = tableros[1-turno].disparar(eleccion)
    if casilla == vars.BARCO:
        if not tableros[1-turno].barcos:
            print(f'El {tableros[turno].id} ha ganado.')
            break
        if tableros[turno].jugador:
            print('Has acertado! Juega de nuevo')
        else:
            print(f'Oponente dispara a {eleccion} y acierta')
        continue
    if casilla == vars.NADA:
        if tableros[turno].jugador:
            print('Agua. Turno del oponente\n')
        else:
            print('Oponente ha fallado. Tu Turno\n')
        turno = 1 - turno # alternar entre 0 y 1
        continue
    if tableros[turno].jugador:
        print('Ya has disparado ahi. Prueba otra vez')
    continue
