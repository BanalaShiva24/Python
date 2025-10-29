customerId = int(input("Enter Customer ID: "))
customerName = input("Enter Customer Name: ")
isPremiumCustomer = input("Is Premium Customer (True/False): ").strip().lower()
YearsPartnership = int(input("Enter Years of Partnership: "))
dealStage= input("Enter Deal Stage (Proposal/Negotiation/Closed): ").strip().lower()
dealValue = float(input("Enter Deal Value: "))
if isPremiumCustomer == 'true':
     discount = 0.1
elif YearsPartnership > 3:
     discount = 0.05
else:
     discount = 0.0
match dealStage:
     case 'proposal':
          discount += 0.02
     case 'negotiation':
          discount += 0.03
     case 'closed':
          discount += 0.05
     case _:
          print("Invalid Deal Stage")
          exit()

finalDealValue = dealValue - (dealValue * discount)
print(f"Final Deal Value for Customer {customerName} (ID: {customerId}) is: ", finalDealValue)