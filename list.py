Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ['she', 'sells', 'shells', 'by', 'the', 'sea', 'shore']
>>> b = "selfish shellfish"
>>> c = [1, 1, 2, 3, 5, 8, 13]
>>> a[1]
'sells'
>>> b[3:4]
'f'
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[5]
'sea'
>>> 'by' in a[3]
True
>>> 'self' in b[0:5]
True
>>> a[2] == a[6]
False
>>> [1,2,5] in c
False
>>> 'by' in a
True
>>> 'sh' in c
False
>>> a[3] == b[8:13]
False
>>> dog = 'dalmatain'
>>> len(dog)
9
>>> dogs = [dog,'poodle'.'boxer']
SyntaxError: invalid syntax
>>> dogs = [dog, 'poodle','boxer']
>>> len(dogs)
3
>>> dogs[0]
'dalmatain'
>>> one = [1,2,3,4]
>>> two = [7,6,5,4]
>>> three = ["y1", "friends", "fun"]
>>> one.remove(4)
>>> print(one)
[1, 2, 3]
>>> one.pop(1)
2
>>> print(one)
[1, 3]
>>> one.sort()
>>> print(one)
[1, 3]
>>> print(sorted(one))
[1, 3]
>>> list_one = [1,5,4]
>>> list_two = [1,3,9]
>>> list_three = list_one[0]
>>> print(list_three)
1
>>> list_three.append(list_one[0])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list_three.append(list_one[0])
AttributeError: 'int' object has no attribute 'append'
>>> list1 = [list_one[0]]
>>> list1
[1]
>>> 
