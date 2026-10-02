print("===================================")
print("   WELCOME TO OUR RESTAURANT")
print("===================================")

# Menu
print("\n------------- MENU -------------")
print("1. Burger       - PHP 80")
print("2. Pizza        - PHP 150")
print("3. Fried Chicken- PHP 120")
print("4. Spaghetti    - PHP 100")
print("5. Soft Drinks  - PHP 50")
print("--------------------------------")

# Prices
burger = 80
pizza = 150
chicken = 120
spaghetti = 100
drinks = 50

total = 0

# First Order
choice = int(input("\nEnter your order (1-5): "))
quantity = int(input("Enter quantity: "))

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

# Display Bill
print("\n===================================")
print("          ORDER SUMMARY")
print("===================================")

print("Total Amount: PHP", total)

payment = float(input("Enter payment: PHP "))

if payment >= total:
    change = payment - total

    print("Payment: PHP", payment)
    print("Change: PHP", change)

    print("\n===================================")
    print("   THANK YOU FOR YOUR ORDER!")
    print("       PLEASE COME AGAIN!")
    print("===================================")

else:
    balance = total - payment
    print("Insufficient payment!")
    print("Remaining Balance: PHP", balance)