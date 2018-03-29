Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Squad ["1", "2", "3", "99", "10", "07", "100"]

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Squad ["1", "2", "3", "99", "10", "07", "100"]
NameError: name 'Squad' is not defined
>>> Squad = ["1", "2", "3", "99", "10", "07", "100"]
>>> Squad
['1', '2', '3', '99', '10', '07', '100']
>>> Squad []
SyntaxError: invalid syntax
>>> Squad.index("100")
6
>>> Squad.index["100"]

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Squad.index["100"]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> Squad[4]
'10'
>>> Squad.append("100")
>>> Squad
['1', '2', '3', '99', '10', '07', '100', '100']
>>> Squad.count(7)
0
>>> Squad.count(07)
0
>>> Squad.count("100")
2
>>> Squad[-1]
'100'
>>> 2+int(Squad.index(Squad[-1]))
8
>>> Squad.count(Squad[-1])+ int(squad.index(Squad[-1]))

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Squad.count(Squad[-1])+ int(squad.index(Squad[-1]))
NameError: name 'squad' is not defined
>>> Squad.count("Squad[-1]")+ int(squad.index(Squad[-1]))

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Squad.count("Squad[-1]")+ int(squad.index(Squad[-1]))
NameError: name 'squad' is not defined
>>> int(Squad.count("Squad[-1]"))+ int(squad.index(Squad[-1]))

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(Squad.count("Squad[-1]"))+ int(squad.index(Squad[-1]))
NameError: name 'squad' is not defined
>>> int(Squad.count("Squad[-1]"))+ int(Squad.index(Squad[-1]))
6
>>> Squad.count(Squad[-1])+ int(squad.index(Squad[-1]))

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Squad.count(Squad[-1])+ int(squad.index(Squad[-1]))
NameError: name 'squad' is not defined
>>> Squad
['1', '2', '3', '99', '10', '07', '100', '100']
>>> Squad.count("100")
2
>>> Squad[-1]
'100'
>>> int(Squad.index(Squad[-1]))
6
>>> Squad.count("100") + int(Squad.index(Squad[-1]))
8
>>> Squad.count("100") + Squad.index(Squad[-1])
8
>>> int(Squad.count("100")) + Squad.index(Squad[-1])
8
>>> squad

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    squad
NameError: name 'squad' is not defined
>>> Squad
['1', '2', '3', '99', '10', '07', '100', '100']
>>> Squad.insert(6,"99")
>>> Squad
['1', '2', '3', '99', '10', '07', '99', '100', '100']
>>> Squad.insert(10,"101")
>>> Squad
['1', '2', '3', '99', '10', '07', '99', '100', '100', '101']
>>> Squad.insert(21, "88")
>>> Squad
['1', '2', '3', '99', '10', '07', '99', '100', '100', '101', '88']
>>> Squad. (21)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    Squad.pop(21)
IndexError: pop index out of range
>>> Squad[-1]
'88'
>>> Squad.count("88)
	    
SyntaxError: EOL while scanning string literal
>>> Squad.count("88")
1
>>> Suqad.insert(3, "100")

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Suqad.insert(3, "100")
NameError: name 'Suqad' is not defined
>>> Squad.insert(3, "100")
>>> Squad
['1', '2', '3', '100', '99', '10', '07', '99', '100', '100', '101', '88']
>>> Squad[-1]
'88'
>>> Squad.count("88")
1
>>> Squad.count("88")+ Squad,index(Squad[-1])

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    Squad.count("88")+ Squad,index(Squad[-1])
TypeError: unsupported operand type(s) for +: 'int' and 'list'
>>> Squad.count("88")+ Squad.index(Squad[-1])
12
>>> Squad
['1', '2', '3', '100', '99', '10', '07', '99', '100', '100', '101', '88']
>>> Squad.pop("100")

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    Squad.pop("100")
TypeError: an integer is required
>>> Squad.pop(11)
'88'
>>> Squad
['1', '2', '3', '100', '99', '10', '07', '99', '100', '100', '101']
>>> Squad.remove("100")
>>> Squad
['1', '2', '3', '99', '10', '07', '99', '100', '100', '101']
>>> Squad.remove("Squad.pop(7)")

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    Squad.remove("Squad.pop(7)")
ValueError: list.remove(x): x not in list
>>> Squad.sort
<built-in method sort of list object at 0x03AD7CB0>
>>> Squad
['1', '2', '3', '99', '10', '07', '99', '100', '100', '101']
>>> Squad.sort()
>>> Squad
['07', '1', '10', '100', '100', '101', '2', '3', '99', '99']
>>> Squad.reverse()
>>> Squad
['99', '99', '3', '2', '101', '100', '100', '10', '1', '07']
>>> Squad.append("7")
>>> Squad
['99', '99', '3', '2', '101', '100', '100', '10', '1', '07', '7']
>>> Squad.append("7")
>>> Squad.append("7")
>>> Squad.append("7")
>>> Squad.append("7")
>>> Squad
['99', '99', '3', '2', '101', '100', '100', '10', '1', '07', '7', '7', '7', '7', '7']
>>> Squad[-1]
'7'
>>> 1+Squad.index(Squad[-1]) #Checking the formula
11
>>> Squad.count("7") + Squad.index(Squad[-1])
15
>>> Squad.count("7") + Squad.index(Squad[-1]) #Yay,formula is working.
15
>>> 
