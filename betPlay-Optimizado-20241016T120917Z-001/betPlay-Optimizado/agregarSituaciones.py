def addMatch (Teams):
    switchaddMatch = True 
    while switchaddMatch:
        try:
            switchTeam1 = False 
            switchTeam2 = False 
            equipo1 = str(input("Por favor, ingrese el nombre del primer equipo: ")).lower()
            marcadorEquipo1 = int(input("Por favor, ingrese la cantidad de goles anotador por el primer equipo: "))
            equipo2 = str(input("Por favor, ingrese el nombre del segundo equipo: ")).lower()
            marcadorEquipo2 = int(input("Por favor, ingrese la cantidad de goles anotador por el segundo equipo: "))
            local = str(input("Por favor, ingrese el nombre del equipo que jugó de local: "))
        except:
            input('Los datos ingresados no son adecuados. presione una letra para volverlo a intentar: ')
            addMatch(Teams)

        for i in range (1,len(Teams)+1):
            if (equipo1 in Teams[i]['nombre']):
                switchTeam1 = True
                codigoTeam1 = i
            if (equipo2 in Teams[i]['nombre']):
                switchTeam2 = True
                codigoTeam2 = i
        
        if (switchTeam1==True and switchTeam2==True) and (equipo1==local or equipo2==local):
            Teams[codigoTeam1]['estadísticas']['partidosJugados']+=1  
            Teams[codigoTeam2]['estadísticas']['partidosJugados']+=1
            Teams[codigoTeam1]['estadísticas']['golesAFavor']+=marcadorEquipo1
            Teams[codigoTeam2]['estadísticas']['golesAFavor']+=marcadorEquipo2
            Teams[codigoTeam1]['estadísticas']['golesEnContra']+=marcadorEquipo2
            Teams[codigoTeam2]['estadísticas']['golesEnContra']+=marcadorEquipo1
            if (equipo1==local):
                Teams[codigoTeam1]['estadísticas']['partidosLocal']+=1
                Teams[codigoTeam2]['estadísticas']['partidosVisitante']+=1
            elif (equipo2==local):
                Teams[codigoTeam2]['estadísticas']['partidosLocal']+=1
                Teams[codigoTeam1]['estadísticas']['partidosVisitante']+=1

            if (marcadorEquipo1>marcadorEquipo2):
                Teams[codigoTeam1]['estadísticas'][ 'partidosGanados']+=1
                Teams[codigoTeam1]['estadísticas'][ 'totalPuntos']+=3
                Teams[codigoTeam2]['estadísticas'][ 'partidosPerdidos']+=1
            elif (marcadorEquipo2>marcadorEquipo1):
                Teams[codigoTeam2]['estadísticas'][ 'partidosGanados']+=1
                Teams[codigoTeam2]['estadísticas'][ 'totalPuntos']+=3
                Teams[codigoTeam1]['estadísticas'][ 'partidosPerdidos']+=1
            else:
                Teams[codigoTeam1]['estadísticas'][ 'partidosEmpatados']+=1
                Teams[codigoTeam2]['estadísticas'][ 'partidosEmpatados']+=1
                Teams[codigoTeam1]['estadísticas'][ 'totalPuntos']+=1
                Teams[codigoTeam2]['estadísticas'][ 'totalPuntos']+=1

        else: 
            input("Los equipos ingresados no se pudieron encontrar en nuestros registros. Por favor, inténtelo nuevamente")
        switchaddMatch = bool(input("Si quiere agregar otra fecha, ingrese cualquier caracter. Si no, ingrese enter."))


def addPlayerStatistics(Teams):
    switchPlayerStatistics = True
    while switchPlayerStatistics:
        try:
            equipo= str(input("Por favor, ingrese el nombre del equipo al cual pertenece el jugador: ")).lower()
            nombreJugador= str(input("Por favor, ingrese el nombre del jugador:  ")).lower()
            golesAnotados= int(input("Por favor, ingrese el número de goles anotados: "))
            tarjetasAmarillas= int(input("Por favor, ingrese el número de tarjetas amarillas del jugador: "))
            tarjetasRojas= int(input("Por favor, ingrese el número de tarjetas rojas del jugador. "))
            totalFaltas= int(input("Por favor, ingrese el número total de faltas del jugador: "))
        except:
            input('Los datos ingresados no son aropiados. Por favor, oprima enter y vuélvalo a intentar.')
            addPlayerStatistics(Teams)


        for i in range(1,len(Teams)+1):
                for j in range(1,len(Teams[i]['jugadores'])+1):
                    if (equipo in Teams[i]['nombre'] ) and (nombreJugador in Teams[i]['jugadores'][j]['nombre']):
                        Teams[i]['jugadores'][j]['estadísticas']['golesAnotados']+=golesAnotados
                        Teams[i]['jugadores'][j]['estadísticas']['tarjetasAmarillas']+=tarjetasAmarillas
                        Teams[i]['jugadores'][j]['estadísticas']['tarjetasRojas']+=tarjetasRojas
                        Teams[i]['jugadores'][j]['estadísticas']['totalFaltas']+=totalFaltas
                        print("Los datos se han añadido correctamente.")
                        
        
        switchPlayerStatistics = bool(input("Si desea seguir añadiendo estadísticas, presione cualquier caracter. Si no, presione enter."))

                    
    





