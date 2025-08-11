 # Program to read and print contents of a file

# Ask the user to enter the file name
filename = input("Enter the name of the file to open (with extension): ")

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the contents
        contents = file.read()
        # Print the contents
        print("\nContents of the file:")
        print(contents)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


#Another program to find word in a file.
# filename = input("Enter the file name to write ")
# try :
#     with open(filename,"r") as f:
#         st = f.read()
#         print(st)
#         word = input("\nEnter the word to find  ")
#         if(word in st):
#             print("yes the word is present in the file")
#         else: 
#             print(" NO the word is not present in the file")

# except  FileNotFoundError:
#     print(f"Error : the file'{filename}' does not exists. ")

 
