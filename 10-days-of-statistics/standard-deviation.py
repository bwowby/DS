from statistics import pstdev

n = input()
input_list = list(map(int,input().split()))

print(round(pstdev(input_list),1))
