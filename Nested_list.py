#A nested list is a list that contains another list (i.e.: a list of lists). 
#It is also referred to as a multi-diminsional array. For example, a 2 dimensional array is used below:
nested_list=[["manal","oumaima"],["noura","chaimae"],["amal","romaisae"]]
print("lenght of list: ",len(nested_list)) #lenght of list
print("first item of list: ",nested_list[0])

#To go through every list in this list
for i in nested_list:
    print(i)

#To go through every list in this list, use a nested for loop.
for i in nested_list:
    for j in i:
        print(j)



