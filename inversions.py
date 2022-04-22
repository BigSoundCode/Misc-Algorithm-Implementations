import os, sys

fhand = open("integers.txt", "r")
integers_text = fhand.read().split()
integers = []


for thing in integers_text:
    integers.append(int(thing))

#initialize counter

test = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

#split until base case
#base case, if appending array from rhs, increment counter. return counter.



def mergesort(A):
    
    if len(A) == 1:
        return A, 0
    else:
        left = A[0:len(A)//2]
        right = A[len(A)//2:]
    
        
        left, ai = mergesort(left)
        right, bi = mergesort(right)
        sort = []
        i = 0
        j = 0
        count = 0 + ai + bi

        
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sort.append(left[i])
                i = i + 1
            
            else:
                sort.append(right[j])
                j = j + 1
                count += len(left) - i
                
        
        
        sort += right[j:]
        sort += left[i:]
   


    return sort, count


sort, count = mergesort(integers)
print(sort, count)

