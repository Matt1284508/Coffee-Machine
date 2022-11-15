from data import MENU, resources

money = 0
machine_active = True
user_selection = ""

def report():
    print(f"Water: {water_resource}ml")
    print(f"Milk: {milk_resource}ml")
    print(f"Coffee: {coffee_resource}g")
    print(f"Money: ${money}")

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def request_payment():
    print("Please make payment.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def process_payment(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. DRINK IS HOT! Please enjoy safely.")
