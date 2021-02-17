amount_people = int(input('How many people? '))
amount_pizzas = int(input('How many pizzas do you have? '))
slices_per_pizza = int(input('How many slices per pizza do you have? '))

print(f"{amount_people} people with {amount_pizzas} pizzas")
print(f"Each person gets {slices_per_pizza * amount_pizzas // amount_people} pieces of pizza.")

leftovers = (slices_per_pizza  * amount_pizzas) % amount_people
print(f"There are {leftovers} leftover pieces.")
