"""A number-guessing game."""

# Put your code here
import random
print("Welcome to guessing name")
name = (input("Hello, Whats your name? "))
correct_num = random.randint(1, 5)
wrong_guesses = 1

while True:
    chosen_num = int(input(f"{name}, please choose number between 1-5: "))
    
    if chosen_num != correct_num:
        
        if chosen_num < correct_num:
            print(f'Your guess? {chosen_num}')
            print ("Your guess is too low, try again!")
        elif chosen_num > correct_num:
            print(f'Your guess? {chosen_num}')
            print ("Your guess is too high, try again!")       
        wrong_guesses +=1    
        
    else:
        print (f"Well done {name}! You found my number in {wrong_guesses} tries!")
        break 
