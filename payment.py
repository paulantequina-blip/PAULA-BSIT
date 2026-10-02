from display import show_receipt, show_insufficient


def ask_payment():
    return float(input("Enter payment: PHP "))


def process_payment(total, payment):
    if payment >= total:
        change = payment - total
        show_receipt(payment, change)
    else:
        balance = total - payment
        show_insufficient(balance)