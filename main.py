from function import *
from données import *

user = user_name()

continuer = True

while continuer:
    full_word = computer_word_choice()
    finded_letter = []
    finded_word = recup_secret_word(full_word, finded_letter)
    chances = nb_coups

    while finded_word!= full_word and chances>0:
        print("Mot à trouver {0} (encore {1} chances)".format(finded_word, chances))
        letter = recup_letter()
        if letter in finded_letter: # Letter already finded
            print("Already played.")
        elif letter in full_word: # Letterin full_word
            finded_letter.append(letter)
            print("Well done.")
        else:
            chances -= 1
            print("nothing insiiiiiiide !")
        finded_word = recup_secret_word(full_word, finded_letter)