#STEP 1 COMUPTE A*C
#STEP 2 COMPUTE B*D
#STEP 3 COMPUTE (A+B)(C+D)
#STEP 4 COMPUTE 3 - 2 - 1
import math




x = int(input("Provide first integer "))
y = int(input("Provide second integer "))




def karat(x, y):
    if x < 10 or y < 10:
        return x*y

   
    length1 = len(str(x))
    length2 = len(str(y))

 

    n = max(length1, length2)
    n2 = round(n/2)


    a = x // (10 ** n2)
    b = x % (10 ** n2)
    c = y // (10 ** n2)
    d = y % (10 ** n2)


 
    
    ac = karat(a,c)
    bd = karat(b,d)
    abcd = karat(a + b, c + d) - ac - bd
    
    return (10** (2*n2))*ac + (10**(n2))*abcd + bd

    

answer = karat(x,y)
print(str(answer))
