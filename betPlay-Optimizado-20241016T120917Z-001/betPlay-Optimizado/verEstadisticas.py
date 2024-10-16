
import estadisticasJugadores as ej
import estadisticasEquipos as ee
def verEstadisticasEquipo(Teams):
    switchVerEquipo = True 
    while (switchVerEquipo):
        equipoDisponible = False
        equipo= str(input("Por favor, ingrese el nombre del equipo para ver sus estadísticas"))
        for i in range(1,len(Teams)+1):
            if equipo in Teams[i]['nombre']:
                equipoDisponible=True
                indiceEquipo= i
        if (equipoDisponible==True):
            print(f"la cantidad de partidos jugados de {equipo} es {Teams[indiceEquipo]['estadísticas']['partidosJugados']}")
            print(f"la cantidad de partidos ganados de {equipo} es {Teams[indiceEquipo]['estadísticas']['partidosGanados']}")
            print(f"la cantidad de partidos perdidos de {equipo} es {Teams[indiceEquipo]['estadísticas']['partidosPerdidos']}")
            print(f"la cantidad de goles a favor de {equipo} es {Teams[indiceEquipo]['estadísticas']['golesAFavor']}")
            print(f"la cantidad de goles en contra de {equipo} es {Teams[indiceEquipo]['estadísticas']['golesEnContra']}")
            print(f"la cantidad de puntos de {equipo} es {Teams[indiceEquipo]['estadísticas']['totalPuntos']}")
            print(f"la cantidad de partidos de local de {equipo} es {Teams[indiceEquipo]['estadísticas']['partidosLocal']}")
            print(f"la cantidad de partidos de visitante de {equipo} es {Teams[indiceEquipo]['estadísticas']['partidosVisitante']}")

        else: 
            print("El equipo ingresado no coincide con ninguno de nuestros registros.")

            
        
        switchVerEquipo = bool(input("Si desea ver las estadísticas de otro equipo, por favor ingrese cualquier caracter. Si no, presione enter. "))

def verNotablesJugador(Teams):
    
    for i in range(0,4):
        match i: 
            case 0: 
                ej.verGoleador(Teams,'golesAnotados')
            case 1: 
                ej.verGoleador(Teams,'tarjetasAmarillas')
            case 2: 
                ej.verGoleador(Teams,'tarjetasRojas')
            case 3: 
                ej.verGoleador(Teams,'totalFaltas')
    input('cuando presione enter, será llevago al menú principal')


def verNotablesEquipo(Teams):
    if (len(Teams)>0):
        for i in range(0,6):
            match i:
                case 0:
                    ee.equipoGoleador(Teams,'partidosGanados')
                case 1:
                    ee.equipoGoleador(Teams,'partidosPerdidos')
                case 2:
                    ee.equipoGoleador(Teams,'partidosEmpatados')
                case 3:
                    ee.equipoGoleador(Teams,'golesAFavor')
                case 4:
                    ee.equipoGoleador(Teams,'golesEnContra')
                case 5:
                    ee.equipoGoleador(Teams,'totalPuntos')
    else:
        print("No hay ningún equipo registrado. No se pudieron obtener las estadísticas.")


    

    input('cuando presione enter, será llevago al menú principal')
