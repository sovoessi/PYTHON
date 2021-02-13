
def calculate_tip(bill_amount: float, tip_rate: float) -> float:
    return bill_amount * tip_rate / 100

def calculate_total(bill_amount: float, tip: float)  -> float:
    return bill_amount + tip


if  __name__ == '__main__':
    bill_amount = float(input("What is the bill amount? $"))
    tip_rate = float(input("What is the tip rate?"))

    tip = calculate_tip(bill_amount, tip_rate)
    total = calculate_total(bill_amount, tip)

    print(f"Tip: ${tip:.2f}\nTotal: ${total:.2f}")

