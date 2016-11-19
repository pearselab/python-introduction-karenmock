# from __future__ import print_function (if using Python 2
# Office PC: /Users/A00017458/Dropbox/ProgrClass2016/python-introduction-karenmock
# Home Mac: /Users/A00017458/Dropbox/ProgrClass2016/python-introduction-karenmock

# Python Exercises 9.5
# Q1 Write a loop that prints out the numbers from 20 to 10
# with Paul's help on running python scripts from Text Wrangler
# originally I had tried to create a list and print in 
# reverse, but this is simpler
for i in range(20,9,-1):
    print (i)

# Q2 Write a list comprehension that returns the numbers from 20 to 10
x = []
x = [print(i)for i in range(20,9,-1)]

# Q3 Write a loop that prints out only the numbers 
# from 20 to 10 that are even
for i in range(20,9,-1):
	if i%2 == 0:  # alternatively could step downward by 2
	    print(i, "+") # + is a nice way to see most recent printing 

# Q4 Write a list comprehension that prints out only the 
# numbers from 20 to 10 that are even
y = []
y = [print(i) for i in range(20,9,-1) if i%2 == 0]

# Q5 Write a function that calculates whether a number 
# is a prime number (hint: what does 2 % 3 give you?
# after much floundering, resorted to cheating
# Marley's code: (works)
def prime (x):
    for i in range(x-1, 2, -1):
    	print i
        p = x % i  #works because below, nothing happens if p != 0
        if p == 0:
            return False
    return True  
# experiment in Python to try to understand range
for i in range(5-1,2,-1):
    print (i) # returns 4,3, which is what we want for the primefun
for i in range(5-1,2,1):
    print (i) # doesn't return anything because range cant run
for i in range(2,5-1,1):
    print (i) # returns 2,3, not what we want
for i in range(2-1,2,-1):
    print (i) # doesn't return anything because range can't run      
# Playing with Marley's code: this works
def is_prime (num):
    for i in range(num-1, 2, -1):
        if num % i == 0:
            return False  #return statement breaks the loop whenever there is a 0
    return True #returns True if the end of the range is reached without a 0  
# Don't know how to get a print statement into this function instead of True or False ***
def is_prime (num):
	for i in range(num-1, 2, -1):
        if num % i == 0:
            return False
        elif num == 4:
            return False
    return True

# Q6 Write a function that loads a text file, loops over the lines in it, and 
# prints out the fifth character on the fifth line of that file.
# “Hint” (really, frankly, this is the solution):
# with open("name_of_file") as handle:
# for line in handle:
# Do something
# on home computer:
# text = open('/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt', 'rU')
# text.read() # returns text
# to find out what kind of object this is
# type(text) # returns <class '_io.TextIOWrapper'>  whatever that is ***
# so I didn't open this correctly
# hours later, turns out that this text had no line breaks so nothing was working.
# re-formatted the text file to have line breaks
# following Will's hint and Paul's code and counseling:
# Home Mac: with open('/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt', 'rU') as quote:
with open('/Users/A00017458/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt', 'rU') as quote:
    counter = 1
    for line in quote:
        if counter == 5:
            print (counter," ", line[4])
        counter+=1
# above works
# TIPS from Paul:
# with 'open' command, always want to include a 'close' command too so it doesn't clog up python
# text.close()
# the 'with' command means with the file open, do this stuff and then close it
# always be sure the text file is 'unix'
# r = read only
# U = universal (for opening difft text file types other than unix); accepts different line break symbols
# now make this a list comprehension without the counter
with open('/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt', 'rU') as quote:
    lines = [print(line) for line in quote]
# above works
# now for letter 5 in line 5 (with python counting); first without list comprehension
# for home mac: with open('/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt', 'rU') as quote:
with open('/Users/A00017458/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt', 'rU') as quote:
    counter = 1
    for line in quote:
        if counter == 5:
            print (counter," ", line[4])
        counter+=1
# Works!

# Q7 Write a loop that prints out the numbers from 1 to 20, printing “Good: NUMBER” if
# the number is divisible by five and “Job: NUMBER” if then number is prime, and nothing otherwise.
def is_prime (num): # re-run the is_prime function
    for i in range(num-1, 2, -1):
        if num % i == 0:
            return False
        elif num == 4:
            return False #return statement breaks the loop whenever there is a 0
    return True
for i in range(1,20):
    if i%5 == 0:
        print (i, " Good: Number")
    elif is_prime(i):
        print (i, " Job: NUMBER")
    else:
        print (i)
# Works!

# Q8 A biologist is modelling population growth using a Gompertz curve, which is defined
# as y(t) = a.e−b.e−c.t
# where y is population size, t is time, a and b are parameters, and e is the
# exponential function. Write them a function that calculates population size at any time
# for any values of its parameters.
def gomp(a,b,c,t):
    import math
    y = (a * math.exp(-b * math.exp(-c * t)))
    return (y)   
print (gomp(6,40,7,2))
# Works!

# Q9 Write a function that draws boxes of a specified width and height that 
# looks like this (height 3, width 5):
# *****
# *   *
# *****
# (Hint: what does print("*" + "" + "*"*4) give you?)
def box(h,w):
    print ((("*" * w) + "\n") 
    + ("*" + ((" ") * (w-2)) + ("*"  + "\n")) * (h-2)
    + ("*" * w)) 
box(8,9) 
# Works! Did not make an error message for values <3
def box(h,w):
    if h > 2 and w > 2:
        print ((("*" * w) + "\n") 
        + ("*" + ((" ") * (w-2)) + ("*"  + "\n")) * (h-2)
        + ("*" * w)) 
    else:
        print ("h and w should be > 2")
box (6,10)
box (3,3)
box (2,3) 
# Works!

# Q10 Implement a point class that holds x and y information for a point in space. 
# Note that I am not asking you to plot that line.
class Points:
    def __init__(self, Xcoord, Ycoord):
    	self.Xcoord, self.Ycoord = Xcoord, Ycoord
Point1 = Points(5,6)
# print(Point1.Ycoord)  # was not expecting to have to print this
# print(dir(Point1))
# Works!

# Q 11 Write a distance method that calculates the distance between two points in space.
# STUCK on this one...
# class Points:
#     def __init__(self, X, Y):
#         self.X, self.Y = X, Y
#     def dist(First, Second):  # need to make sure these are Points class?
#         import math
#         side1 = First.Y - Second.Y
#         print(side1)
#         side2  = First.X - Second.X
#         print(side2)
#         h = math.sqrt(side1**2 + side2**2)
#         return h
# P1 = Points(5,6)
# P2 = Points(7,12)
# dist(P1,P2) # need to have the command be xxx.dist...but the pair of points is not the object
# gives error that dist is not defined
# not sure whether to write a separate class with dependency on the Points class or just what.






