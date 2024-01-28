from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_card = Menu()
coffee_making = CoffeeMaker()
money = MoneyMachine()
is_on = True

coffee_making.report()
money.report()

while is_on:
    options = menu_card.get_items()
    take_order = input(f"What would you like to drink ({options}): ")
    if take_order == "off":
        is_on = False
    elif take_order == "report":
        coffee_making.report()
        money.report()
    else:
        drink = menu_card.find_drink(take_order)
        if coffee_making.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_making.make_coffee(drink)




