import random
number = random.randint(1,100)

player_name = input("Hello, what is your name? ")
number_of_guesses = 0
print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number between 1 and 100 then you will guess, alright? \nDon\'t forget! You have only 10 chances so guess:'.format(player_name))

while number_of_guesses < 10:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
        print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
if guess == number:
    print('Congratulations {}, you guessed the number in {} tries!'.format(player_name, number_of_guesses))
else:
    print('You couldn\'t guess the number.\nGame Over \nWell, the number was {}.\nTry again'.format(number))
