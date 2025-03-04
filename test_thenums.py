'''
Shane Kent
03/03/2024
Module 07 Practice Exercise 2
py testing the converted functions to ensure code works as expected

'''

import pytest

from ISBN import preprocess_isbn, calculate_total_sum, calculate_checksum, is_valid_isbn

#Conversion to digits while excluding the last digit
def process_isbn(isbn: str):
    isbn = isbn.replace(" ", "") 
    digits = [int(num) for num in isbn[:-1]]
    return digits

#calculates checksum with 1 to 3 integers (step 3)
def calculate_checksum_sum(digits):
    total_sum = sum(digits[i] * (1 if i % 2 == 0 else 3) for i in range(len(digits)))
    return total_sum

#check digit calculation from the total sum
def extract_check_digit(total_sum):
    remainder = total_sum % 10
    return (10 - remainder) % 10

#Validation by comparing calculated and last check digit
def validate_isbn(isbn: str):
    digits = process_isbn(isbn)
    total_sum = calculate_checksum_sum(digits)
    calculated_check_digit = extract_check_digit(total_sum)
    actual_check_digit = int(isbn[-1])
    return calculated_check_digit == actual_check_digit

# Test ISBN numbers
def test_isbn_validator():
    # Test ISBN 9781718502710 (First number)
    isbn1 = "9781718502710"
    expected_digits1 = [9, 7, 8, 1, 7, 1, 8, 5, 0, 2, 7, 1] 
    expected_sum1 = 90  
    expected_check_digit1 = 0  
    
    assert process_isbn(isbn1) == expected_digits1
    assert calculate_checksum_sum(expected_digits1) == expected_sum1
    assert extract_check_digit(expected_sum1) == expected_check_digit1
    assert validate_isbn(isbn1) == True

    # Test ISBN 9780357881057 (Second number)
    isbn2 = "9780357881057"
    expected_digits2 = [9, 7, 8, 0, 3, 5, 7, 8, 8, 1, 0, 5] 
    expected_sum2 = 113  
    expected_check_digit2 = 7 
    
    assert process_isbn(isbn2) == expected_digits2
    assert calculate_checksum_sum(expected_digits2) == expected_sum2
    assert extract_check_digit(expected_sum2) == expected_check_digit2
    assert validate_isbn(isbn2) == True
