n = int(input())
numbers = list(map(int, input().split()))
operands = list(map(int, input().split()))


def cal(arr, operands, v, n):
    result = []
    if sum(operands) == 0:
        # print('return', v)
        return [v]
    if operands[0] > 0:
        operands[0] -= 1
        # print(v, '+', arr[n+1])
        result.extend(cal(arr, operands, v+arr[n+1], n+1))
        operands[0] += 1
    if operands[1] > 0:
        operands[1] -= 1
        # print(v, '-', arr[n+1])
        result.extend(cal(arr, operands, v-arr[n+1], n+1))
        operands[1] += 1
    if operands[2] > 0:
        operands[2] -= 1
        # print(v, '*', arr[n+1])
        result.extend(cal(arr, operands, v*arr[n+1], n+1))
        operands[2] += 1
    if operands[3] > 0:
        operands[3] -= 1
        # print(v, '//', arr[n+1])
        if v < 0:
            v = -(-v//arr[n+1])
        else:
            v = v//arr[n+1]
        result.extend(cal(arr, operands, v, n+1))
        operands[3] += 1
    return result


result = cal(numbers, operands, numbers[0], 0)
print(max(result))
print(min(result))
