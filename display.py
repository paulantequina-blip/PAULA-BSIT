def show_summary(total):
    print("\n===================================")
    print("          ORDER SUMMARY")
    print("===================================")
    print("Total Amount: PHP", total)


def show_receipt(payment, change):
    print("Payment: PHP", payment)
    print("Change: PHP", change)

    print("\n===================================")
    print("   THANK YOU FOR YOUR ORDER!")
    print("       PLEASE COME AGAIN!")
    print("===================================")


def show_insufficient(balance):
    print("Insufficient payment!")
    print("Remaining Balance: PHP", balance)