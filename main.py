from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine() #Object created and stored inside money_machine
coffee_maker = CoffeeMaker() #Object created and stored inside coffee_maker

coffee_maker.report() #Taps into coffee_maker and pulls out the report
money_machine.report() #taps into money_machine and pulls out the report