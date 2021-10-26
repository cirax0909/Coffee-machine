from data import MENU
from data import resources
money = 0
resource_water = resources['water']
resource_milk = resources['milk']
resource_coffee = resources['coffee']


def check_resource(resource_water, resource_milk, resource_coffee, option):
    if option == 'espresso':
        if resource_water >= 50 and resource_coffee >= 18:
            print('enough')
        elif resource_water < 50 and resource_coffee >= 18:
            print('Sorry. Not enough water')
        else:
            print('Sorry. Not enough coffee')
    elif option == 'latte':
        if resource_water >= 200 and resource_milk >= 150 and resource_coffee >= 24:
            print('enough')
        elif resource_water < 200 and resource_milk >= 150 and resource_coffee >= 24:
            print('Sorry. Not enough water')
        elif resource_water >= 200 and resource_milk < 150 and resource_coffee >= 24:
            print('Sorry. Not enough milk')
        else:
            print('Sorry. Not enough coffee')
    elif option == 'cappuccino':
        if resource_water >= 250 and resource_milk >= 150 and resource_coffee >= 24:
            print('enough')
        elif resource_water < 200 and resource_milk >= 150 and resource_coffee >= 24:
            print('Sorry. Not enough water')
        elif resource_water >= 200 and resource_milk < 150 and resource_coffee >= 24:
            print('Sorry. Not enough milk')
        else:
            print('Sorry. Not enough coffee')


def payment(cost):
    quarter = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01
    print("Please insert coins.")
    quarter_quan = int(input('how many quarters?:'))
    dimes_quan = int(input('how many dimes?:'))
    nickles_quan = int(input('how many nickles?:'))
    pennies_quan = int(input('how many pennies?:'))
    money_receive = float(quarter * quarter_quan + dimes_quan * dimes + nickles * nickles_quan + pennies * pennies_quan)
    change = money_receive - cost
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${change} in change.")


machine_on = True
while machine_on:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    check_resource(resource_water, resource_milk, resource_coffee, option)
    if option == 'off':
        machine_on = False
    elif option == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['water']}\n")
    elif option == 'espresso':
        cost = MENU['espresso']['cost']
        payment(cost)
    elif option == 'latte':
        cost = MENU['latte']['cost']
        payment(cost)
    elif option == 'cappuccino':
        cost = MENU['cappuccino']['cost']
        payment(cost)

