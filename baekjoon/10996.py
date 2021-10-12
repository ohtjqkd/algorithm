n = int(input())
if n == 1:
    print("*")
else:
    for i in range(2*n):
        string = ''
        if i % 2 == 0:
            for j in range(n):
                if j % 2 == 0:
                    string += "*"
                else:
                    string += " "
        else:
            for j in range(n):
                if j % 2 == 0:
                    string += " "
                else:
                    string += "*"
        print(string.rstrip())
