 # Function to check if a number is even
def check_odd_even(num):
    # If num % 2 equals 0, it's even; returns True for even, False for odd
    return num % 2 == 0

# Taking input from user and converting it to integer
num = int(input("Enter the num: "))

# Calling the function and checking if the number is even
if check_odd_even(num):
    print(num, "number is an even")  # Prints if number is even
else:
    print(num, "number is an odd")   # Prints if number is odd
