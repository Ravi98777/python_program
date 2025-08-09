def check_odd_even(num):
    return num%2 == 0
num = int(input("Enter the num "))
if(check_odd_even(num)):
    print(num," number is an even")
else: print(num," number is as odd")    