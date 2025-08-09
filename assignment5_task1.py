dictionary = {
    'ravi' : 82.5,
    'ayush' :  95.2,
    'abhinav':  75.2,
    'vatan' : 93.2,
    'deepanjal' :  85.2
}
name = input("Enter the student name : ")
try:
    print("{}'s  marks is : {}".format(name ,dictionary[name]))
except:
    print("Student not found")