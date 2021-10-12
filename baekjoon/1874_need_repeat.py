##error - 출력초과
n = int(input())
arr = []
stack1 = [i for i in range(n, 0, -1)]
stack2 = [0]
idx = 0
result = []
boolean = True
for i in range(n):
    number = int(input())
    arr.append(number)
    if number == n:
        idx = i
arr1 = sorted(arr[idx:], reverse=True)
if arr1 != arr[idx:]:
    # if not boolean:
    print("NO")
else:
    for number in arr:
        while boolean:
            print(stack1, stack2)
            if stack2[-1] == number:
                result.append("-")
                stack2.pop()
                break
            elif len(stack1) != 0:
                stack2.append(stack1.pop())
                result.append("+")
            else:
                boolean = False
                break
        if not boolean:
            break
    for r in result:
        print(r)

nico = {age: 44}
print(nico["age"])
