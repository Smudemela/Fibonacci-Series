x = int(input("enter the number of rounds: "))

a =0
b =1
i =0
while i<x:
    print(a)
    c=a+b
    a = b
    b = c
    i+=1
