'''
Tuple() :-
    1) The group of elements enclosed between two parenthesis [braces()] is known as tuple.
    2) Elements are separated by commas and these can be of any type.
    3) Tuples are IMMUTABLE and ORDERED data structure.
    4) Syntax:
        tuple_name= (ele1,ele2,ele3,.....)
    5) Ex.
'''
t = (1,2,3,4,[4,5])
t[-1][1] = 10
#t[-1] = 100    TypeError: 'tuple' object does not support item assignment
print(t.index(1))
print(t.count(3))
print(t)

'''
 Dictionary{} :-
    1) The group of items enclosed between two flower brackets is known as dictionary in python.
    2) Items are separated by commas and an items combination of key and values.
    3) Key and values separated with colon(:).
    4) In dictionaries a key should be UNIQUE and IMMUTABLE.
    5) Values can be of any type.
    6) Dictionaries are UNORDERED and MUTABLE data structure.
    7) Syntax:
        dictionary_name = {key1:value1,key2:value2,key3:value3,...}
    8) Ex.
'''
d = {'a':1,'b':'Dhanraj','c':1.5,'d':[1,2,3,4,5]}
print(d)
print(d['b'])
print(d['a'])
# print(d['x'])  KeyError: 'x'
e = {'a':1,'b':2,'c':3,'a':3}
print(e)
''' 
Keying :- 
    1) The process of accessing the data from unordered data structure is known as keying.
    2) Syntax:
        dictionary_name[key]
    3) Ex.
'''
x = {'a':1,'b':2,'c':3}
x['b']
print(x)

''' 
 1) Updating an item in dictionary :- 
      1) Syntax:
            dict_name[key] new_error
    2) Ex.
'''
a = {'a':1,'b':2,'c':3}
a['a'] = 2
print(a)
a['c'] = 'Dhanraj'
print(a)

'''
 2) Deleting an item in dictionary :-
     1) Syntax:
            del dict_name[key]
    2) Ex.
'''
y = {'Name':'Dhanraj','age':25,'a':1,'b':2}
del y['a']
print(y)
del y['Name']
print(y)

'''
 3) Inserting an item in dictionary :-
        1) Syntax:
            dict_name[new_key] = new_value
        2) EX. 
'''
x = {'a':1,'b':2,'c':3}
x['d'] = 4
print(x)
x['e'] = 5
print(x)

'''
Dictionary functions :-
    1) Keys() -
        1) This method will return list of keys available in given dictionary.
        2) No parameters required.
        3) The output format is always dict_keys method object.
        4) Syntax:
            dictionary_name.keys()
            print(d.keys()) => dict_keys(['a','b'])
        5) Ex.
'''
q = {'a':1,'b':2,'c':3}
print(q.keys())

'''
    2) Values() -
        1) This method will return list of values available in given dictionary.
        2) No parameters required.
        3) The output format is always dict_values method object.
        4) Syntax:
            dictionary_name.values()
            print(d.values()) => dict_values(['a','b'])
        5) Ex.
'''
q = {'a':1,'b':2,'c':3}
print(q.values())

'''
    3) Items() - 
        1) This method will return list of items available in given dictionary.
        2) No parameters required.
        3) The output format is always dict_items method object.
        4) Syntax:
            dictionary_name.items()
            print(d.items()) => dict_items([('a', 1), ('b', 2), ('c', 3)])
        5) Ex.
'''
q = {'a':1,'b':2,'c':3}
print(q.items())

'''
    4) get() -
        1) This method will return the value available at given key .
        2) This method takes at most two parameters.
        3) The output format is always type of value at key.
        4) Syntax:
            dictionary_name.get(key,value=None)   default value=None.
        5) Note :
            1) Get method will return second parameter value only when the key is not available.
            2) Get method will not effect of dictionary.
        6) Ex.
'''
q = {'a':1,'b':2,'c':3}
print(q.get('a'))
print(q.get('a',10))
print(q.get('x',10))
print(q.get('x'))

'''
    5) Setdefault() :-
        1) This method will also works like get method (including the syntax and output format )
        2) But unlike get ,set default will insert a new item into the dictionary if the key is not available.
        3) Syntax:
            dict_name.setdefault(key,value=None)
        4) Ex.
'''
w = {'a':1,'b':'Hi','c':[1,2],'d':{'a':11,'b':22}}
print(w.setdefault('a'))
print(w.setdefault('a',100))
print(w.setdefault('x'))
print(w)
print(w.setdefault('y',100))
print(w)

'''
    6) pop() :-
        1) This method will return return the value at given key and removes the item from dictionary.
        2) This method takes at least one parameter and at most two parameters.
        3) The output format is always type of value at given key.
        4) Syntax:
            dict_name.pop(key,value)
        5) Ex.
'''
d = {'a':11,'b':22,'c':33}
print(d.pop('a'))
print(d)
 # print(d.pop('x'))   ----->KeyError: 'x'
print(d)
print(d.pop('x',15))
print(d.pop('b',100))
print(d)

'''
    7) popitem() :-
        1) This method will return the last item of the dictionary and then remove it.
        2) No parameter required.
        3) Output format is always tuple.
        4) Syntax:
            dict_name.popitem()
        5) Ex.
'''
p = {'name':'Dhanraj','age':25,'a':12,'b':22}
print(p.popitem())
print(p)
print(p.popitem())
print(p)

'''
    8) fromkeys() :-
        1) This method will return a new dictionary with the keys available in given data structure and with comma values.
        2) This method takes at least one parameter and at most two parameters.
        3) Output format is always dictionary.
        4) Syntax:
            dict_name.fromkeys(data_structure,value=None)   -----> Default value is None.
        5) Ex.
'''
c = {'name':'Dhanraj','age':25,'a':12,'b':22}
print(c.fromkeys('a',100))
print((c))
print(c.fromkeys('abc',200))
print(c.fromkeys('xyz'))
print(c.fromkeys({'a':1,'b':2},100))
'''
    9) Update() :- 
        1) This method is used to update one dictionary with another.
        2) This method takes exactly one parameter i.e. dictionary.
        3) The output format is always None.
        4) Syntax:
            dict_name1.update(dict_name2)
        5) Ex.
'''
d1 = {'a':1,'b':2}
d2 = {'b':3,'c':4}
# d1.update(d2)   --> {'a':1,'b':2,'b':3,'c':4}
# print(d1)  ---->   {'a':1,'b':3,'c':4}
d2.update(d1)
print(d2)
'''
    10) Clear() :-
        1) This method is used to remove all item from the dictionary.
        2) No parameters required.
        3) Output format is None.
        4) Syntax:
            dict_name.clear()
        5) Ex.
'''
a = {'x':1,'y':2}
a.clear()
print(a)


