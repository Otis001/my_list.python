my_list = [10,20,30,40]
my_list[1]=15
print(my_list)

#extending the list
list=[50,60,70]
my_list.extend(list)
print(my_list)

#deleting the last number in the list
del my_list[-1]
print(my_list)

#sorting the numbers in ascending order
my_list.sort()
print(my_list)

#finding index 30
index_30 = my_list.index(30)
print("Index of value 30:", index_30)

print("Modified list:", my_list)