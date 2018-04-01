Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> # Dictionary data structure
>>> dict1 = {'name' : 'godfather', 'age' : '60', 'role' : 'don'}
dict2 = {'name' : 'basha', 'age' : '56', 'role' : 'mafia don'}
dict3 = {'name' : 'balayya', 'age' : '62', 'role' : 'factionist'}
dict4 = {'name' : 'chiru', 'age' : '53', 'role' : 'mesthri'}
dict5 = {'name' : 'ali', 'age' : '32', 'role' : 'pitpocketer'}
>>> dict1
{'age': '60', 'role': 'don', 'name': 'godfather'}
>>> dict2

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    dict2
NameError: name 'dict2' is not defined
>>> dict2 = {'name' : 'basha', 'age' : '56', 'role' : 'mafia don'}
>>> dict2
{'age': '56', 'role': 'mafia don', 'name': 'basha'}
>>> dict3 = {'name' : 'balayya', 'age' : '62', 'role' : 'factionist'}
>>> dict3
{'age': '62', 'role': 'factionist', 'name': 'balayya'}
>>> dict4 = {'name' : 'chiru', 'age' : '53', 'role' : 'mesthri'}
>>> dict4
{'age': '53', 'role': 'mesthri', 'name': 'chiru'}
>>> dict4
{'age': '53', 'role': 'mesthri', 'name': 'chiru'}
>>> dict5 = {'name' : 'ali', 'age' : '32', 'role' : 'pitpocketer'}
>>> dict5
{'age': '32', 'role': 'pitpocketer', 'name': 'ali'}
>>> import scrapy

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import scrapy
ImportError: No module named scrapy
>>> dict1;dict2;dict3;dict4;dict5
{'age': '60', 'role': 'don', 'name': 'godfather'}
{'age': '56', 'role': 'mafia don', 'name': 'basha'}
{'age': '62', 'role': 'factionist', 'name': 'balayya'}
{'age': '53', 'role': 'mesthri', 'name': 'chiru'}
{'age': '32', 'role': 'pitpocketer', 'name': 'ali'}
>>> dict4['role']    #getting the key from dictionary
'mesthri'
>>> dict2['name']
'basha'
>>> dict5["role"]
'pitpocketer'
>>> dict1.fromkeys('age')
{'a': None, 'e': None, 'g': None}
>>> dict1.fromkeys('age' [,0])
SyntaxError: invalid syntax
>>> dict1["56"]

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict1["56"]
KeyError: '56'
>>> dict1.values(56)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict1.values(56)
TypeError: values() takes no arguments (1 given)
>>> dict1.values()
['60', 'don', 'godfather']
>>> dict1.values()    #get values of each key in the dictionary.
['60', 'don', 'godfather']
>>> dict2.values()    #get values of each key in the dictionary.
['56', 'mafia don', 'basha']
>>> dict1.keys()
['age', 'role', 'name']
>>> dict2.items()
[('age', '56'), ('role', 'mafia don'), ('name', 'basha')]
>>> dict5.items()     #lists out each key and it's values in the dictionary in a tupple form.
[('age', '32'), ('role', 'pitpocketer'), ('name', 'ali')]
>>> dict3.get("age")
'62'
>>> dict2.get("role")   #returns the key value.
'mafia don'
>>> dict2 ["role"]      #returns the key value.
'mafia don'
>>> dict3.has_key("age")   #checks if that particular key is dict3.Just give True or False in return.
True
>>> dict3.has_key("53")   #checking if this method can be used for values.
False
>>> dict4.has_key("53")
False
>>> dict4
{'age': '53', 'role': 'mesthri', 'name': 'chiru'}
>>> dict4.has_key("53")    #is not working for values..
False
>>> dict4.pop("age")      #removes the key from dict4.
'53'
>>> dict4
{'role': 'mesthri', 'name': 'chiru'}
>>> dict4.popitem()
('role', 'mesthri')
>>> dict4
{'name': 'chiru'}
>>> dict4.iteritems()
<dictionary-itemiterator object at 0x03123F90>
>>> dict1
{'age': '60', 'role': 'don', 'name': 'godfather'}
>>> dict1.iteritems()
<dictionary-itemiterator object at 0x0312B030>
>>> dict1.iterkeys()
<dictionary-keyiterator object at 0x03123F90>
>>> dict1.viewitems()
dict_items([('age', '60'), ('role', 'don'), ('name', 'godfather')])
>>> dict1.viewkeys()
dict_keys(['age', 'role', 'name'])
>>> dict1.viewvalues
<built-in method viewvalues of dict object at 0x03115030>
>>> dict1.viewvalues()
dict_values(['60', 'don', 'godfather'])
>>> dict1.clear()     #empties the dictionary.
>>> dict1
{}
>>> dict2.copy()
{'age': '56', 'role': 'mafia don', 'name': 'basha'}
>>> dict2
{'age': '56', 'role': 'mafia don', 'name': 'basha'}
>>> copydict2

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    copydict2
NameError: name 'copydict2' is not defined
>>> copy of dict2
SyntaxError: invalid syntax
>>> dict2.setdefault("role")
'mafia don'
>>> dict2.setdefault("class")
>>> dict2
{'age': '56', 'role': 'mafia don', 'name': 'basha', 'class': None}
>>> dict2.setdefault("role")
'mafia don'
>>> dict2
{'age': '56', 'role': 'mafia don', 'name': 'basha', 'class': None}
>>> dict1;dict2;dict3;dict4;dict5
{}
{'age': '56', 'role': 'mafia don', 'name': 'basha', 'class': None}
{'age': '62', 'role': 'factionist', 'name': 'balayya'}
{'name': 'chiru'}
{'age': '32', 'role': 'pitpocketer', 'name': 'ali'}
>>> dict1.fromkeys(dict5)
{'age': None, 'role': None, 'name': None}
>>> dict1
{}
>>> dict1 = dict.fromkeys(dict5, "naaku thelvadh")
>>> dict1
{'age': 'naaku thelvadh', 'role': 'naaku thelvadh', 'name': 'naaku thelvadh'}
>>> dict1 = dict.fromkeys(dict5, "naaku thelvadh")  #imports all the keys from dict5 and we can also assign them values in this method.
>>> dict1
{'age': 'naaku thelvadh', 'role': 'naaku thelvadh', 'name': 'naaku thelvadh'}
>>> dict1;dict2;dict3;dict4;dict5
{'age': 'naaku thelvadh', 'role': 'naaku thelvadh', 'name': 'naaku thelvadh'}
{'age': '56', 'role': 'mafia don', 'name': 'basha', 'class': None}
{'age': '62', 'role': 'factionist', 'name': 'balayya'}
{'name': 'chiru'}
{'age': '32', 'role': 'pitpocketer', 'name': 'ali'}
>>> dict1.update(dict4)
>>> dict1
{'age': 'naaku thelvadh', 'role': 'naaku thelvadh', 'name': 'chiru'}
>>> dict1.update(dict4)     # adds dict1 and dict4 and displays dict1 = dict1 + dict4
>>> dict1
{'age': 'naaku thelvadh', 'role': 'naaku thelvadh', 'name': 'chiru'}
>>> reversed(dict1)

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    reversed(dict1)
TypeError: argument to reversed() must be a sequence
>>> a = ("l","o","u","y","g","k")
>>> type(a)
<type 'tuple'>
>>> fresh = {}
>>> type(fresh)
<type 'dict'>
>>> fresh.fromkeys(a)
{'g': None, 'k': None, 'l': None, 'o': None, 'u': None, 'y': None}
>>> fresh.setdefault("newkey")
>>> fresh
{'newkey': None}
>>> ###Question
>>> fresh.update(a)

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    fresh.update(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> #thats a wrap of Dictionary
