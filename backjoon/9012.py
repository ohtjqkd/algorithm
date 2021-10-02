for _ in range(int(input())):
    arr = list(input())
    stack = []
    # print(len(arr))
    result = 'YES'
    for i in range(len(arr)):
        if arr[i] == ')':
            if len(stack) == 0:
                result = 'NO'
                break
            else:
                stack.pop()
        else:
            stack.append(arr[i])
        # print(stack)
    if len(stack) != 0:
        result = 'NO'
    print(result)
