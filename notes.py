#this will print the characters sequentially
#end=""
#OpenEDG Python Institute
text = "OpenEDG Python Institute"
for letter in text:
    print(letter, end="")

#int = float
x = 1
y = 1.0
z = "1"
x == y #True
y == int(z) #True

#default values for booleans: 0 for False, 1 is True
"""number != 0""" equivalent to """number""" #because 1 is True
"""number % 2 == 1""" equivalent to """number % 2"""

range(100) # starts from 0 .. 99. If no first number, the inital position is 0.
range(2, 8, 3) # first pos = 2, last pos = 7, 3 is the increment. -> 2,5

#break statement breaks out of the for/while loop immediately
#Inside the loop. 1
#Inside the loop. 2
#Outside the loop.
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

#else statement for while & for loops is executed only once, regardless if the loop condition is true or false
#1
#2
#3
#4
#else: 5
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

#watch out in the for loop, the else statement is executed a bit differently
#it will not reiterate at range 5, i = 4
#0
#1
#2
#3
#4
#else: 4
for i in range(5):
    print(i)
else:
    print("else:", i)

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

#If you have a list l1, then the following assignment: l2 = l1 does not make a copy of the l1 list, 
#but makes the variables l1 and l2 point to one and the same list in memory.
l1 = ['car', 'bicycle', 'motor']
print(l1) # outputs: ['car', 'bicycle', 'motor']

l2 = l1
del l1[0] # deletes 'car'
print(l2) # outputs: ['bicycle', 'motor']

#If you want to copy a list or part of the list, you can do it by performing slicing:
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

#You can use negative indices to perform slices, too.
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

#The start and end parameters are optional when performing a slice: list[start:end]
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

#this prints
# [2]
my_list = [1,2,3,4]
a = my_list[-3:-2]

#You can delete slices using the del instruction:
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]
del my_list[:]
print(my_list)  # deletes the list content, outputs: []


#You can test if some items exist in a list or not using the keywords in and not in, e.g.:
my_list = ["A", "B", 1, 2]
print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

#prints ['B', 'C']
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2
print(list_3)


#The snippet produces a ten-element list filled with squares of ten integer numbers starting from zero.
squares = [x ** 2 for x in range(10)]
#The snippet makes a list with only the odd elements of the squares list.
odds = [x for x in squares if x % 2 != 0 ]

#As list comprehensions can be nested, the inner part creates a row, and the outer part builds a list of rows.
board = [[EMPTY for i in range(8)] for j in range(8)]

#bitwise operators
#& requires exactly two 1s to provide 1 as the result; 1&0=0; 1&1=1
#| requires at least one 1 to provide 1 as the result; 1|0=1; 0|0=0
#^ requires exactly one 1 to provide 1 as the result. 1^0=1; 1^1=0

#Binary left shift and binary right shift
17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 
#(shifting to the right by one bit is the same as integer division by two)
17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 
#(shifting to the left by two bits is the same as integer multiplication by four)

#keyword argument passing
#SyntaxError - a non-default argument (c) follows a default argument (b=2)
def add_numbers(a, b=2, c):
    print(a + b + c)
add_numbers(a=1, c=3)

#positional argument passing.
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")
intro("Susan") #My name is Bond. Susan.

#It's important to remember that positional arguments mustn't follow keyword arguments. 
def subtra(a, b):
    print(a - b)
subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error

#None
#if a function doesn't return a certain value using a return expression clause, 
#it is assumed that it implicitly returns None
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2)) #True
print(strange_function(1)) #None


