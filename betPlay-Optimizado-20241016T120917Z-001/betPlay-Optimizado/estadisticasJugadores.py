def verGoleador(Teams, estadistica:str):
    totalJugadoresYGoles ={}
    totalGolesJugadores =[]
    for i in range(1,len(Teams)+1):
        for j in range(1,len(Teams[i]['jugadores'])+1):
            nombre = Teams[i]['jugadores'][j]['nombre']
            goles = Teams[i]['jugadores'][j]['estadísticas'][estadistica]
            totalJugadoresYGoles.update({nombre:goles})
            totalGolesJugadores.append(goles)
    golesMasAltos = max(totalGolesJugadores)
    jugadorGoleador = None
    for k,v in totalJugadoresYGoles.items():
        if v == golesMasAltos:
            jugadorGoleador = k
    print(f'El jugador con el mayor número de {estadistica} fue {jugadorGoleador}')



