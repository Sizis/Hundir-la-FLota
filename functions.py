import clases as clss
import variables as vars


def formatear_eleccion(eleccion):
    # cambia de string "letra numero" a lista [numero, numero]
    for key, val in vars.LETRAS.items():
        if val == eleccion[0].upper():
            x = key
            break
    y = int(eleccion[1])
    return [x, y]

def mostrar_tableros(tableros):
    jugador = tableros[1].tablero
    oponente = tableros[0].tablero_sin_barcos
    # print(tableros[0].tablero) # cheats
    # print()
    print(f'\t\t{tableros[1].id}\t\t\t\t\t\t{tableros[0].id}')
    for i in range(vars.DIMENSION_TABLERO):
        print(f'{vars.LETRAS[i]} {jugador[i]}\t{vars.LETRAS[i]} {oponente[i]}')
    print('    0   1   2   3   4   5   6   7   8   9\t    0   1   2   3   4   5   6   7   8   9\n')