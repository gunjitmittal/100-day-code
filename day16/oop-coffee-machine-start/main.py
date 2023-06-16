from importlib.resources import is_resource
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
umen = Menu()
drink_list = umen.get_items()
machine = CoffeeMaker()
money = MoneyMachine()
on = True
while on:
    choice = input(f"What would you like? {drink_list}:")
    if choice == "report":
        machine.report()
        money.report()
    elif choice == "off":
        on = False
    else:
        drink = umen.find_drink(choice)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
