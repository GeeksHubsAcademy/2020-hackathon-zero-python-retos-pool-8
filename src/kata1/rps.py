from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):

    if (player.lower() == "piedra"):
        if (ai.lower() == "papel"):
            return 'Perdiste!'
        elif (ai.lower() == "tijeras"):
            return 'Ganaste!'
        else : #  caso ai== Papel
            return 'Empate!'

    elif (player.lower() == "papel"):
        if (ai.lower() == "papel"):
            return 'Empate!'  
        elif (ai.lower() == "tijeras"):
            return 'Perdiste!'
        else : #  caso ai== Papel
            return 'Ganaste!'

    elif (player.lower() == "tijeras"):
        if (ai.lower() == "papel"):
            return 'Ganaste!'
        elif (ai.lower() == "tijeras"):
            return 'Empate!'
        else : #  caso ai== Papel
            return 'Perdiste!' 
    else:
        return "Input error-> Vuelve a intentarlo"     


    

# Entry Point
def Game():
    #
    #Seleccion aleatoria de la AI
    ai = options[randint(0, 2)]
    #
    #
    ##print(ai)
    player = input("Elige -'Piedra, papel o tijeras-'\n")
    
    winner = quienGana(player, ai)

    print(winner)



if __name__ == '__main__':
    Game()

