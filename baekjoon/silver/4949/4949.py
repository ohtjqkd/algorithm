import sys
input = sys.stdin.readline
arr = []
while True:
    string = input()
    if string.rstrip() == '.':
        break
    stack = []
    result = 'yes'
    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        else:
            if c == ')':
                if len(stack) == 0 or stack.pop() == '[':
                    result = 'no'
                    break
            elif c == ']':
                if len(stack) == 0 or stack.pop() == '(':
                    result = 'no'
                    break
    if len(stack) != 0:
        result = 'no'
    print(result)
