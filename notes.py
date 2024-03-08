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
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
