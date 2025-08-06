def delete(A, max_size, n, p):
    if p < 0 or p >= n:
        print("Invalid position")
        return A, n

    for i in range(p, n - 1):
        A[i] = A[i + 1]

    A.pop()  # remove last duplicate
    n -= 1
    return A, n

# def search(A,n,key):
#      for i in range(0,n-1):
#         if(A[i] == key):return True
#         else: return False
def search(A, key):
    return key in A

def main():
    max_size = 20
    n = int(input("enter the number of elements "))
    if(n>max_size):
        print ("number is greater then  the maximum size ")
        return 
    
    A=[]
    print("Enter" ,n ,"element : ")
    for i in range(n) :
        A.append(int(input()))

    print("original array : ",A)
    p = int(input("\nEnter the position to  delete\n")) 
    A,n =  delete(A,max_size,n,p)
    print("Modified array : ",A)
    if(search(A,2)):print("yes the element is present in an array")
    else:print(" NO the element is not present in an array")
    
if __name__ == "__main__":
    main()







