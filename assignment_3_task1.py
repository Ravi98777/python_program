fact = 1
def factorial(num):
    if num == 0 :
        return 1
    return factorial(num-1)*num
num = int(input("Enter the number "))
print("The factoral of " ,num,"is : ",factorial(num))

