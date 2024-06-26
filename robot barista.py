#this is a robot barista code for my coffee shop
print("Welcome to J.K coffee shop")
name = input("What is your name? ")

while name == "":
    name = input("Dear customer you have not entered your name. Please try again. ")

if name == 'BEN' or name == 'ben':
    status = input('Are you evil?YES/NO ')
    good_deeds = int(input("Enter the number of good deed that you have done "))

    if status == 'YES' or name == 'yes' :
        if good_deeds <= 4:

            exit(f'sorry {name} but you are not qualified')
    else:
        print(f'{name} welcome')

menu = '(1)apple\n(2)chapati\n(3)black coffee'
order = int(input(f"{name.capitalize()} what would you like to order?\n USE NUMBERS TO ORDER.\n {menu}"))

while order == "":
    order = int(input(f"{name.capitalize()} you have not made any order.\n TRY AGAIN.\n USE NUMBERS TO ORDER"))

if order == 1:
    price = 10
    title = 'apple'
elif order == 2:
    price = 20
    title = 'chapati'
elif order == 3:
    price = 30
    title = 'black coffee'
else:
    print(f'sorry dont have that.')
    exit()

quantity = int(input(f'how many of {title} do you want?'))

total = price * quantity
print(total)

