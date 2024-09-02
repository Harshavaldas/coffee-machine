menu = {"espresso": {"ingredients": {"water": 50,"coffee": 18, },
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def sub(we):
    if we == "espresso":
        a = resources['water'] - menu[we]['ingredients']['water']
        c = resources['coffee'] - menu[we]['ingredients']['coffee']
        resources['water'] = a
        resources['coffee'] = c
    else:
        a = resources['water'] - menu[we]['ingredients']['water']
        b=resources['milk']-menu[we]['ingredients']['milk']
        c = resources['coffee'] -menu[we]['ingredients']['coffee']
        resources['water'] = a
        resources['milk'] = b
        resources['coffee'] = c
def check(we):
    if we=="espresso":
        if resources['water'] < menu[we]['ingredients']['water']:
            return True
        elif resources['coffee']<menu[we]['ingredients']['coffee']:
            return True
    else:
        if resources['water']<menu[we]['ingredients']['water']:
            return True
        elif resources['milk']<menu[we]['ingredients']['milk']:
            return True
        elif  resources['coffee']<menu[we]['ingredients']['coffee']:
            return True
def coins(we):
    print("please insert coins")
    quarter=int(input("please enter quarters"))
    dimes = int(input("please enter dimes"))
    nickels =int(input("please enter nickels"))
    pennies= int(input("please enter pennies"))
    cash=round(0.25 * quarter + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies)
    if cash<menu[we]['cost']:
        return True
    elif cash>menu[we]['cost']:
        change=cash-menu[we]['cost']
        print(f"here is ur change ${change}")
        print(f"Please enjoy your {we}")
    elif cash==menu[we]['cost']:
        print(f"Please enjoy your {we}")
def profit(we):
    global nomey
    nomey=nomey+float(menu[we]['cost'])
    resources['money']=nomey
nomey=0
start=True
while start is True:
    display=input("what would you like?espresso/latte/cappuccino")
    if display=="report":
        print(f"water:{resources['water']} milk:{resources['milk']} coffee:{resources['coffee']}")
    elif display=="espresso":
        w=check(we=display)
        if w is True:
            print("sorry the water is not available")
        else:
            q=coins(we=display)
            if  q is True:
                print("insufficient funds money is refunded")
            else:
                profit(we=display)
                sub(we=display)
    elif display=="latte":
        w=check(we=display)
        if w is True:
            print("sorry the water is not available")
        else:
            q=coins(we=display)
            if q is True:
                print("insufficient funds money is refunded")
            else:
                profit(we=display)
                sub(we=display)
    elif display=="cappuccino":
        w=check(we=display)
        if w is True:
            print("sorry the water is not available")
        else:
            q=coins(we=display)
            if q is True:
                print("insufficient funds money is refunded")
            else:
                profit(we=display)
                sub(we=display)
    print(resources)
