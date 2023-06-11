import numpy as np
import variables as vars

class Tablero:
    '''
    Clase para crear tableros y hacer operaciones en ellos
    - id: str, nombre
    - jugador: bool, indica si es el tablero del jugador o no
    - tablero: matriz cuadrada, donde se colocan los barcos
    -tablero_sin_barcos: tablero vacio que se le muestra al jugador
    - barcos: lista de listas con las coordenadas de cada barco
    '''

    def __init__(self, id, jugador=False):
        self.id = id
        self.jugador = jugador
        self.vaciar_tablero()
        if not self.jugador:
            self.tablero_sin_barcos = self.tablero.copy()
        self.barcos = []
        self.colocar_barcos()
        
    def vaciar_tablero(self):
        #np.full((10, 10), ' ')
        self.tablero = np.full((vars.DIMENSION_TABLERO, vars.DIMENSION_TABLERO),
                               vars.NADA)

    def mostrar_tablero(self):
        # mostrar el tablero que toque segun de quien sea
        # deprecated
        print(self.id)
        if not self.jugador:
            print(self.tablero_sin_barcos, end='\n\n')
        else:
            print(self.tablero, end='\n\n')

    def ver_casilla(self, coords):
        # devuelve lo que contenga la casilla, tipico get_
        return self.tablero[tuple(coords)]

    def actualizar_casilla(self, coords, accion):
        # escribe la nueva accion en la casilla, tipico set_
        self.tablero[tuple(coords)] = accion
        if not self.jugador and accion != vars.BARCO:
            # en este tablero no se muestran los barcos
            self.tablero_sin_barcos[tuple(coords)] = accion

    def colocar_barcos(self):
        for cant, tipo in vars.BARCOS:
            for i in range(cant):
                self.colocar_barco(tipo)

    def colocar_barco(self, longitud):

        def punta_valida(coords):
            # comprobar que no haya barcos en las 9 casillas alrededor de la primera coordenada
            x, y = coords[0], coords[1]
            x_desde = x if x == 0 else x-1
            x_hasta = x+2 # si es mas grande que la matriz se ajusta solo
            y_desde = y if y == 0 else y-1
            y_hasta = y+2
            return vars.BARCO not in self.tablero[x_desde:x_hasta, y_desde:y_hasta]

        def perimetro_extra_valido(coords, direccion):
            # comprobar que no hay barcos en las siguientes 3 casillas en perpendicular hacia esa direccion
            x, y = coords[0], coords[1] # (fila, columna)

            if direccion == 'N':
                if x == 0:
                    #si no hay tablero no hay barcos
                    return True
                x -= 1 # la fila anterior entera
                y_desde = y if y == 0 else y-1
                y_hasta = y+2
                return vars.BARCO not in self.tablero[x, y_desde:y_hasta]
            if direccion == 'S':
                if x == vars.DIMENSION_TABLERO-1:
                    #si no hay tablero no hay barcos
                    return True
                x += 1 # la fila anterior entera
                y_desde = y if y == 0 else y-1
                y_hasta = y+2
                return vars.BARCO not in self.tablero[x, y_desde:y_hasta]
            if direccion=='E':
                if y == vars.DIMENSION_TABLERO-1:
                    return True
                x_desde = x if x == 0 else x-1
                x_hasta = x+2
                y += 1
                return vars.BARCO not in self.tablero[x_desde:x_hasta, y]
            if direccion=='O':
                if y == 0:
                    return True
                x_desde = x if x == 0 else x-1
                x_hasta = x+2
                y -= 1
                return vars.BARCO not in self.tablero[x_desde:x_hasta, y]
        
        def dibujar_barco(inicio, direccion, longitud):
            x, y = inicio[0], inicio[1]
            long = 0
            nuevo_barco = [] # para guardar las coordenadas de cada barco
            while long < longitud:
                self.actualizar_casilla((x, y), vars.BARCO)
                nuevo_barco.append((x, y))
                if direccion == 'N':
                    x -= 1
                if direccion == 'S':
                    x += 1
                if direccion == 'E':
                    y += 1
                if direccion == 'O':
                    y -= 1
                long += 1
            self.barcos.append(nuevo_barco)

        ha_cabido = False
        while not ha_cabido: # hasta que entre entero
            punta = np.random.randint(10, size=2) # [x, y]
            if not punta_valida(punta):
                continue # otra punta
            direcciones = vars.DIRECC_CARDIN.copy()
            while direcciones and not ha_cabido:
                # sacar una direccion aleatoria de las que quedan y volver a la punta
                direccion = direcciones.pop(np.random.randint(len(direcciones)))
                mas_barco = punta.copy()
                long = 1
                # intentar meter el barco en esa direccion
                while long < longitud:
                    if direccion == 'N': # x^ == x-
                        mas_barco[0] -= 1
                        if mas_barco[0] < 0:
                            # fuera del tablero, cambia direccion y vuelve a la punta
                            break
                    if direccion == 'S': # xv == x+
                        mas_barco[0] += 1
                        if mas_barco[0] > vars.DIMENSION_TABLERO-1:
                            break
                    if direccion == 'E': # y-> == y+
                        mas_barco[1] += 1
                        if mas_barco[1] > vars.DIMENSION_TABLERO-1:
                            break
                    if direccion == 'O': # y<- == y-
                        mas_barco[1] -= 1
                        if mas_barco[1] < 0:
                            break
                    if not perimetro_extra_valido(mas_barco, direccion):
                        # hay un barco en el perimetro, cambia direccion y vuelve a la punta
                        break
                    long += 1
                if long == longitud:
                    ha_cabido = True
        dibujar_barco(punta, direccion, longitud)

    def actualizar_barcos(self, coords):
        # ir borrando las coordenadas de los barcos cuando se les dispara para saber cuando pierde
        msg = ''
        for barco in self.barcos:
            if tuple(coords) in barco:
                barco.remove(tuple(coords))
                msg = 'tocado'
                if not barco:
                    self.barcos.remove(barco)
                    msg = msg + ' y hundido'
                break
        print(msg)

    def disparar(self, coords):
        casilla = self.ver_casilla(coords)
        if casilla == vars.NADA:
            self.actualizar_casilla(coords, vars.AGUA)
        elif casilla == vars.BARCO:
            self.actualizar_casilla(coords, vars.DESTRUCCION)
            self.actualizar_barcos(coords)
        return casilla