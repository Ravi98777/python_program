def join(A,B):
    return A+B

def main():
   A = [1,2,3,4,5]
   B = [5,6,7,8,9]
   C = []
   C= join(A,B)
   print("The joined array",C)

if __name__=="__main__":
    main()