""" 
Shane Kent
01/27/2025
Module 02 Programming Assignment 
I will be writing code that will checksum credit card numbers to confirm ISBN numbers 
to validate against a checksum digit.

"""
#ISBN numbers from syllabus
# ISBN: 9781718502710
# ISBN: 9780357881057

#inputing ISBN number, removing spaces between numbers and creating a list.
ISBN_Number = input("Enter your ISBN number: ")
ISBN_Number = ISBN_Number.replace(" ", "")
numlist = [int(num) for num in ISBN_Number]

#calculating the total sum with alternative multiplication of 1 and 3.
Total_Sum = 0
#ensuring the numbers are in the correct range. calculating multiplication between even or odd numbers.
for digits in range(12):
    multiplier = 1 if digits % 2 == 0 else 3
    Total_Sum += numlist[digits] * multiplier

#the total sum divided by 10
remainder = Total_Sum % 10

#calculating the checksum
Checksum = (10 - remainder) % 10

#display the total sum
print(f"Total Sum: {Total_Sum}")
#display the last digit of the numlist
print(f"the checksum digit from the ISBN is: {numlist[-1]}")
#display the calculated checksum
print (f"the calculated checksum is: {Checksum}")