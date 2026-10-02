# Prices
burger = 80
pizza = 150
chicken = 120
spaghetti = 100
drinks = 50


def ask_order():
    choice = int(input("\nEnter your order (1-5): "))
    quantity = int(input("Enter quantity: "))
    return choice, quantity


def calculate_total(choice, quantity):
    total = 0

    if choice == 1:
        total = burger * quantity
        print("You ordered Burger.")

    elif choice == 2:
        total = pizza * quantity
        print("You ordered Pizza.")

    elif choice == 3:
        total = chicken * quantity
        print("You ordered Fried Chicken.")

    elif choice == 4:
        total = spaghetti * quantity
        print("You ordered Spaghetti.")

    elif choice == 5:
        total = drinks * quantity
        print("You ordered Soft Drinks.")

    else:
        print("Invalid choice!")
        total = 0

    return total