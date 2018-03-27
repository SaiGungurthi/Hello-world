Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print a

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print a
NameError: name 'a' is not defined
>>> a=1
>>> print a
1
>>> print ('a')
a
>>> type (a)
<type 'int'>
>>> a=b

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
>>> a=1
>>> b=2
>>> a=b
>>> print a
2
>>> type (b)
<type 'int'>
>>> a= forcabarca

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a= forcabarca
NameError: name 'forcabarca' is not defined
>>> a="forcabarca"
>>> type(a)
<type 'str'>
>>> print b
2
>>> b=2.1
>>> type(b)
<type 'float'>
>>> a= 2.11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
>>> type (a)
<type 'float'>
>>> a+b
4.211111111111111
>>> a-b
0.011111111111111072
>>> a*b
4.433333333333334
>>> a/b
1.0052910052910053
>>> 2*a+4*b
12.622222222222224
>>> (1+a)*(1+b)
9.644444444444446
>>> 1+a*1+b
5.211111111111111
>>> c=1+a*1+b
>>> print c
5.21111111111
>>> print "c"
c
>>> c = True
>>> type(c)
<type 'bool'>
>>> 1+a*2+b-c
6.322222222222223
>>> c=true

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c=true
NameError: name 'true' is not defined
>>> c="true"
>>> c=True
>>> print c
True
>>> type(c)
<type 'bool'>
>>> c="True"
>>> type c
SyntaxError: invalid syntax
>>> type(c)
<type 'str'>
>>> c="true"
>>> type(c)
<type 'str'>
>>> c=true

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c=true
NameError: name 'true' is not defined
>>> c= True
>>> type(c)
<type 'bool'>
>>> a+b+c
5.211111111111111
>>> c= "Forcabarca"
>>> a+c

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a+c
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> a*c

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a*c
TypeError: can't multiply sequence by non-int of type 'float'
>>> a*b
4.433333333333334
>>> a/b
1.0052910052910053
>>> a=1
>>> b= cfg

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    b= cfg
NameError: name 'cfg' is not defined
>>> b="cfg"
>>> str(a)+b
'1cfg'
>>> a+int(b)

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a+int(b)
ValueError: invalid literal for int() with base 10: 'cfg'
>>> c=2.1
>>> str(a)+float(c)

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    str(a)+float(c)
TypeError: cannot concatenate 'str' and 'float' objects
>>> str(a)+c

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    str(a)+c
TypeError: cannot concatenate 'str' and 'float' objects
>>> c+str(a)

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    c+str(a)
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> str("a")+c

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    str("a")+c
TypeError: cannot concatenate 'str' and 'float' objects
>>> str("a")+str(c)
'a2.1'
>>> str(a)+str(c)
'12.1'
>>> str(c)+str(a)
'2.11'
>>> a=1
>>> a=2
>>> b=3
>>> c=4
>>> a+b #doesn't matter.
5
.
>>> a+b+c #doesn't matter too
9
>>> a+b-c #this is a lot of fun
1
>>> b+c-a
5
>>> b-c+a
1
>>> #lot of questions tonight on math. Don I know the math??
>>> #lot of questions tonight on math. Don I know the math??
>>> 
>>> 
>>> 
