import sys

if 5 > 2:
    print("five is greater than two")
else:
    print("five is not greater than two")   

### Variables - Start ###
x = 5
X  = "Hello"
#print(X)
#print(y)

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
#print(x + y + z)

# Working with Global Variables

def myfunc():
    x = "fun!"
    print("Python is " + x)

#myfunc()

#print("Python is " + x)

# The global Keyword
def myfunc1():
    global x
    x = "fantastic" 

myfunc1()

print("Python is " + x)

## Data Types - Start ###
x = 5               # int
y = 5.5             # float
z = 1j              # complex
a = "Hello"         # str
b = True            # bool
c = None            # NoneType

d = ["apple", "banana", "cherry"]  # list
e = ("apple", "banana", "cherry")  # tuple
f = range(6)                      # range
g = {"name": "John", "age": 36}    # dict
h = {"apple", "banana", "cherry"}   # set
i = frozenset({"apple", "banana", "cherry"})  # frozenset
j = bytes(5)                     # bytes
k = bytearray(5)                 # bytearray
l = memoryview(bytes(5))         # memoryview
### Data Types - End ###
"""
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))

import random
print(random.randrange(1,10))
"""
a = "Hello, World!"
print(a[1])
print(a[-5:-2])
print(a.lower())
print(a.strip(""))
print(a.replace("H", "J"))
print(a.split(","))


for x in "banana":
    print(x)
txt = "The best things in life are free!"
print("z" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

age = 36
#This will produce an error:
txt = f"My name is John, I am {age}"
print(txt)
txt = f"My name is John, I am {age:.2f}"
print(txt)
txt = f"My name is John, I am {age*20}"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "We are the so-called \n from the north."
print(txt)
txt = "FROM the north."
print(txt.center(50))

print(10 > 9)
print(10 == 9)
print(10 < 9)