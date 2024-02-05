from dict import *
import random
import os

clear = lambda: os.system('cls') # Очищение консоли
def gallows_start():
    clear()
    print("Привет! Это игра под названием виселица")
    word = dictionary[random.randint(0,(len(dictionary)-1))] # Выбор слова
    word_arr = list(word)
    guess = list("_"*len(word))
    attempt_counter = 5 # Счетчик попыток
    print("_"*len(word), "|", len(word), "букв\n")
    while guess!=word_arr:
        print ("Осталось попыток: ", attempt_counter, "\n")
        inputed_letter=(input("Введите букву - ")).lower()
        # Проверка на наличие буквы в загаданном слове
        if inputed_letter in word_arr:
            clear()
            x = [i for i, ltr in enumerate(word_arr) if ltr == inputed_letter] # Нахождение всех повторяющихся букв
            for j in x: # Вставка в guess
                guess[j] = inputed_letter
            print("".join(guess)) # Вывод
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
            if attempt_counter == 0: print ("\nЭто слово:", word)   
        if attempt_counter == 0:
            print("К сожалению, тебя повесили.")
            break
    if guess==word_arr:
        print("Поздравляю, ты победил!")
choice = "да"
while True:
    choice = input("Хотите ли вы начать игру? да/нет:").lower()
    if choice!="да" and choice!="нет":
        print("Ты сказал что-то не то.")
    elif choice=="нет":
        clear()
        break
    else:
        gallows_start()
