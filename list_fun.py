'''
the group of elements enclosed between two square brackets is known as a list in python.
the elements are saperated with camas and element can be of any type.
list is an hetiro genious data structure (it can contain the combination of diffrent data types and structures).
list is a mutable and ordered data structure.
syntax:- list_name = [ele0, ele1, ele2-------]
updating an element from a list
syntax:- list_name[index] = new_value
deletion of an element in a list
syntax:- del list_name[index]
'''
list = [1, 2, 'mahesh', [1, 3.4, 566]]
print(list)
list[1] = 123
print(list)
list[2] = 'ravula'
print(list)
del list[-1][-1]
print(list)