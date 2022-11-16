from data import MENU, resources

money = 0
machine_active = True

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"\nSorry there is not enough {item}.\n")
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
        print(f"Your change is ${change:.2f}.\n")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Your payment has been refunded.\n")
        return False

def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. DRINK IS HOT! Please enjoy safely.\n")

while machine_active:
    print("Welcome to the coffee machine! ☕")
    customer_choice = input("What drink would you like? (espresso/latte/cappuccino): ")
    if customer_choice == "off":
        machine_active = False
    elif customer_choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}\n")
    elif customer_choice == "service":
        print("\n⚙️ Machine serviced! 🔧 \n")
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    else:
        drink = MENU[customer_choice]
        if check_resources(drink["ingredients"]):
            payment = request_payment()
            if process_payment(payment, drink["cost"]):
                make_drink(customer_choice, drink["ingredients"])