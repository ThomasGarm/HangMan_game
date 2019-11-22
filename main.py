from function import *
from données import *

user = user_name()
scores = score_file()
continuer = True

# Si l'utilisateur n'a pas encore de score, on l'ajoute
if user not in scores.keys():
    scores[user] = 0 # 0 point pour commencer


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
        print("Congratulations ! You have find the word: {0}.".format(full_word))
    else:
        print("Wouarghhhhh! Bleuaaaaaarrrrd! HANGED!")

    scores[user] += chances
    save_score(scores)
    show_score()
        
        

    continue_game = input("Do you want to know more ? (N) ?").lower()
    if continue_game == "n":
        continuer = False

