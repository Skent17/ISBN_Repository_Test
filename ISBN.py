'''
Shane Kent
03/03/2024
Module 07 Practice Exercise 2
Converted to functions

'''

def preprocess_isbn(isbn):
    isbn = isbn.replace(" ", "")
    return [int(num) for num in isbn]

def calculate_total_sum(digits):
    total_sum = 0
    for i in range(12):
        multiplier = 1 if i % 2 == 0 else 3
        total_sum += digits[i] * multiplier
    return total_sum

def calculate_checksum(total_sum):
    remainder = total_sum % 10
    return (10 - remainder) % 10

def is_valid_isbn(isbn):
    digits = preprocess_isbn(isbn)
    total_sum = calculate_total_sum(digits)
    calculated_checksum = calculate_checksum(total_sum)
    return calculated_checksum == digits[-1]

# Example usage
if __name__ == "__main__":
    isbn = input("Enter your ISBN number: ")
    if is_valid_isbn(isbn):
        print("The ISBN is valid.")
    else:
        print("The ISBN is not valid.")