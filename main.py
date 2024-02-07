from dict import *
import random
import os

clear = lambda: os.system('cls') 

def get_random_word():
    return random.choice(dictionary)

def check_inputed_letter(word_arr, inputed_letter):
    return [i for i, ltr in enumerate(word_arr) if ltr == inputed_letter]

def check_char(inputed_letter):
    return inputed_letter.isalpha() and len(inputed_letter) == 1 and not inputed_letter.isdigit()

def play_again():
    ask = input("Хотите ли вы начать игру вновь? [да/нет]:").lower()
    
    return ask == "да"

def gallows_loop():
    clear()
    word = get_random_word()
    word_arr = list(word)
    guess = list("_"*len(word))
    
    attempt_counter = 0
    if len(word)>=7:
        attempt_counter = 10
    else:
        attempt_counter = 5
    print("".join(guess), "|", len(word), "букв\n")
    
    while guess!=word_arr:
        print ("Осталось попыток: ", attempt_counter, "\n")
        inputed_letter=(input("Введите букву - ")).lower()
        if check_char(inputed_letter):
            if inputed_letter in word_arr:
                clear()
                x = check_inputed_letter(word_arr, inputed_letter)
                
                for j in x: 
                    guess[j] = inputed_letter
                print("".join(guess))
            else:
                clear()
                print("".join(guess))
                attempt_counter-=1
                print ("Не угадал")
                if attempt_counter < 5: print ("  | ")
                if attempt_counter < 4: print ("  O ")
                if attempt_counter < 3: print (" /|\ ")
                if attempt_counter < 2: print ("  | ")
                if attempt_counter < 1: print (" / \ ")
                if attempt_counter == 0:
                    print("К сожалению, тебя повесили.")
                    if play_again():
                        gallows_loop()
                    else:
                        clear()
                        exit()
        else:
            print("Некорректный ввод")
            
    else:
        print("Поздравляю, ты победил!")  
        if play_again():
            gallows_loop()
        else:
            clear()
            exit()   

if __name__ == '__main__':
    gallows_loop()