import math

a = 10
print(a)

x = math.cos(2 * math.pi)
print(x)

print(dir(math))

help(math.cos)

x = 1.0
print(type(x))

# dynamically typed
x = 1
print(type(x))

print(1 + 2, 1 - 2, 1 * 2, 1 / 2)

# integer division of float numbers
print(3.0 // 2.0)

# power operator
print(2 ** 2)
print(True and False)
print(not False)
print(True or False)
print(2 > 1, 2 < 1, 2 > 2, 2 < 2, 2 >= 2, 2 <= 2)

# equality
print([1,2] == [1,2])

s = "Hello world"
print(type(s))
print(len(s))

s2 = s.replace("world", "test")
print(s2)
print(s[0])
print(s[0:5])
print(s[6:])
print(s[:])

# define step size of 2
print(s[::2])

# automatically adds a space
print("str1", "str2", "str3")

# C-style formatting
print("value = %f" % 1.0) 

# alternative, more intuitive way of formatting a string 
s3 = 'value1 = {0}, value2 = {1}'.format(3.1415, 1.5)
print(s3)

z = [1, 2, 3, 4]
print(type(z))
print(z)

print(z[1:3])
print(z[::2])
print(z[0])

# don't have to be the same type
z = [1, 'a', 1.0, 1-1j]
print(z)

start = 10
stop = 30
step = 2
range(start, stop, step)

# consume the iterator created by range
print(list(range(start, stop, step)))

# create a new empty list
z = []

# add an elements using `append`
z.append("A")
z.append("d")
z.append("d")
print(z)

z[1:3] = ["b", "c"]
print(z)

z.insert(0, "i")
z.insert(1, "n")
z.insert(2, "s")
z.insert(3, "e")
z.insert(4, "r")
z.insert(5, "t")
print(z)

z.remove("A")
print(z)

del z[7]
del z[6]
print(z)

point = (10, 20)
print(point, type(point))

# unpacking
x, y = point
print("x =", x)
print("y =", y)

params = {"parameter1" : 1.0,
          "parameter2" : 2.0,
          "parameter3" : 3.0,}

print(type(params))
print(params)

params["parameter1"] = "A"
params["parameter2"] = "B"

# add a new entry
params["parameter4"] = "D"

print("parameter1 = " + str(params["parameter1"]))
print("parameter2 = " + str(params["parameter2"]))
print("parameter3 = " + str(params["parameter3"]))
print("parameter4 = " + str(params["parameter4"]))

statement1 = False
statement2 = False

if statement1:
    print("statement1 is True")
elif statement2:
    print("statement2 is True")
else:
    print("statement1 and statement2 are False")

for x in range(4):
    print(x)

for word in ["scientific", "computing", "with", "python"]:
    print(word)

for key, value in params.items():
    print(key + " = " + str(value))

for idx, x in enumerate(range(-3,3)):
    print(idx, x)

l1 = [x**2 for x in range(0,5)]
print(l1)

i = 0
while i < 5:
    print(i)
    i = i + 1
print("done")

# include a docstring
def func(s):
    """
    Print a string 's' and tell how many characters it has    
    """
    
    print(s + " has " + str(len(s)) + " characters")

help(func)

func("test")

def square(x):
    return x ** 2

print(square(5))

# multiple return values
def powers(x):
    return x ** 2, x ** 3, x ** 4

print(powers(5))

x2, x3, x4 = powers(5)
print(x3)

f1 = lambda x: x**2
print(f1(5))

print(list(map(lambda x: x**2, range(-3,4))))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))

p1 = Point(0, 0)
print(p1)

p2 = Point(1, 1)
p1.translate(0.25, 1.5)

print(p1)
print(p2)

try:
    print(test)                     # intend to be this
except:
    print("Caught an expection")

try:
    print(test)
except Exception as e:
    print("Caught an exception: " + str(e))

