from function import *
from données import *

user = user_name()

continuer = True

while continuer:
    full_word = computer_word_choice()
    finded_letter = []
    finded_word = recup_secret_word(full_word, finded_letter)
    chances = nb_coups