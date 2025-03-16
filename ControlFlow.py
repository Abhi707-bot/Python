## Control Flow:
     Conditional statements (if/else)
     Loops (for, while)
     Functions and arguments
     Exception handling (try/except)
	 
--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

# If = do something only IF some conditionsis True
       Else do something else

age = int(input('Enter your age: '))

if age>= 18:
    print('You are now signed up!')
else:
    print('You are underage and sorry!')


response = input('Would you like food (Y/N): ')

if response == 'Y' or response == 'y':
    print('Have some food!')
else: 
    print('No food for you!')


name = input('Enter your name: ')

if name == '':
    print('You did not type in your name!')
else:
    print(f'Hello {name}')


online = True

if online:
    print('User is online')
else:
    print('User is offline')


operator = input("Enter the given operator (+ - * /): ")

----------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

#Python Calculator

if operator == '+' or operator == '-' or operator ==  '*' or operator == '/':
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    
    if operator == '+':
        res = num1 + num2
        print(round(res))
    elif operator == '-':
        res = num1 - num2
        print(round(res))
    elif operator == '*':
        res = num1 * num2
        print(round(res))
    elif operator == '/':
        res = num1 / num2
        print(round(res))
else:
    print('enter the given operator only!')

----------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

#Python weight calculator

weight = float(input("Enter your weight: "))


unit = input("Kilograms or Pounds? (Kg or L): ")

if unit == 'Kg' or unit == 'kg' or unit == 'l' or unit == 'L':
    if unit == 'Kg':
        weight = weight * 2.205
        unit = 'Lbs.'
    elif unit == 'L':
        weight = weight / 2.205
        unit = 'Kgs.'
    print(f"Your weight is: {round(weight,2)} {unit}")
else:
    print(f"{unit} was not valid")


unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

temp = float(input("Enter the temp: "))

if unit == 'C':
    temp = round((9*temp)/5 + 32, 1)
    print(f"The temp in Fahrenheit is: {temp} deg F")
elif unit == 'F':
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temp in Celsius is: {temp} deg C")
else:
    print(f"{unit} is invalid of measurement")

----------------------------------------------------------------------------

#logical operators = evaluate multiple conditions (or, and, not)
                    or = at least one condition must be True
                    and = both conditions must be True
                    not = inverts the condition (not False, not True)


temp = 26

is_raining = False

if temp > 30 or temp < 0 or is_raining:
    print('The outdoor event is cancelled')
else:
    print('The outdoot event is still scheduled')


temp = 30

is_sunny = False

if temp>= 28 and is_sunny:
    print('The outside weather is too Hot')
elif temp<=0 and is_sunny:
    print('It is cold outside')
elif temp>= 28 and not is_sunny:
    print('The outside weather is too Hot')
    print('It is cloudy')
elif temp<=0 and not is_sunny:
    print('It is cold outside')
    print('It is cloudy')
    

----------------------------------------------------------------------------

#Conditional operators = one-line shortcut for the if-else statement (ternary operator)
print or assign one of two values based on a condition
X if condition else Y



num = 5

a = 9
b = 7

age = 25

temp =25

#print("Positive" if num > 0 else 'Negative')
#result = 'Even' if num % 2 == 0 else 'Odd'

#max_num = a if a>b else b
#min_num = a if a<b else b

#status = 'Adult' if age>=18 else 'Child'

weather = 'Hot' if temp >20 else 'Cold'

print(weather)


#String Methods

name = input('Enter your name: ')

#result = len(name)
#result = name.find("c")
#result = name.rfind("o")
name=name.capitalize()

print(name)

-- print(help(str))

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can not be more than above 12 char")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")


--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------



# While loop = execute some code WHILE some condition remains true

------------------------------------------------------------------
name = input('Enter your name: ')

while name == '':
    print('You did not enter name')
    name = input('Enter your name: ')
print(f"Welcome {name}")

---------------------------------------------------------------
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"you like {food} ")
    food = input("Enter a another food you like (q to quit): ")
print("Bye")

-----------------------------------------------------------------
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the priciple amount: "))
    if principle < 0:
        print("Principle can't be less than 0")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate can't be less than 0")
    else:
        break
        
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than 0")
    else:
        break

total = principle * pow((1+ rate/100), time)

print(f"Balance after {time} year/s: ${total:.2f}")

---------------------------------------------------------------

********************************---------****************************

# For loops = execute a block of code a fixed no. of times
              You can iterate over a range, strings, sequence, etc.

---------------------------------------------------------------------

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

------------------------------------------------------------------

# Countdown timer

import time 

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int((x /60) % 60)
    hours = int(x /3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
print("Time's UP")


********************************---------****************************

# Nested loops

A loop within another loop (outer, inner)

outer loop:
    inner loop:

-------------------------------------------------------

rows = int(input("Enter the # of rows: "))
col = int(input("Enter the # of col: "))
symbol = input("Enter the symbol: ")

for x in range(rows):
    for y in range(col):
        print(symbol, end="")
    print()
    
    
--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------   

# function = A block of reusable code
             place () after the function name to invoke it
--------------------------------------------------------------------------------------------

def happy_birth(name, age):
    print(f"Happy birthday to {name}!!")
    print(f"you are {age} years old!!")
happy_birth('Bro', 20)
happy_birth('steve', 30)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
display_invoice("BroCode", 56.90, "01/01")

--------------------------------------------------------------

# Return = statement used to end a function 
           and send a result back to caller
--------------------------------------------------------------------------------------------

def add(x, y):
    z = x + y
    return z
    
def subs(x, y):
    z = x - y
    return z
    
print(subs(1,2))


def capital_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
    
full_name = capital_name("bro", "code")

print(full_name)

-------------------------------------------------------------------

# Default arguments = A default value for certain parameters
                      Default is used when that argument is omitted
                 make your functions more flexible, reduces # of arguments

1. positional 2. default 3 keyword 4 arbitrary

--------------------------------------------------------------------------------------------

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 - tax)
    
print(net_price(500))


import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")
count(10)

----------------------------------------------------------------------

# Keyword arguments = an argument preceded by an identifier
                      helps with readability
                      order of arguments doesn't matter
                      1. positional 2. dafault 3. keyword 4. arbitrary
                      
--------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------

# Exception = An event that interrupts the flow of a program 
              (ZeroDivisionError, TypeError, ValueError)
              
              1. try, 2. except, 3. finally
              
              
try:
    # Try some code
    
except Exception:
    # Handle an Exception
    
finally:
    # Do some clean up
    
    
try:
    num = int(input("Enter a num: "))
    print(1/num)
    
except ZeroDivisionError:
    print("You can't divide by zero sorry!")
    
except ValueError:
    print("Enter only valid number!")

except Exception:
    print("Something went wrong!")

finally:
    print("Do some clean up")