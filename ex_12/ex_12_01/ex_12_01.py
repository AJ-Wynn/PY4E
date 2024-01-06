# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re
fhand = open('mbox.txt')

reg_exp = input("Enter a regular expression: ")

counter = 0
for line in fhand:
    line = line.rstrip()
    if re.search((reg_exp), line):
        counter = counter + 1


print("mbox.txt had %d lines that matched %s" % (counter, reg_exp))

