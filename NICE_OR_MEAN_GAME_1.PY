##*******************
##NICE OR MEAN GAME 1
##*******************
#Python: 3.9.7
#
#Author: Logan Choate
#
#Purpose: The tech academy  - Python course, creating our first program together.
##            Demonstrating how to pass variable from function to function while
##            producing a fuinctional game.
##
##            Remember, function_name(variable)_means that we pass in the variable.
##            return varaible _means that we are returning the variable back to
##            the calling function.

##this code defines tthe functions that are called later on
def start(nice = 0, mean = 0, name = ""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # Meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name

    if name != "":
        print("\n Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
                if name == "":
                    name = input("\n What is your name? \n>>> ").capitalize()
                    if name != "":
                        print("\n Welcome, {}!".format(name))
                        print("\n In this game, you will be greeted by serveral different people.")
                        print("\n You can choose to be nice or mean.")
                        print("\n At the end of the game your fate will have been sealed by your actions.")
                        stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\n A stranger approaches you for a conversation. \n Will you be nice or mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\n the stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print("\n The stranger glares at you menancingly and storms off...")
            mean = (mean+1)
            stop = False
    score(nice, mean, name) # pass the 3 variables to the "score()" function

def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and({}, Mean)".format(name, nice, mean))

def score(nice, mean, name):
    #score function is being passed to the valuse stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variable so it can use them
        win(nice, mean, name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice, mean, name)
    else:       # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    #substitute the {} wildcards with our variable values
    print("\n Nice job {}, you win! \n Everybody loves you and you've made lots of friends along the way!".format(name))
    #call function again and pass in our variables
    again(nice, mean, name)

def lose():
    # Substitute the {} wildcards with out variable values
    print("\n Ahh to bad, game over! \n {}, you live in a dirty, beat-up van down by the river, \n wretched and alone!".format(name))
    #call again function and pass in our varaibles
    araing(nice, mean, name)
    
def again(nice, mean, name):
        stop = True
        while stop:
            choice = input("\n Do you want to play again? (Y/N):\n>>> ").lower()
            if choice == "y":
                stop = False
                reset(nice, mean, name)
            if choice == "n":
                print("\n So sorry to see you go!")
                stop = False
                quit()
            else:
                print("\n Enter ( Y ) for 'Yes', or ( N ) for 'No':\n>>>")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    # Notice we do not rest the name variable as the same user has elected to play again
    start(nice, mean, name)
    
    

if __name__ == "__main__":
    start()
