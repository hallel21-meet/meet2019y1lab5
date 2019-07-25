Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> print(turtle.pos())
(0.00,0.00)
>>> print(type(turtle.pos()))
<class 'turtle.Vec2D'>
>>> one = [1,2,3,4]
>>> two = [7,6,5,4]
>>> one.reverse()
>>> print(one)
[4, 3, 2, 1]
>>> one.sort()
>>> print(one)
[1, 2, 3, 4]
>>> one.remove(4)
>>> print(one)
[1, 2, 3]
>>> three = [3]
>>> four = three*3
>>> print(four)
[3, 3, 3]
>>> five = one.copy()
>>> one.sort()
>>> print(one)
[1, 2, 3]
>>> print(five)
[1, 2, 3]
>>> 
