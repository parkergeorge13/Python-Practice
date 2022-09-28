# Parker George
# IS 403 Section 4
# Chapter 11 Homework 

# You are given the task of creating a program that will keep track of all customers and their accounts within a company.
# Write a program that creates a class for a customer, loads up data for the customer object from the keyboard, and then prints the data. 
# The constructor should receive all of the data from the keyboard and assign the values to all of the instance variables. 
# The printing of the data should be done through a class method called display_customer and should display the customer name and the balance similar to:

# John Doe has a balance of $102.00

# There should be a common class variable shared between all objects with the company name of "ABC Accounting".

# The attributes for the customer are:
# Customer ID
# Customer Name
# Account Number
# Balance


# Clear Console
import os
def clear_console():
    os.system('cls')
clear_console()

class Customer: 
    company_name = 'ABC Accounting'

    def __init__ (self, customer_id, customer_name, account_number, balance):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance

    def display_customer(self):
        return (f"{self.customer_name} has a balance of ${self.balance}")

iCustId = input("Enter the customer id: ")
sCustName = input("Enter the customer name: ")
sAcctNum = input("Enter the customer account number: ")
fBalance = input("Enter the customer balance: ")

oCustomer = Customer(iCustId, sCustName, sAcctNum, fBalance)

print(oCustomer.display_customer())
