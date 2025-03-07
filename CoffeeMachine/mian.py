from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_sufficient(drinks):
    for item in drinks['ingredients']:
        if drinks['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            resources[item] -= drinks['ingredients'][item]
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.10
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total

def check_enough_money(price_menu,payments):
    if price_menu > payments:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += price_menu
        change = round(payments-price_menu,2)
        print(f"Here is ${change} dollars in change.")
        return True

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_sufficient(drink):
            payment = process_coin()
            if check_enough_money(drink['cost'],payment):
                print(f"Here is your {choice} ☕️. Enjoy!")

