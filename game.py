"""A number-guessing game."""

# Put your code here
import random
print("Welcome to guessing game!")
name = (input("Hello, Whats your name? "))
correct_num = random.randint(1, 5)
wrong_guesses = 1

while True:
    chosen_num = input(f"{name}, please choose number between 1-5: ")
    try:
        num = int(chosen_num)
    except ValueError:
        print("Error! Must be numbers")
        continue

    if num < 1 or num > 5:
        print("Error! Try again")
        
    if num != correct_num:
        
        if num < correct_num:
            print(f'Your guess? {num}')
            print ("Your guess is too low, try again!")
        elif num > correct_num:
            print(f'Your guess? {num}')
            print ("Your guess is too high, try again!")       
        wrong_guesses +=1    
            
    else:
        print (f"Well done {name}! You found my number in {wrong_guesses} tries!")
        break        