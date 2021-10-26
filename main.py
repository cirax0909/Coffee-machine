from data import MENU
from data import resources

money_receive = 0

def check_resource(resources, option, money_receive):
    if option == 'espresso':
        if resources['water'] >= 50 and resources['coffee'] >= 18:
            resources['water'] -= 50
            resources['coffee'] -= 18
            cost = MENU['espresso']['cost']
            money_receive += payment(cost, money_receive)
            print('Here is your espresso ☕. Enjoy!')
        elif resources['water'] < 50 and resources['coffee'] >= 18:
            print('Sorry. Not enough water')
        else:
            print('Sorry. Not enough coffee')
    elif option == 'latte':
        if resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
            cost = MENU['latte']['cost']
            money_receive += payment(cost, money_receive)
            print('Here is your latte ☕️. Enjoy!')
        elif resources['water'] < 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            print('Sorry. Not enough water')
        elif resources['water'] >= 200 and resources['milk'] < 150 and resources['coffee'] >= 24:
            print('Sorry. Not enough milk')
        else:
            print('Sorry. Not enough coffee')
    elif option == 'cappuccino':
        if resources['water'] >= 250 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
            cost = MENU['cappuccino']['cost']
            money_receive += payment(cost, money_receive)
            print('Here is your cappuccino ☕️. Enjoy!')
        elif resources['water'] < 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            print('Sorry. Not enough water')
        elif resources['water'] >= 200 and resources['milk'] < 150 and resources['coffee'] >= 24:
            print('Sorry. Not enough milk')
        elif resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] < 24:
            print('Sorry. Not enough milk')
        else:
            print('Sorry. Not enough milk and water')
    return money_receive


def payment(cost, money_receive):
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
    change = round(money_receive - cost, 2)
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${change} in change.")
    return money_receive


machine_on = True
while machine_on:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == 'off':
        machine_on = False
    elif option == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money_receive}")
    elif option == 'espresso':
        money_receive = check_resource(resources, option, money_receive)
    elif option == 'latte':
        money_receive = check_resource(resources, option, money_receive)
    elif option == 'cappuccino':
        money_receive = check_resource(resources, option, money_receive)
