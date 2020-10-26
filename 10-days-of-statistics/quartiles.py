from statistics import median

n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()

mid=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:mid]
    U=arr[mid:]
else:
    L=arr[:mid]
    U=arr[mid+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))
