try :
    with open("sample.txt","r")  as file :

        content = file.readlines()
        print(content)
        file.close()
except :
    print("The file sample .txt was not found")