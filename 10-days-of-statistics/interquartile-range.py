# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import median

n=int(input())
arr=[int(x) for x in input().split()]
arr2=[int(y) for y in input().split()]

input_arr=[]
for i in range(len(arr2)) : 
    input_arr.extend([arr[i] for ii in range(arr2[i])])

input_arr.sort()
# print(input_arr)

mid=int(len(input_arr)/2)
if len(input_arr)%2==0:
    L=input_arr[:mid]
    U=input_arr[mid:]
else:
    L=input_arr[:mid]
    U=input_arr[mid+1:]
# print(median(U),median(L))
print(round(float(median(U)-median(L)),1))
