n = int(input())

for i in range(2*n-1):
    string = ''
    if i < n:
        empty_idx = i
    else:
        empty_idx = 2*n-i-2
    for j in range(empty_idx):
        string += ' '
    for j in range(2*n-1-2*empty_idx):
        string += '*'

    print(string)
# for i in range(n-2, -1, -1):
#     string = ''
#     for j in range(n):
#         if i <= j and j < n-i:
#             string += '*'
#         else:
#             string += ' '
#     print(string)
