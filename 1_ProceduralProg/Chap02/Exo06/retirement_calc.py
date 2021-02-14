from datetime import date

current_age = input("What is your current age? ")
choose_retire_age = input("At what age would you like to retire? ")

years_left = int(choose_retire_age) - int(current_age)
actual_year = date.today().year

print(f"You have {years_left} years left until you can retire.")
print(f"It's {actual_year}, so you can retire in {actual_year + years_left}.")

