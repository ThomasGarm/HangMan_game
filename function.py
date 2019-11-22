import os
import pickle
from random import choice
from données import *

def user_name():#call for game  user
    while control_user_name(user) is False:
        print("minimum 2 caractères et maxi 4")
        user=input("choose your name")
    return user


def control_user_name(user):#conditions for the name
    try:
        assert len(user) >1 and len(user) < 4
    except AssertionError as a:
        return False


def recup_scores():
    if os.path.exists(my_score_file): 
        fichier_scores = open(my_score_file, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else:
        scores = {}
    return scores

def enregistrer_scores(scores):
    fichier_scores = open(my_score_file, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

def computer_word_choice():
    return choice(word_list)

def recup_letter():
    letter = input("Tap a letter: ").lower
    if len(letter)>1 or not letter.isalpha():
        print("wrong entry, choose one letter")
        return recup_letter()
    else:
        return letter

def recup_secret_word(full_word, finded_letter):
    secret_word = ""
    for letter in full_word:
        if letter in finded_letter:
            secret_word += letter
        else:
            secret_word += "*"
    return secret_word