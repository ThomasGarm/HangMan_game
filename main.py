from function import *
from données import *

user = user_name()

continuer = True

while continuer:
    full_word = computer_word_choice()
    finded_letter = []
    finded_word = recup_secret_word(full_word, finded_letter)
    chances = nb_coups

    while finded_word != full_word and chances>0:
        print("The secret word is {0} (still {1} chances)".format(finded_word, chances))
        letter = recup_letter()
        if letter in finded_letter: # Letter already finded
            print("Already played.")
        elif letter in full_word: # Letter in full_word
            finded_letter.append(letter)
            print("Well done.")
        else:
            chances -= 1
            print("nothing insiiiiiiide !")
        finded_word = recup_secret_word(full_word, finded_letter)

    # when the word is finded or chances = 0
    if finded_word == full_word:
    print("Congratulations ! You have find the word {0}.".format(full_word))
    else:
        print("Wouarghhhhh! Bleuaaaaaarrrrd! HANGED!")

    
    scores[user] += chances #reboot chances

    continue_game = input("Do you want to know more ? (O/N) ?").lower()
    if continue_game == "N"
        continuer = False
    

# La partie est finie, on enregistre les scores
enregistrer_scores(scores)

# On affiche les scores de l'utilisateur
print("Vous finissez la partie avec {0} points.".format(scores[utilisateur]))