principal = float(input("Enter the principal: "))
rate_of_interest = float(input("Enter the rate of interest: "))
num_of_years = int(input("Enter the number of years: "))

investment = principal * (1 + ( num_of_years * rate_of_interest/100))
print(
    f"After {num_of_years} years at {rate_of_interest}%, the investment will be worth ${investment}."
    )