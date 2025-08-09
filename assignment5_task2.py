list = [1,2,3,4,5,6,7,8,9,10]
print("Original list : ",list)
print("The extracted 5 elements :",list[0:5])
list2 =  [x for x in list[0:5]]
list2.reverse()
print("The reversed extracted 5 elements :",list2)
