import math
import random
import pickle
import mymodulefile
import time
import calendar
import re

print("Hello Python")
print("Printing pythons Int and String class")
help(int)
help(str)
print("Printing count method in str class")
help(str.count)

# Python Variables
intVar = 4
floatVar = 5.55
stringVar = "Hey iOS and Python Developer"

print("Int values : ", intVar, " Float values : ", floatVar, " String Values : ", stringVar)

# Assigning values to multiple variables
var1 = var2 = var3 = var4 = 44
print("All variable values are ")
print(var1)
print(var2)
print(var3)
print(var4)
# Swapping values
x = 4
y = 2
print("Before swapping X value ", x)
print("Before swapping Y value ", y)
# Now I'm going to swap above variables
y, x = x, y
print("After swapping X value ", x)
print("After swapping Y value ", y)

# Getting values from the user               # This is not working for some reason will fix it later for sure...
#receivedVal = input("What's your designation?")
#print("He/She is ",receivedVal)

# Converting values in int datatype to string
myIntVal = 4
print("myIntVal datatype is ", type(myIntVal))
myIntVal = str(myIntVal)
print("Converted myIntVal datatype is ", type(myIntVal))

# Using builtin modules
math.pi

# Numbers
# Integers
i = 10
print(i)

# Float
f = 4.40
print(f)

# types
type(f)

# Strings and Characters
charVal = 'V'
print(charVal)
type(charVal)

strVal = "Vinoth"
print(strVal)

strValNew = "Vinoth"
print(strValNew)

id(strVal)
id(strValNew)

# Operations on Strings
strValNew[0]
print(strValNew)

strValNewNew = strValNew * 4
print(strValNewNew)

print(strValNewNew[1: 5])
print(strValNewNew[ : 3])
print(strValNewNew[2 : ])

# Returning ASCII code of character
print(ord('R'))

print("Length of the strValNewNew", len(strValNewNew))
print("Max of the strValNewNew", max(strValNewNew))
print("Min of the strValNewNew", min(strValNewNew))

# Iterating string using for loop
name = "Vinoth"
for i in name:
	print(i, end = " rashiee\n")

# Python conditions
a = 5
if a==5:
	print("hey iOS Developer")
else:
	print("Sorry")


# For loop 
num = 2
for b in range(1,5):
	print(num * b)

# While loop

a = 10
while a > 0:
	print("value of a is ",a)
	a = a - 2

#Python break
print("Break statement")
for i in [1,2,3,4,5,6,7,8]:
	if i==5:
		break
	print("i value is ",i)

#Python continue
print("Continue statement")
for i in [1,2,3,4,5,6,7]:
	if i==5:
		continue
	print("i value is ",i)

#Python pass statement
print("Pass statement")
for i in [1,2,3,4,5,6]:
	if i==3:
		pass
	print("i value is ",i)

# Python List
list1 = [1,2,3,4,5,6,7]
print("Length ",len(list1))
print("Max",max(list1))
print("min ",min(list1))
print("Sum ",sum(list1))
inVal = 5 in list1
print(inVal)
notInVal = 5 not in list1
print(notInVal)

#Slice operation in list
print(list1)
threeToSix = list1[2:6]
print(threeToSix)
upToSeven = list1[:7]
fromTwoToEnd = list1[1:]
print(upToSeven)
print(fromTwoToEnd)

#Concatenating lists
list2 = [9,10,11]
listAdd = list1 + list2
print(listAdd)

#replicating lists
listRep = list2 * 2
print(listRep)

# In and Not int
inCheck = 9 in listRep
print(inCheck)
notInCheck = 5 not in listRep
print(notInCheck)

# Traversing list
for t in list1:
	print(t, end=" ")

#List methods
list2.append(12)
print("List 1 Appended",list2)

list1.extend(list2)
print("List 1 Extended ",list1)

indexValOfSix = list1.index(6)
print("Index val ",indexValOfSix)

print("List 2 values : ",list2)
list2.insert(2, 8)
print("After insertion at index 2 : ",list2)

list2.pop(2)
print("After popped the number 8 from list 2 is ",list2)

list2.pop()
print("It removes the last digit in list2 ",list2)

list2.remove(9)
print("Removing number 9 from the list2 is ",list2)

print("Before reversing the value of list 2 is ",list2)
reversedVal = list2.reverse()
print("After reveersing the vlaue of list 2 is ",list2)

list3 = [5,3,6,7,2,9,1]
print("Before sorting the list 3 : ",list3)
list3.sort()
print("After sorting the list 3 : ",list3)

# List comprehension

list4 = [x for x in range(8)]
print(list4)

list5 = [x+3 for x in range(6)]
print(list5)

list6 = [x for x in range(6) if x % 2 == 0]
print(list6)

# Dictionaries
dict_emp = {} # empty dictionary

#Adding values in the dictionary
dict_emp['name'] = "Rashiee" 
dict_emp['rollno'] = 42
dict_emp['designation'] = "Interior Designer"
dict_emp['regno'] = 78
print("Name : ", dict_emp['name'])
print(dict_emp)

#deleting key value from dictionary
del dict_emp['regno']
print(dict_emp)

# Looping items in the dictionary
for keyVal in dict_emp:
	print(keyVal, " : ", dict_emp[keyVal])

# Finding the length of the dictionary
lenVal = len(dict_emp)
print(lenVal)

# in or not in operator
rollnoInDictEmpStatus = "rollno" in dict_emp
print("Rollno key is presented in dictemp : ",rollnoInDictEmpStatus)

#Dictionary methods
print(dict_emp)
dict_emp.popitem()
print(dict_emp)

dict_new = {}
dict_new['name'] = "vinoth"
dict_new['des'] = "iOS Developer"
dict_new['machinelearning'] = "Python"

print("Before clearing dict_new")
print(dict_new)
dict_new.clear()
print(dict_new)

dict_new['name'] = "vinoth"
dict_new['des'] = "Python Developer"
dict_new['machinelearning'] = "AI"
keyValues = dict_new.keys()
print(keyValues)
valuesInDict = dict_new.values()
print(valuesInDict)

print(dict_new.get('des'))
dict_new.pop("des")
print(dict_new)

#Tuples

t1 = ()
t2 = (5,6,3,6,2,7)
t3 = tuple([2,3,5,6,3,2,6])
t4 = tuple("Rashiee")
print(type(t3))
print(t4)

# Methods in tuples
print(min(t2))
print(max(t2))
print(sum(t2))
print(len(t2))

#Iterating through tuples
for i in t2:
	print(i, end=" ")

#Slicing operator
print("\n",t2[0:4])

#in and not in operator
fiveIn = 5 in t2
print(fiveIn)

fiveNotIn = 5 not in t2
print(fiveNotIn)

# Data type conversion
i = 11
convertedIval = float(11)
print(type(convertedIval))

f = 14.55
convertedFval = int(f)
print(type(convertedFval))

#Rounding numbers
i = 23.53053
print(round(i, 3))

# Python Control Statements
i = 10
if i % 2 == 0:
	print("Number is even")
else:
	print("Number is odd")

#if elif statement
today = "Tuesday"
if today == "Monday":
	print("This is monday")
elif today == "Tuesday":
	print("This is Tuesday")
elif today == "Wednesday":
	print("This is wednesday")
else:
	print("something else")

# Nested if statement
today = "holiday"
bankbal = 24000
if today == "holiday":
	if bankbal > 20000:
		print("Go for shopping")
	else:
		print("Watch Tv")
else:
	print("Normal working day")

# Python functions
def sum(start, end):
	result = 0
	for i in range(start,end + 1):
		result += i
	print(result)
sum(4,7)

#Function with return value
def sum(start, end):
	result = 0
	for i in range(start, end + 1):
		result += i
	return result
s = sum(10,50)
print(s)

#Global and Local variables
global_var = 50
def myfunc():
	local_var = 40
	print(global_var)
myfunc()
# print(local_var) 

t = 1
def increment():
	global t 
	t = t + 1
	print(t)
increment()
print(t)

def foo():
	global x
	x = 100
foo()
print(x)

def funcArg(i, j = 150):
	print(i, j)
funcArg(2)
funcArg(3,55)

def keywordArg(name, greeting):
	print(greeting + " " + name)
keywordArg(name="Vinoth", greeting="Hello")
keywordArg(greeting = "Helo", name="Vinoth")

#Returning multiple values from function
def returnMultipleValues(i1,i2):
	return i1, i2
s = returnMultipleValues(4,5)
print(s)
print(type(s))


# For loop
my_list = [3,5,6,7,2,8]
for i in my_list:
	print(i)

#for loop with range function
print("Loop with range function")
for r in range(1,11):
	print(r)

# Range with three parameters
print("Range with three parameter")
for v in range(1,10,2):
	print(v)

# While loop
print("While loop")
count = 0
while count < 10:
	print(count)
	count += 1

#break statement
count = 0
print("Break statement")
while count < 10:
	count += 1 
	if count == 5:
		break
	print("Inside the loop",count)
print("Out of the loop")

# Continue loop
print("Continue statement")
count = 0
while count < 10:
	count += 1
	if count % 2 == 0:
		continue
	print(count)

#Mathematical functions
print(abs(-22))
print(max(3,5,2,9,5,1))
print(min(8,4,2,5,1,9))
print(pow(4,2))
print(round(3.23))
print(round(3.2356,2))
print(math.ceil(3.4123))
print(math.floor(24.99392))

# Generating random numbers
for i in range(1,10):
	print(random.random())

for i in range(0,10):
	print(random.randint(1, 10))

# Python file handling
print("File writing")
f = open("vino.txt", "w")
f.write("This is first line\n")
f.write("This is second line\n")
f.close()

print("Reading all the data at once")
f = open("vino.txt", "r")
print(f.read())
f.close()

print("Reading all lines as an array")
f = open("vino.txt","r")
flist = f.readlines()
print(flist)
f.close()
print(type(flist))
print(type(f))

print("Reading one line at a time")
f = open("vino.txt","r")
print(f.readline())
f.close()

# Appending data
f = open("vino.txt","a")
f.write("This is third line")
f.close()

print("Looping through the data using for loop")
f = open("vino.txt","r")
for line in f:
	print(line)
f.close()

# Reading and writing binary datas
print("Writing datas")
f = open("pick.dat","wb")
pickle.dump(11,f)
pickle.dump("This is a line",f)
pickle.dump([2,3,5,6,7],f)
f.close()

print("Reading data")
f = open("pick.dat","rb")
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()

# python classes 
class MyClass:
	"This is javatpoint"
	a = 40
	def mytpointfunc(self):
		print("Hello javatpoint")

print(MyClass.a)
print(MyClass.__doc__)
print(MyClass.mytpointfunc)
obj = MyClass()
print(obj.mytpointfunc())

# Python object class example
class Student:
	def __init__(self, rollno, name):
		self.rollno = rollno
		self.name = name
	def displayStudent(self):
		print("Roll no : ",self.rollno, ", Name : ",self.name)
emp1 = Student(121,"Vinoth")
emp2 = Student(122,"Rashiee")
emp1.displayStudent()
emp2.displayStudent()

#Pythonguru classes and objects
class Person:

	#constructor or initializer
	def __init__(self, name):
		self.name = name

	def display(self):
		return "You are "+ self.name

p1 = Person("Vino")
print(p1.display())
print(p1.name)

class BankAccount:

	def __init__(self, name, money):
		self.__name = name
		self.__balance = money

	def deposit(self, money):
		self.__balance += money

	def withdraw(self, money):
		if self.__balance > money:
			self.__balance -= money
			return money
		else:
			return "Insufficient funds"

	def checkbal(self):
		return self.__balance

b1 = BankAccount("vino",400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbal())
print(b1.withdraw(800))
print(b1.checkbal())

# Operator Overloading
class Circle:

	print("Circle class")
	def __init__(self, radius):
		self.__radius = radius

	def setRadius(self, radius):
		self.__radius = radius

	def getRadius(self):
		return self.__radius

	def area(self):
		return math.pi * self.__radius ** 2

	def __add__(self, another_circle):
		return Circle(self.__radius + another_circle.__radius)

c1 = Circle(4)
print(c1.getRadius())

c2 = Circle(5)
print(c1.getRadius())

c3 = c1 + c2
print(c3.getRadius())

#Inheritance
class Vehicle:

	def __init__(self, name, color):
		self.__name = name
		self.__color = color

	def getColor(self):
		return self.__color

	def setColor(self, color):
		self.__color = color

	def getName(self):
		return self.__name

class Car(Vehicle):

	def __init__(self, name, color, model):
		super().__init__(name, color)
		self.__model = model

	def getDescription(self):
		return self.getName() + self.__model + " in " + self.getColor() + " Color"

c = Car("Ford","Violet","GT340")
print(c.getDescription())
print(c.getName())

# Multiple Inheritance

class MyClass1():

	def method_super1(self):
		print("Method from myclass 1")

class MyClass2():

	def method_super2(self):
		print("Method from myclass 2")

class ChildClass(MyClass1, MyClass2):

	def child_method(self):
		print("Child method")

c = ChildClass()
c.method_super1()
c.method_super2()
c.child_method()

# Overriding methods

class A:

	def __init__(self):
		self.__x = 1

	def m1(self):
		print("m1 from A")

class B(A):

	def __init__(self):
		self.__y = 1

	def m1(self):
		print("m1 from B")

c = B()
c.m1()

#isInstance() function

print(" One is instance of int class ? ",isinstance(4, int))
print(" 1.2 is instance of int class ? ",isinstance(1.2, int))
print(" 1,2,3,4 is instance of int class ? ",isinstance([1,2,3,4], list))

# Python Exception handling
try:
	f = open("vinoth.txt","r")
	print(f.read())
	f.close()
except IOError:
	print("File not found")

try:
	num1, num2 = 5,4#eval(input("Enter two numbers, sparated by a comma :"))
	result = num1/num2
	print("Result is ",result)

except ZeroDivisionError:
	print("Division by zero is error")

except SyntaxError:
	print("Comma is missing. Enter numbers separated by comma")

except:
	print("Wrong input")

else:
	print("No exceptions")

finally:
	print("This will execute no matter what")

#Custom Exception class
def enterage(age):
	if age < 0:
		raise NegativeAgeException("Only positive integers are allowed")

	if age % 2 == 0:
		print("Age is even")
	else:
		print("Age is odd")

try:
	num = 5 #int(input("Enter your age: ")) 
	enterage(num)
except NegativeAgeException:
	print("Only positive integers are allowed")
except:
	print("somethig is wrong")

# Python Modules
print(mymodulefile.foo)
print(mymodulefile.dev())

print("All attributes in mymodulefile : ",dir(mymodulefile))

# Python Time
localTime = time.asctime(time.localtime(time.time()))
print("Current time : ",localTime)

#Python calendar
cal = calendar.month(2017, 9)
print("Current month is ")
print(cal)

#Printing whole month in 2017
print("All months in 2017")
print(calendar.prcal(2017))

print("Printing 2017 april month")
print(calendar.prmonth(2017,4))

#Python args
print("\nPython args\n")
def sum(*numbVal):
	s = 0
	for i in numbVal:
		s += i
	print("Sum is",s) 

sum(4,5,6,7)
sum(5,2,5,6,6,7,4,2,2)

#Python kwargs
print("\nPython kwargs\n")
def kwargsMethod(**mykwargs):
	for i, j in mykwargs.items():
		print(i, j)

kwargsMethod(name="vino", sport="football", rollno=42)

#Python generators
print("python generators")
def my_range(start, stop, step = 1):
	if stop <= start:
		raise RuntimeError("Start must be smaller than stop")
	i = start
	while i < stop:
		yield i 
		i += step

try:
	for yieldVal in my_range(12,50,4):
		print(yieldVal)
except RuntimeError as ex:
	print(ex)
except:
	print("Unknown error occurred")

#Python regular expressions
print("Python regular expressions")
s = "my ph number is 802"
matchVal = re.search(r"\d\d\d", s)
print("Match Values are ",matchVal)
print("Filtered values : ",matchVal.group())

s2 = "tim email is tim@somehost.com"
match = re.search(r"[\w.-]+@[\w.-]+",s2)

if match:
	print(match.group())
else:
	print("match not found")

#Group capturing
match = re.search(r"([\w.-]+)@([\w.-]+)",s2)
if match:
	print(match.group())
	print(match.group(1))
	print(match.group(2))

s3 = "Vinoth's phone numbers are 12345-34343 and 45948"
match = re.findall(r"\d{5}",s3)

if match:
	print(match)

s4 = "Tim's phone no are 24342-24344 and 85858-47474"
match = re.findall(r"(\d{5})-(\d{5})",s4)
print(match)

for i in match:
	print()
	print(i)
	print("First Group",i[0])
	print("Second Group",i[1])

s5 = "vino ios developer"
match = re.match(r"vin",s5)
if match:
	print(match.group())

s6 = "vino ios developer"
match = re.search(r"^vin",s6)
if match:
	print(match.group())

# Python lamda function
r = lambda x, y: x + y
print(r(4,4))

