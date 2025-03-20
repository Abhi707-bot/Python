
# Collection = single "variable" used to store multiple values

# List = [] ordered and changeable. Duplicates OK

# Set = {} unordered and immutable, but Add/Remove OK. No duplicates

# Dictionary : a collection of {key:value} pairs

# Tuple = () ordered and unchageable. Duplicates OK. FASTER



fruits = ['Orange', 'Apple', 'Banana', 'Coconut']

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print('Apple' in fruits)

fruits[0] = 'Pineapple'
fruits.append('Pineapple')
fruits.sort()
fruits.remove("apple")
fruits.insert(0, 'Pineapple')
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))
print(fruits.count('pineapple'))


for fruit in fruits:
    print(fruit, end = " ")


fruits = {'Orange', 'Apple', 'Banana', 'Coconut'}

fruits.remove('Apple')
fruits.add('Pineapple')
fruits.pop()
fruits.clear()

print(fruits)

#for fruit in fruits:
    #print(fruit)


------------------------------------------------------------------

#Shopping Cart Program   ---> PROJECT-1

two cart 

foods and price with list 

while -- bcoz I want to repeat until someone exit from cart
nested if else to break the while loop and customer can add the price of food 
then append those item in the list

for loop to print those item 
-------------------------------------------------------------------

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item (q to quit): ")
    if food == 'q':
        break
    else:
        price = float(input(f'Enter the price of {food}: $'))
        prices.append(price)
        foods.append(food)
        
print("------Your Cart------")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price

print()
print(f"Your total cart price is: ${total}")

--------------------------------------------------------------------



#Dictionary : a collection of {key:value} pairs
              ordered and changeable. No Duplicates

----------------------------------------------------------------

capitals = {'USA': "Washigton D.C.",
            'India': 'Delhi',
            'Russia': 'Moscow'
}
'''
if capitals.get('Japan'):
    print("Capitals does exist")
else:
    print("Capitals doesn't exist")
'''

capitals.update({'Germany':'Berlin'})
capitals.pop('USA')
capitals.popitem()
capitals.clear()

keys = capitals.keys()

for key, value in capitals.items():
    print(f"{key} : {value}")

.get() --- is mainly use to retrieve the value for specified key of dict
           it avoids the error if key is not found 

-----------------------------------------------------------------
### Menu food Program   --> PROJECT-2
-----------------------------------------------------------------

menu = {'pizza': 3.00,
        'nachos':1.29,
        'popcorn':4.50,
        'fries':3.90,
        'chips':1.20,
        'soda':2.00
}

cart = []
total = 0

print("----------- Menu ------------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------- Your Order --------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Your total price of order is: ${total:.2f}")

------------------------------------------------------------------------

### Number Guessing Game  --> PROJECT-3

import random

lowest_num = 1
highest_num =100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("Oops.. Invalid guess!!")
            print(f"Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low.. Try Again!!")
        elif guess > answer:
            print("Too high.. Try Again!!")
        else:
            print(f"CORRECT!! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
        
    else:
        print("Oops.. Invalid Guess!!")
        print(f"Please select a number between {lowest_num} and {highest_num}")


--------------------------------------------------------

### Rock paper game --> PROJECT-4
--------------------------------------------------------

import random

#we used tuple so it will not changed
options = ('rock', 'paper', 'scissors')
running = True

#random.choice will select random choices from tuples
while running:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice (rock, paper, scissors): ')
    
    print(f"player: {player}")
    print(f"computer: {computer}")
    
    if player == computer:
        print("It's Tie!!")
    elif player == 'rock' and computer == 'scissors':
        print("You Win!!")
    elif player == 'paper' and computer == 'rock':
        print("You Win!!")
    elif player == "scissors" and computer == "paper":
        print("You Win!!")
    else:
        print("You lose!!")
    if not input("Play again!! (y/n): ").lower() == 'y':
        running = False
        
print("Thanks for playing!!")
