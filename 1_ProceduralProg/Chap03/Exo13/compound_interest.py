from math import pow

principal = float(input("What is the principal amount? "))
rate_of_interest = float(input("What is the rate? ")) / 100
num_of_years = int(input("What is the number of years? "))
compounded_times = int(input("What is the number of times the interest is compounded per year? "))

investment = principal * pow(
        1 + rate_of_interest/compounded_times, compounded_times * num_of_years);
print(
    f"${principal} invested at {rate_of_interest*100:.2f}% for {num_of_years} years compounded {compounded_times} times per year is ${investment:.2f}."
    )