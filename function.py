import os
import pickle
from random import choice
from données import *

#using pickle for create, save and display player's score
def score_file():
    score = {}
    save= open("PenduGame/score_file", "wb")
    pickle.dump(score, save)
    save.close()
    return score

def save_score(scores):
    save = open("PenduGame/score_file", "wb")
    pickle.dump(scores, save)
    save.close()

def show_score():
    load = open("PenduGame/score_file", "rb")
    result = pickle.load(load)
    print(result)


def user_name():
    user=input("choose your name")
    while control_user_name(user) is False:
        print("minimum 2 caractères et maxi 4")
        user=input("choose your name")
    return user


def control_user_name(user):#conditions for the name
    try:
        assert len(user) >1 and len(user) < 4
    except AssertionError as a:
        return False


def computer_word_choice(): #from file données.py
    return choice(word_list)

def recup_letter():# input from player
    letter = input("Tap a letter: ").lower()
    if len(letter)>1 or not letter.isalpha():
        print("wrong entry, choose one letter")
        return recup_letter()
    else:
        return letter

def recup_secret_word(full_word, finded_letter): #function for adding letter
    secret_word = ""
    for letter in full_word:
        if letter in finded_letter:
            secret_word += letter
        else:
            secret_word += "*"
    return secret_word