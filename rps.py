from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.lower()
    ai = ai.lower()
    if(player == "Piedra"):
        if(ai=="Piedra"):
            return "Empate!"
        elif(ai=="Papel"):
            return "Perdiste!"
        else: 
            return "Ganaste!"
    elif(player == "Papel"):
        if(ai=="Papel"):
            return "Empate!"
        elif(ai=="Tijeras"):
            return "Perdiste!"
        else: 
            return "Ganaste!"

    elif(player == "Tijeras"):
        if(ai=="Tijeras"):
            return "Empate!"
        elif(ai=="Piedra"):
            return "Perdiste!"
        else: 
            return "Ganaste!"

# Entry Point
def Game():
    #
    #
    
    #
    #
    player = input("Elije Piedra, Papel o Tijeras: ")
    ai =["Piedra","Papel","Tijeras"]
    ai = random.choice(list(ai))
    winner = quienGana(player, ai)

    print(winner)

