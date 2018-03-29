Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Barca = [ "messi", "suarez", "mina", "semedo", "iniesta"]
>>> Real = 0
>>> 
>>> for p in Barca:
	if p == "iniesta":
		Real = Real + 1
		print "star", p
	else:
		print "Zero", p

		
Zero messi
Zero suarez
Zero mina
Zero semedo
star iniesta
>>> a = range(1,20)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> 
>>> 
>>> for i in a:
	if i = 19:
		
SyntaxError: invalid syntax
>>> for i in a:
	if i == 19:
		Real = Real+1
		print "emle", i
	else:
		print "dorkindi",i   #fingers crossed

		
dorkindi 1
dorkindi 2
dorkindi 3
dorkindi 4
dorkindi 5
dorkindi 6
dorkindi 7
dorkindi 8
dorkindi 9
dorkindi 10
dorkindi 11
dorkindi 12
dorkindi 13
dorkindi 14
dorkindi 15
dorkindi 16
dorkindi 17
dorkindi 18
emle 19
>>> Barca
['messi', 'suarez', 'mina', 'semedo', 'iniesta']
>>> Barca.append("coutinho")
>>> Barca.append("umtiti")
>>> Barca.append("alena")
>>> Barca.append("stegen")
>>> Barca.append("isco")
>>> Barca.append("neymar")
>>> Barca
['messi', 'suarez', 'mina', 'semedo', 'iniesta', 'coutinho', 'umtiti', 'alena', 'stegen', 'isco', 'neymar']
>>> 
>>> for i in Barca:
	if i == "neymar":
		Real = Real+1
		print "", i
	else:
		print "RM sucks", i

		
RM sucks messi
RM sucks suarez
RM sucks mina
RM sucks semedo
RM sucks iniesta
RM sucks coutinho
RM sucks umtiti
RM sucks alena
RM sucks stegen
RM sucks isco
 neymar
>>> for i in Barca:
	
	else:
		print "RM sucks", i
		
SyntaxError: invalid syntax
>>> for i in Barca:
	
	else:
		
SyntaxError: invalid syntax
>>> for i in Barca:
	print "RM sucks", i
	else:
		
SyntaxError: invalid syntax
>>> 				
