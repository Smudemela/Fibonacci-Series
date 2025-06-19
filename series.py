# Rounds in the program
x = int(input("enter the number of rounds: "))

# Variables for the Program
a =0
b =1
i =0

# Loop
while i<x:
    print(a)
    c=a+b
    a = b
    b = c
    i+=1
