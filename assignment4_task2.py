with open("output.txt","w") as file:
    write = file.write(input("Enter text to write to file: "))
    print("Data succssfully entered to output.txt")
     
    
with open("output.txt","a+") as file:
    write = file.write(input("Enter additional text to write to file: "))
    print("Data succssfully appended")
    file.seek(0)
    content = file.read()
    print("printing the final content of the file : \n")
    print(content)
   

