# Compound Interest Calculation
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))
rate = rate / 100
amount = principal * (1 + rate) ** time
compound_interest = amount - principal
print("Amount =", amount)
print("Compound Interest =", compound_interest)