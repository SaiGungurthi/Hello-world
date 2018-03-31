Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 1
>>> b = 1.1
>>> c= True
>>> type(a)
<type 'int'>
>>> b
1.1
>>> type(b)
<type 'float'>
>>> c
True
>>> type(c)
<type 'bool'>
>>> a+b
2.1
>>> b+c
2.1
>>> c+b
2.1
>>> # type bool and float are adding up.
>>> a+b+c
3.1
>>> (*ca+b)
SyntaxError: invalid syntax
>>> (a+b)*c
2.1
>>> # type bool, int and float are multiplying.
>>> a = (1,2,3,4,5,6,7,8,9,10)
>>> type(a)
<type 'tuple'>
>>> a.count(1)
1
>>> a.index(10)
9
>>> a(-1)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a(-1)
TypeError: 'tuple' object is not callable
>>> a.index(9)
8
>>> a
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> a[-1]
10
>>> a[-2]   #is working
9
>>> a[-6]   #Tuple is complete.
5
>>> b = [ 1,2,3,4,6,8,9,7,44,556,1,2,4,5,6]
>>> type(b)
<type 'list'>
>>> b.append[101]

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b.append[101]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> b.append(101)
>>> b
[1, 2, 3, 4, 6, 8, 9, 7, 44, 556, 1, 2, 4, 5, 6, 101]
>>> b.count(1)
2
>>> b.extend(a)
>>> b
[1, 2, 3, 4, 6, 8, 9, 7, 44, 556, 1, 2, 4, 5, 6, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> b.index(101)
15
>>> b.insert(-1, 550)
>>> b
[1, 2, 3, 4, 6, 8, 9, 7, 44, 556, 1, 2, 4, 5, 6, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 550, 10]
>>> #Question on insert.
>>> b.insert(-1, 550)
>>> b
[1, 2, 3, 4, 6, 8, 9, 7, 44, 556, 1, 2, 4, 5, 6, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 550, 550, 10]
>>> b.pop(-1)
10
>>> b
[1, 2, 3, 4, 6, 8, 9, 7, 44, 556, 1, 2, 4, 5, 6, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 550, 550]
>>> b.remove(1)
>>> b
[2, 3, 4, 6, 8, 9, 7, 44, 556, 1, 2, 4, 5, 6, 101, 1, 2, 3, 4, 5, 6, 7, 8, 9, 550, 550]
>>> b.sort()
>>> b
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556]
>>> b.
SyntaxError: invalid syntax
>>> b.append(556)
>>> b
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556, 556]
>>> b.sort()
>>> b.reverse()
>>> b
[556, 556, 550, 550, 101, 44, 9, 9, 8, 8, 7, 7, 6, 6, 6, 5, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1]
>>> b.sort()
>>> b
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556, 556]
>>> b(-1)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b(-1)
TypeError: 'list' object is not callable
>>> b[-1]
556
>>> b.count(b[-1]) + b.index(b[-1])
27
>>> b.length

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.length
AttributeError: 'list' object has no attribute 'length'
>>> b
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556, 556]
>>> b.__len__
<method-wrapper '__len__' of list object at 0x03E72A30>
>>> len(b)
27
>>> len(b)       #length of the list
27
>>> b.count(b[-1]) + b.index(b[-1])    #length of the list
27
>>> b[:]
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556, 556]
>>> b[:]    #split fuction
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556, 556]
>>> b[1:7]
[1, 2, 2, 2, 3, 3]
>>> b[1:7]     #gives the next 6 variables starting from variable 1 at b[0] position.
[1, 2, 2, 2, 3, 3]
>>> b[5:10]
[3, 3, 4, 4, 4]
>>> b[5:10]   #gives the variables from position b[5] to b[9]
[3, 3, 4, 4, 4]
>>> b[12:17]
[6, 6, 6, 7, 7]
>>> ##lists methods are done
>>> b
[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 9, 9, 44, 101, 550, 550, 556, 556]
>>> # for loop in lists.
>>> 
>>> 
>>> count = 10
>>> 
>>> for x in b:
	if x = 556,
	
SyntaxError: invalid syntax
>>> for x in b:
	if x = 556:
		
SyntaxError: invalid syntax
>>> for x in b:
	if x == 556
	
SyntaxError: invalid syntax
>>> for x in b:
	if x == 556,
	
SyntaxError: invalid syntax
>>> for x in b:
	if x == 556:
		count = count + 1,
		print count, x
	else:
		print x

		
1
1
2
2
2
3
3
4
4
4
5
5
6
6
6
7
7
8
8
9
9
44
101
550
550
(11,) 556

Traceback (most recent call last):
  File "<pyshell#88>", line 3, in <module>
    count = count + 1,
TypeError: can only concatenate tuple (not "int") to tuple
>>> for x in b:
	if x == 556:
		count = count + 1,
		print (count, x)
	else:
		print x

		
1
1
2
2
2
3
3
4
4
4
5
5
6
6
6
7
7
8
8
9
9
44
101
550
550

Traceback (most recent call last):
  File "<pyshell#90>", line 3, in <module>
    count = count + 1,
TypeError: can only concatenate tuple (not "int") to tuple
>>> for x in b:
	if x == 556:
		count = count + 1,
		print ("count", "x")
	else:
		print x

		
1
1
2
2
2
3
3
4
4
4
5
5
6
6
6
7
7
8
8
9
9
44
101
550
550

Traceback (most recent call last):
  File "<pyshell#92>", line 3, in <module>
    count = count + 1,
TypeError: can only concatenate tuple (not "int") to tuple
>>> 
