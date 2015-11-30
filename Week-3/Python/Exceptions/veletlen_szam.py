# def get_integer():
# return a number
from random import randint

number_to_guess = randint(0, 10)

number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = int(input("Enter an integer:"))
    except ValueError:
        print("You have to enter a number.")
    else:
        print("Koszi")
        if  guess == number_to_guess:
            print("Congratulations! You won.")
            break
        else:
            print("Bzzz!Wrong answer")
            if guess < number_to_guess:
                print("Think bigger!")
            else:
                print("You're a bit over!")
            print("You have still " + str(number_of_guesses) + " guesses")    
            number_of_guesses -= 1

if number_of_guesses == 0:
    print("Sorry!You lost")
