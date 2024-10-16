import os 
import agregarPersonas as ae
import agregarSituaciones as ads
import verEstadisticas as ve
ligaBetplay = {}

def menuPrincipal(diccionarioLiga):
    os.system('clear')
    optionMenu = int(input("""Por favor, ingrese alguna de las siguientes opciones:
                           1. Agregar equipo.
                           2. Agregar jugadores.
                           3. Agregar cuerpo técnico
                           4. Agregar fecha
                           5. Agregar estadísticas de jugadores
                           6. Ver estadísticas generales de un equipo
                           7. Ver estadísticas relevantes de equipos
                           8. Ver estadísticas relevantes de jugadores
                           9.Salir
                           """ ))
    
    match optionMenu:
        case 1: 
            os.system('clear')
            ae.addTeam(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 2: 
            os.system('clear')
            ae.addPlayer(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 3: 
            os.system('clear')
            ae.addStaff(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 4: 
            os.system('clear')
            ads.addMatch(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 5: 
            os.system('clear')
            ads.addPlayerStatistics(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 6: 
            os.system('clear')
            ve.verEstadisticasEquipo(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 7: 
            os.system('clear')
            ve.verNotablesEquipo(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 8: 
            os.system('clear')
            ve.verNotablesJugador(ligaBetplay)
            menuPrincipal(ligaBetplay)
        case 9: 
            os.system('clear')
            print("El programa ha terminado, Gracias por participar en la liga betplay.")
            
        case _: 
            os.system('clear')
            input("Ninguna de las opciones coincide con el valor ingresado. Presione cualquier caracter para volver al menù principal")
            menuPrincipal(ligaBetplay)

menuPrincipal(ligaBetplay)