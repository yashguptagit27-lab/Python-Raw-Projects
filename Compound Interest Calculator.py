# Python Compound interest calculator

import math

principle=0
rate=0
time=0

while principle<=0: 
    principle=float(input("enter the principle amount: "))
    
    if principle<=0:
        print("Principle amount cannot be negative or zero")
        
while rate<=0:
    rate=float(input("Enter the annual rate of interest: "))
    
    if rate<=0:
        print("Rate cannot be negative or zero.")
        
while time<=0:
    time=float(input("Enter the time period of interest: "))
    
    if time<0:
        print("The time period cannot be negative.")
    else:
        CI=principle*pow((1+rate/100), time)
        print(f"The compound interest for your {principle}, at the annual rate of {rate} per annum for {time} years is {CI: ,}")
        print("The total amount to be collected is ", CI+principle)
        
        