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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def menu_cost():
    """print items on menu and their cost"""
    print("=== MENU ===")
    for item in MENU:
        item_cost = MENU[item]["cost"]
        print(f"{item}: ${item_cost}")


# TODO: 3. check to see if resources are sufficient
def check_inv(order):
    """takes user's order and check to see if there's sufficient amount of resource inventory"""
    for items in MENU:
        if order == items:
            recipe = MENU[items]["ingredients"]
            # print(recipe)
            for i in recipe:
                if recipe[i] > resources[i]:
                    print(f"sorry, there's not enough {i}.")
                else:
                    resources[i] -= recipe[i]

# check_inv(order)


# TODO: 4. process coins
def payment(order):
    order_cost = MENU[order]["cost"]
    input("Please insert coins.")
    quarter = int(input("how many quarters? "))
    dime = int(input("how many dime? "))
    nickle = int(input("how many nickle? "))
    penny = int(input("how many penny? "))
    payment_total = round((quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01), 2)
    # TODO 5. check transaction successful
    if payment_total >= order_cost:
        global profit
        profit += order_cost
        change = round(float(payment_total - order_cost), 2)
        print(f"Here's ${change} in change")
        print(f"Here is your {order} ☕ Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded")


# payment(order)


def coffee_machine():
    machine_if_off = False
    while not machine_if_off:
        menu_cost()
            # TODO: 1. print report of the resources
        order = (input("What would you like? (espresso/latte/cappuccino) "))
        if order == "report":
            for ingredients in resources:
                print("{}: {}".format(ingredients, resources[ingredients]))
            print(f"money: {profit}")
        elif order == "off":
            machine_if_off = True
            exit()
        else:
            check_inv(order)
            payment(order)


coffee_machine()
