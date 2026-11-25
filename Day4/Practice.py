#
# correct_pin =1234
# actual_attempt=0
# maximum_attempts=3
# starting_balance=1000
# deposit_amount=0
# withdraw_amount=0
#
# while actual_attempt<maximum_attempts:
#     pin=int(input("Enter your pin: "))
#     actual_attempt+=1
#
#     if actual_attempt==maximum_attempts:
#         print("Maximum attempts reached. Your account is locked.")
#     else:
#         attempt_left=maximum_attempts-actual_attempt
#         print(f"Incorrect PIN. You have {attempt_left} attempts left.")
#
#
#     if pin==correct_pin:
#         print(f"Enter PIN:{pin}")
#         print("Login successful")
#         print("")
#         print("1.check Balance")
#         print("2.Deposit Money")
#         print("3.Withdraw Money")
#         print("4.Exit")
#         while True:
#             number = int(input("Enter choice:"))
#             if number==1:
#                 print(f"Your balance is ${starting_balance}")
#
#             elif number==2:
#                 deposit_amount=int(input("Enter amount to deposit:"))
#                 if deposit_amount>0:
#                     print(f"You have deposited ${deposit_amount}")
#                     starting_balance+=deposit_amount
#                 else:
#                     print("Invalid deposit amount")
#             elif number==3:
#                 withdraw_amount=int(input("Enter amount to withdraw:"))
#                 if withdraw_amount<starting_balance:
#                     print(f"You have withdrawn ${withdraw_amount}")
#                     starting_balance-=withdraw_amount
#                 else:
#                     print("Insufficient balance")
#             elif number==4:
#                 print("Thanks for using our services. Goodbye!")
#                 break
from Tuple import mytule

if "apple" not in mytule:
    print("Apple is not in the tuple")
else:
    print("Apple is in the tuple")

print(list(mytule))
print(type(mytule))

list4=[1,2,3,4,5]


print(mytule.index("banana"))















