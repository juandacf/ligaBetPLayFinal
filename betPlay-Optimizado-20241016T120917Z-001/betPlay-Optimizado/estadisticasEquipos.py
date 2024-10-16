def equipoGoleador(Teams, estadistica):
    totalEquiposYgoles = {}
    totalGoles = []
    for i in range(1,len(Teams)+1):
        nombreEquipo=Teams[i]['nombre']
        golesEquipo=Teams[i]['estadísticas'][estadistica]
        totalEquiposYgoles.update({nombreEquipo:golesEquipo})
        totalGoles.append(golesEquipo)
    golesAltos = max(totalGoles)
    equipoGoleador = None
    for k,v in totalEquiposYgoles.items():
        if v==golesAltos:
            equipoGoleador= k
    
    if (estadistica=='partidosPerdidos'):
        print(f'El equipo que ocupa el último lugar de la tabla de posiciones es {equipoGoleador}')
    else:
        print(f'El equipo con el mayor número de {estadistica}  fue {equipoGoleador}')




