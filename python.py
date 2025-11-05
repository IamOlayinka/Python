age = 56
a = f"The name of my school is Algonquin college. The school will be {age * 2:.2f} this November"

print(a)


txt = "We are the so-called \"Vikings\" from the north.\nWe are the best!"
print(txt)

b = "Hello, World!"
print(b.center(20, '-'))

c= "Hello"
d = "World"
e =10
f=""
g=0
h=3

print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))

if y :=3 >= 4:
    print("Y is greater than 2")
else:
    print("Y is less than 2")


myList = list(("apple", "banana", "cherry"))

print(myList)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-6:-3])

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print(len(thislist))
print(range(len(thislist)))

thislist.insert(2, "orange")
thislist.append("grape")
#thislist.remove("banana")
thislist.pop()
#thislist.clear()
thislist2 = thislist.copy()
#thislist.pop(2)
#del thislist[0]
#del thislist2       
print(thislist2)        

thislist2 = [x for x in thislist2 if "a" in x]
print(thislist2)

number = [x for x in range(15) if x % 2 == 0]
print(number)

number2 = [x if x % 2 == 0 else x * 100 for x in range(15)]

number3 = [20,21,12,30,90,15,50,70,5]
def myFunction(n):
    return abs(n - 5)

number4 = sorted(number3, key = myFunction)
print(number4)  
number3.sort(key = myFunction)

print(number3)
thislist.sort(key = str.lower)
print(thislist)

thislist3 = thislist.copy()
thislist4 = list(thislist3)

print(thislist4, thislist3)

def my_function(myfunc):
    def wrapper():
        return myfunc(5) * 10
    return wrapper

@my_function
def myfunc (x):
    return x + 5

print(myfunc())

x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5, 6))


new_number = list(map(lambda x : x * 2, number))
print(new_number)

import math

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")