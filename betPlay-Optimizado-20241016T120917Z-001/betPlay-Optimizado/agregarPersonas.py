def addTeam (teams:dict):
    switchAddTeam = True
    while (switchAddTeam):
        equipo= str(input("Por favor, ingrese el nombre del equipo que desea agregar a la liga: ")).lower()
        constructor = {
            'nombre': equipo,
            'personal': {
            },
            'jugadores': {

            },
            'estadísticas':{
                'partidosJugados': 0,
                'partidosGanados': 0,
                'partidosPerdidos':0,
                'partidosEmpatados':0,
                'golesAFavor':0,
                'golesEnContra':0,
                'totalPuntos':0,
                'partidosLocal':0,
                'partidosVisitante':0
            }
        }
        teams.update({int(len(teams))+1:constructor})
        print(F'El equipo {equipo} se ha agregado satisfactoriamente.')
        switchAddTeam = bool(input("Si desea agregar otro equippo, presione cualquier tecla. Si no, presione enter."))
    

def addPlayer(teams:dict):
    switchAddPlayers = True
    while  (switchAddPlayers):
        equipo= str(input("Por  favor, ingrese el nombre del equipo al que desea agregar un jugador: ")).lower()
        nombreJugador= str(input("Por favor, ingrese el nombre del jugador: ")).lower()
        numeroJugador= str(input("Por favor, ingrese el número del jugador: "))
        posicionJugador =str(input("Por favor, añada la posición del jugador: "))
        constructor = {
            'nombre': nombreJugador,
            'numero': numeroJugador,
            'posición': posicionJugador,
            'estadísticas':{
                'golesAnotados':0,
                'tarjetasAmarillas':0,
                'tarjetasRojas':0,
                'totalFaltas':0
        }
        }
        if (len(teams)>0):
            for i in range(1,len(teams)+1):
                if equipo in teams[i]['nombre']:
                    teams[i]['jugadores'].update({len(teams[i]['jugadores'])+1:constructor})
                    print(f'el jugador{nombreJugador} ha sido agregado satisfactoriamente al equipo {equipo}')
        else:
            print("No hay equipos para que jugadores puedan ser añadidos. Para añadir jugadores, primero añada un equipo.")

        switchAddPlayers = bool(input("Si desea agregar otro jugador, presione cualquier  tecla. Si no, presione enter."))

def addStaff(teams:dict):
    switchAddStaff = True
    while (switchAddStaff):
        equipo = str(input("Por favor, añada el equipo al cual quiere añadirle el funcionario: "))
        rolFuncionario = str(input("Por favor, añada el rol del funcionario que quiere añadir. Recuerde que los mas comunes son tecnico, asistente, preparadores y cuerpo medico: "))
        nombreFuncionario = str(input("Por favor, añada el nombre del funcionario a añadir"))

        if (len(teams)>0):
            for i in range(1,len(teams[i]['jugadores'])+1):
                if equipo in teams[i]['nombre']:
                    teams[i]['personal'].update({rolFuncionario:nombreFuncionario})
                    print('El funcionario se ha añadido correctamente ')
        else: 
            print("No hay equipos para que jugadores puedan ser añadidos. Para añadir jugadores, primero añada un equipo.")
        
        switchAddStaff = bool(input("Si desea agregar otro miembro al staff, presione  cualquier tecla. Si no, presione enter."))

    


    
        


    





