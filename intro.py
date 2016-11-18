from __future__ import print_function

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
# below doesn't work but not sure why; prints at each loop
def primefun (num):
    for i in range(num-1,2,-1): # from Marley's code, accounts for python counting, looping problem
        if (num % i) == 0:
            break
            print (num, "is not a prime number")            
        elif (num % i) != 0: 
            print (num, "is prime")               
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
    return True

# Q6 Write a function that loads a text file, loops over the lines in it, and 
# prints out the fifth character on the fifth line of that file.
# “Hint” (really, frankly, this is the solution):
# with open("name_of_file") as handle:
# for line in handle:
# Do something
# on home computer:
text = open("/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt")
text.read() # returns text
# to find out what kind of object this is
type(text) # returns <class '_io.TextIOWrapper'>  whatever that is ***
# so I didn't open this correctly
open("/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt") 
# returned error, invalid syntax...so that doesn't work
# online help: "You can read the file as a list of lines by simply calling list() on the file object:"
# with open('goodlines.txt') as f:
    # mylist = list(f)
with open('/Users/karenmock/Dropbox/ProgrClass2016/python-introduction-karenmock/Adams_quote.txt') as f
	quote = list(f)
# error: invalid syntax
# other online help:
quote = text.readlines()
type(quote) # returns ,class 'list'>
len(quote) # returns 0
quote # returns []
# so that didn't work either.
# Will: can you give me a clue here? 
	


 



    
