''' LIST[] -
 1)The group of elements inclosed between two square brackets is known as list in python.
 2)The elements are seperated with commas and element can be an any type.
 3)List is an Heterogenious Data Structure (It can contain the combination of different data types and structures).
 4)List is is a MUTABLE and ORDERED data structure.
 5) Syntax :
        List_name = [ele1,ele2,ele3,......]
 '''

l = [1,2.8,'hi',[5,6]]
print(l[3])
print(l[3][0])
print([1])
print(l[0])

# Accessing element in List
''' Syntax :
list_name = [index]'''

l = [1,2.8,'hi',[5,6]]

print(l[1])

# updating an element in list
''' Syntax : 
list_name[index] = new_value'''

l[1] = 15.2
print(l)
l[1],l[2] = 1.2,'Hello'
print(l)
l[3],l[1] = 3,'Hi'
print(l)


# Deleting element in List
'''Syntax:
 del list_name[index]'''
print(l)
del l[-2]
print(l)
del l[0]
print(l)


#List Functions()
'''
   1) index() :-
        1) This method used to know the index position of substring of given list.
        2) This method takes atleast one parameter and atmost three parameter.
        3) Output format is Integer.
        4) Syntax :-
                List_name.index('Substring',start,end)
        5) EX.
        '''
l = ['a','b','c','a','a','d','c']
print(l.index('a',1,6))
print(l.index('b'))
'''
   2) count() :-
        1) This method is used to know the number of occurrence of given substring in the list.
        2) This method takes attlist one parameter and atmost three parameter.
        3) Output format is integer.
        4) Syntax :- 
                List_name.count('Substring',start,end)
        5) Ex.
        '''
q = ['a' , 'b' , 'a' , 'c' , 'd' , 'a' , 'd']
print(q.count('a'))

''' 3) Append() - 
1) This method is used to add one element at end of the list.
2) This method takes exactly one parameter i.e Element to append(element can be odf any type)
3) the output format is always None.
4) Syntax :-
  List_name.append(Element)  <- Any type
5) ex.
'''
list = [1,2,'Hi',4]
list.append("hi")
print(list)
list.append('HIII')
print(list)

'''
4) Extend() :-
 1) This method is used to add multiple elements at end of the list.
 2) This method takes exactly one parameter i.e a Data Structure.
 3) The output format is always None.
 4) Syntax :-
    list_name.extend(Data Structure)   <- (String,List)
  5) Ex.  
    '''
x = [1,2.2,'hi']
x.extend([5,6])
print(x)
x.extend('Hi')
print(x)
x.extend(list)
print(x)

'''5) insert() :- 1) This method is used to insert one element at given index position. 2) This method takes exactly 
TWO parameters they are Index position and Element to insert. (Element can be of any type) 3) The output format is 
always None. 4) Syntax :- List_name.insert(index,element)  <- 1st index position and 2nd Any type of element. 5) Ex. '''
a = [1,2.2,'hi']
a.insert(-5,'a')
print(a)
a.insert(1,'Dhanraj')
print(a)
a.insert(3,[1,2,'HI'])
print(a)
a.insert(-3,111)
print(a)

'''
6) Remove() :-
    1) This method is used to delete a specific element from given list.
    2) This method takes exactly one parameter i.e. Element to delete.
    3) Output format is always None.
    4) Syntax:
        list_name.remove(element_to_remove)
    5) EX.
'''
l1 = [1,2,3,4]
l1.remove(1)
print(l1)
#l1.remove(5) - > x not in list
print(l1)

'''
7) Pop() :-
    1) This method will return the element at given index position and deletes it from the list.
    2) This method takes atmost one parameter .
    3) The output format is always a type of element at index position.
    4) Syntax:
        list_name.pop(index=-1)
    5) Ex.
'''
l2 = [1,2,3,4,'hi',[1,2],[3,4]]
print(l2.pop(1))
print(l2.pop())
#print(l2.pop(5))
#print(l2.pop(10))   # pop index out of range.
# print(l2.pop(10,20))  it will return whatever value you pass.

'''
8) Reverse() :-
    1) This method is used to reverse the elements of given list.
    2) No parameters require.
    3) The output format is always None.
    4) Syntax:
        List_name.reverse()
    5) Ex.
'''
l3 = [1,2,3,'a','b','c']
l3.reverse()
print(l3)
l3.reverse()
print(l3)

'''
9) Sort() :-
    1) This method is used to sort the given list either in ascending or descending order.
    2) This method takes at most one parameter.
    3) The output format is always None.
    4) Syntax:
        list_name.sort(reverse=False)  # default value is False.
    5) Ex.
'''
l4 = [3,4,5,1,3,6,8,9]
l4.sort(reverse=True)
print(l4)
l4.sort()  # its combination of (Ascending order + Reverse)
print(l4)

'''
10) Ord() :-
        1) Syntax :
               ord(''character)
               '''
       # print(ord('A'))
        #print(ord('a'))
'''
11) Chr() :-
            1) Syntax:
                chr(ASCII)'''

       # print(chr(65))->
        #print(chr(97))->
'''
12) Copy() :-
        1) This method will return a copy of specific list.
        2) No parameter required.
        3) The output format is always None.
        4) Syntax:
            list_name.copy()
        5) Ex.
'''
a = ['apple','mango','banana']
b = a.copy()
print(b)
c = [1,2,3,4]
b = a.copy()
print(b)
'''
13) join() :-
        1) This method will return the joined string from the list of string.(Concatenated string)
        2) This method takes exactly one parameter i.e. Substring to concatenate .
        3) Output format is always list.
        4) Syntax:
         'substring'.join(Datastructures)
    5) Ex.
       '''
l = ['hi','hello','world']
l1 = '@'.join(l)
print(l1)

