import random
import string
import os

def ask_name():
    name = input("what is your name? ")
    print("Hello " + name + "!")
    return name

def randomword():
    word_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "words.txt"
    try:
        word_file = open(word_path,"r")
        word_list = word_file.readlines()
        word_file.close()
    except FileNotFoundError:
        word_list = ["banana", "apple", "grape"]

    while True:
        number = round(random.random()*(len(word_list)-1))
        selected = word_list[number].strip()
        if len(selected) < 4:
            continue
    
        return selected.upper()

def word_mask(secretword,picked_letters):
    mask = ""
    for letter in secretword:
        if letter in picked_letters:
            mask = mask + letter
        else:
            mask = mask + "*"
    return mask

def ask_letter():
    while True:
        letter = (input("select a letter ")).upper()
        if (len(letter) != 1):
            print("only input 1 letter at a time ")
            continue
        if not (letter in string.ascii_uppercase):
            print("only input letters")
            continue
        return letter
    
def hangman(secretword, turn=10):
    letters_ok = []
    letters_nok = []

    while turn > 0:
        print("---")
        word_view = word_mask(secretword, letters_ok)
        print(word_view)
        if word_view == secretword:
            print("Congratulations, you have won the game!")
            break
        if len(letters_nok) > 0:
            print("wrong letters guessed:",letters_nok)
        print("you have", turn,"turns left")
        letter = ask_letter()
        if (letter in letters_nok) or (letter in letters_ok):
            print("letter picked already")
            continue
        if letter in secretword:
            print("correct! Please guess the next letter")
            letters_ok.append(letter) 
        else:
            print("wrong!")
            turn = turn -1
            letters_nok.append(letter)
            letters_nok.sort()                  
    if turn == 0:
        print("you are dead! the word you were looking for was", secretword)
    
def yesno (prompt="do you want to try again? "):
    question = input(prompt)
    if question in ("yes","yep","yeah","yup","yea","y"):
        return True 
                  
    else:
        print("Okay, Goodbye! ")
        return False
        
def newgame():
    playagain = yesno("do you want to start a game? ")
    while playagain:
        hangman(randomword())
        playagain = yesno()
            
def main():
    ask_name()
    newgame() 


if __name__ == "__main__":
    main()

