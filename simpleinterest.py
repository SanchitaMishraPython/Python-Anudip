
#calculate simple interest
def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (in percentage): "))
time = float(input("Enter the time (in years): "))


interest = calculate_simple_interest(principal, rate, time)


print("The simple interest is:", interest)
