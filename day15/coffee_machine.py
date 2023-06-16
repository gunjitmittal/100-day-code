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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resources():
    for i in resources:
        if i == "water" or i == "milk":
            unit = "ml"
        else:
            unit = "gm"
        print(f"{i}: {resources[i]}{unit}")


def deduct_resources(choice):
    for i in MENU[choice]["ingredients"]:
        resources[i] -= MENU[choice]["ingredients"][i]


def check_sufficient(choice):
    for i in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        else:
            return True


machine_money = 0
on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        print_resources()
        print(f"Money: ${machine_money}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_sufficient(choice):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money = quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
            if money < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                machine_money += MENU[choice]["cost"]
                change = round(money - MENU[choice]["cost"], 2)
                if change != 0:
                    print(f"Here is ${change} in change.")
                deduct_resources(choice)
                print(f"Here is your {choice} ☕️ Enjoy!")
    elif choice == "off":
        on = False
