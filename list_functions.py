'''1)The group of elements enclosed between two square brackets is know as a list in python
2)The elements are separated with (,)and element can be of any type.
3)List is an heterogeneous data structure(it can contain the combination of different data types and structures)
4)list is mutable and ordered data structure

Syntax: list_name = [ele1,ele2,ele3,....]'''

l = [1,2.5,"hi",[4,5]]
print(l[1])
print(l[2])
print(l[3][1])
print(l[ :2])
print(l[2])

'''To replace 
Syntax: list_name[index] = new value'''

l[1] = 5.5
print(l)
l[2],l[3] = 'hello',[5,6]
print(l)
# del is a option to delete an element from the given list 
del l[-1]
print(l)
del l[1]
print(l)

'''Updating an element is list:
Syntax: list_name[index] = new_value'''

l[1] = 15.5
print(l)

'''Deleting and element from list
Syntax: del list_name[index]'''

del l[-1]
print(l)

l1 = [1,2,3,1.5,[55,66],'hello']
print(l1)
print(l1[0:2])
print(l1[4][1])

l1[5] = 'hey'
print(l1)
del l1[5]
print(l1)

a = [1,5,9]
a.append(15)
print(a)

l2 = [1,2,3,4]
l2.remove(2)
print(l2)

l3 = [1,'munna',[1,2,3],['python','hyderabad','hey']]
print(l3)
l3.remove('munna')
print(l3)
l3.remove([1,2,3,])
print(l3)

l4 = [1,2,3,4]
print(l4.pop(2))
print(l4)

l5 = ['munna',1,[1,2,3,],'hello',50]
print(l5.pop(0))

l6 = [1,2,3]
l6.reverse()
print(l6)
 
l7 = [1,'munna',[123],'hyd']
l7.reverse()
print(l7)


l8 = [3,1,5,2,8,10]

l8.sort()
print(l8)

l9 = [3,1,5,2,8,10]
l9.sort(reverse=True)
print(l9)

l10 = ["hello","hi","bye"]
print("@".join(l10))

l11 = ["hello","hi","bye"]
print(" ".join(l11))



