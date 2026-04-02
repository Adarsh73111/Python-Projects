import coffee_machine_prj12
from coffee_machine_prj12 import resources,MENU

def is_resource_sufficient(order_ingredients):
    # is_enough = True
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
    #         is_enough = False
    # return is_enough
            return False
    return True

def process_coin():
    print("PLease insert coins")
    total =  int(input("How many quarters?: ")) * 0.25 #cents
    total += int(input("How many dimes?: "))    * 0.10 #cents
    total += int(input("How many nickels?: "))  * 0.05 #cents
    total += int(input("How many pennies?: "))  * 0.01 #cents
    return total

def is_transaction_successful(money_received, drin_cost):
    if money_received >= drin_cost:
        change = round(money_received-drin_cost, 2)
        print(f"Here is ${change} in change.")
        # global profit
        coffee_machine_prj12.profit += drin_cost
        return True
    else:
        print("Sorry that is not enough money. Money Refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}☕")

is_on = True
while is_on:
    choice = input("What would you like? (Espresso / Latte / Cappuccino / Mocha / Flat_White / Macchiato / Americano / Irish_coffee): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:  {resources['water']}ml")
        print(f"Milk:   {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money:  {coffee_machine_prj12.profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]) :
                make_coffee(choice, drink["ingredients"])