from data import MENU, resources

water_resource = resources["water"]
milk_resource = resources["milk"]
coffee_resource = resources["coffee"]
money = 0
machine_active = True

def report():
    print(f"Water: {water_resource}ml")
    print(f"Milk: {milk_resource}ml")
    print(f"Coffee: {coffee_resource}g")
    print(f"Money: ${money}")

while machine_active:    
    user_selection = input("What would you like? (espresso/latte/cappuccino): ")

    if user_selection == "off":
        machine_active = False
    elif user_selection == "report":
        print(report())
    else:
        # check_resources()
        # process_payment()
        # make_coffee()

# TODO: Check if resources are sufficient

# TODO: Process payment

# TODO: Check if transaction is successful

# TODO: If resources are sufficient and trans is successful, make coffee

# TODO: Print thank you/enjoy message and loop back to selection prompt

# Coffee Emoji: ☕