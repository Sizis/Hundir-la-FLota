
DIMENSION_TABLERO = 10 # 10x10
LETRAS = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J'}
DIRECC_CARDIN = ['N', 'S', 'E', 'O']
BARCOS = [(1, 4), (2, 3), (3, 2), (4, 1)] # (catidad, longitud)
NADA = ' '
AGUA = '~'
BARCO = 'O'
DESTRUCCION = 'X'

mensage_reglas = '''
        Bienbenido a Hundir la Flota
Reglas:
 - Por turnos elije una casilla para disparar
 - Si aciertas a un barco vuelves a disparar,
    si fallas se acaba tu turno
 - El Oponente juega solo y se le aplican las mismas reglas
 - El primero que destrulla todos los barcos gana

'''


