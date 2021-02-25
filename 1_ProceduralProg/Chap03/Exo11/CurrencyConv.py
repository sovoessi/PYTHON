
amount_from =float (input("How many euros are you exchanging? "))
exchange_rate = float(input("What is the exchange rate? "))

amount_to = amount_from * exchange_rate / 100;

print(f"{amount_from} euros at an exchange rate of {exchange_rate} is {amount_to:.2f} U.S.dollars.")