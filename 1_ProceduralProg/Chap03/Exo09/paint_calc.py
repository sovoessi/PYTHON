from math import ceil

CONVERSION_RATE = 350

length =float(input("Enter length: ")) 
width = float(input("Enter width: "))
area = length * width;

paint = ceil(area / CONVERSION_RATE);

print(f"You will need to purchase {paint} gallons of paint to cover {area:.0f} square feet.")
