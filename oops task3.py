# Write a Python program to check loan eligibility using a customer class
# Requirements:
# 1. Attributes:
# name, income credit_score
# 2. Method check_eligibility()
# → Rules:
# * Income >= 25000 and credit score >= 650 → Eligible
# * Else → Not eligible
# 3. Take customer details from the user and display eligibility result.


# class Customer:
    
#     name=input("enter name:")
#     income=int(input("enter income:"))
#     credit_score=int(input("enter credit score:"))
#     def __init(self,name,income,credit_score):
#         self.name=name
#         self.income=income
#         self.credit_score=credit_score
#     def check_eligibility(self):
#         if self.income>=25000 and self.credit_score>=650:
#             print(f"{self.name} is eligible for loan")
#         else:
#             print("not eligible")
# c=Customer()
# c.check_eligibility()
            
class BankAccount:
    owner=input("owner name: ")
    balance=int(input("initial balance: "))
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):

        if amount>0:
            self.__balance+=amount
            print(f"deposit Rs {amount}")
       
   
    def withdrew(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdrew Rs {amount}")

           
        else:
            print("no sufficient balance")
   
    def get_balance(self):
        return self.__balance
           

b1=BankAccount("alice",5000)
b1.deposit(3000)
b1.withdrew(2000)
print("final balance:",b1.get_balance())

