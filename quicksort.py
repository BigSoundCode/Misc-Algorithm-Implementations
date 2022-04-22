
fhand = open("quicksort.txt", "r")
quicktext = fhand.read().split()
arr = []

for thing in quicktext:
    arr.append(int(thing))

#arr = [2148,9058,7742,3153,6324,609,7628,5469,7017,504]

count = 0


def partition(arr, l, r):
    
    pivot = arr[l]
    i = l + 1
    j = l + 1
    while j < r:
        if arr[j] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i = i + 1
            
        j = j + 1
    
    tempL = arr[l]
    arr[l] = arr[i-1]
    arr[i-1] = tempL
    p = i - 1
    return p


def quicksort(arr, l, r):
    global count
    if r - l < 1:
        return
    
        
    p = partition(arr, l, r)
    count += (r - l - 1)
    
    quicksort(arr, l, p)
    quicksort(arr, p+1, r)
    
    
length = len(arr)
quicksort(arr, 0, length)


print(count)