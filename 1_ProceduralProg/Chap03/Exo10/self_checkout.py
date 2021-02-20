TAX = 0.055
item1 = int(input('Enter the price of item 1 : '))
qty1 = int(input('Enter the quantity of item 1: '))
item2 = int(input('Enter the price of item 2: '))
qty2 = int(input('Enter the quantity of item 2: '))
item3 = int(input('Enter the price of item 3: '))
qty3 = int(input('Enter the quantity of item 3: '))

subtotal = (item1 * qty1) + (item2 * qty2) + (item3 * qty3) 
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax: ${subtotal * TAX:.2f}')
print(f'Total: ${subtotal * 1.055:.2f}')