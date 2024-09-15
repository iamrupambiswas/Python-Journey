def calculate_compound_interest(principal, rate, time, compounds_per_year):
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    compound_interest = amount - principal
    return compound_interest, amount

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): ")) / 100
time = float(input("Enter the time (in years): "))
compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))

compound_interest, total_amount = calculate_compound_interest(principal, rate, time, compounds_per_year)

print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount (Principal + Interest): {total_amount:.2f}")