from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()  # Object created and stored inside money_machine
coffee_maker = CoffeeMaker()  # Object created and stored inside coffee_maker
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items() #Saves the list of all the options in menu to the variable menu
    choice = input(f"What would you like? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()  # Taps into coffee_maker and pulls out the report
        money_machine.report()  # taps into money_machine and pulls out the report
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

