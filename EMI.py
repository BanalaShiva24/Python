car  = input("Enter the car name ").capitalize()
if car == "Audi":
     print("The car name is Audi")
elif car == "BMW":
     print("The car name is BMW")       
elif car == "Mercedes":
     print("The car name is Mercedes")
else :
     print("Car not available")

if car == "Audi":
     price = int(input("Enter the price of the car "))
elif car == "BMW":
     price = int(input("Enter the price of the car "))
elif car == "Mercedes":
     price = int(input("Enter the price of the car "))
down_payment_amount = int(input("Enter the down payment amount "))
loan_amount = price - down_payment_amount
if price<=loan_amount:
    print("Loan amount should be less than the price of the car") 
interest_rate = float(input("Enter the interest rate "))
loan_tenure = int(input("Enter the loan tenure in years "))
monthly_interest_rate = interest_rate / (12 * 100)
number_of_payments = loan_tenure * 12   
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
print(f"The EMI for the loan amount {loan_amount} at an interest rate of {interest_rate}% for a tenure of {loan_tenure} years is: {emi:.2f}")
