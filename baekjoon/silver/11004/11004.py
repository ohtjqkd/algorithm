# iuput
# 5 2
# 4 1 2 3 5
# output
# 2

N, K = input().split(' ')
array = []

array = list(map(int, input().split(' ')))
    
array = sorted(array)

idx = int(K) - 1

print(array[idx])