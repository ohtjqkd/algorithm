n = int(input())

for i in range(n):
    string = ''
    for _ in range(i+1):
        string += '*'
    print(string)

for i in range(n-2, -1, -1):
    string = ''
    for _ in range(i+1):
        string += '*'
    print(string)
