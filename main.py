from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu=Menu()

while True:
    options=menu.get_items()
    choice = input(f"What would you like 🤔 ({options})? ")
    if choice == "off":
        print("Goodbye!👋")
        break
    elif choice == "report":
        coffee_maker.report()
    elif choice == "menu":
        print(menu.get_items())
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

