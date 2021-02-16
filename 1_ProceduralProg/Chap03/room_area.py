import math

CONVERSION_FACTOR = 0.09290304

room_length = float(input('What is the length of the room in feet? '))
room_width = float(input('What is the width of the room in feet? '))

area = room_length*room_width

print(f"You entered dimensions of {math.trunc(room_length)} feet by {math.trunc(room_width)} feet.")
print('The area is')
print(f"{math.trunc(area)} square feet")
print(f"{area * CONVERSION_FACTOR:.3f} square meters")
  
