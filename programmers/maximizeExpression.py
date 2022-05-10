# li = []
# s = 0
# for i, v in enumerate(expression):
#     if v in ["*", "+", "-"]:
#         li.append(expression[s:i])
#         li.append(v)
#         s = i + 1
#     else:
#         li.append(expression[s:])
#     stacks = [deque(li), deque()]

# for op in opes:
#     if op not in expression:
#         ops.remove(op)
#     primarity = permutations(ops)

from collections import deque

def to_postfix(expression, primirity):
    order = {oper: i for i, oper in enumerate(primirity)}
    postfix = deque([])
    start_idx = 0
    operand = []
    while start_idx < len(expression):
        curr = expression[start_idx]
        if order.get(curr, False):
            if not operand or order.get(operand[-1]) < order.get(curr):
                operand.append(curr)
            else:
                postfix.append(operand.pop())
                operand.append(curr)
                print(postfix)
            start_idx += 1
        else:
            str_len = 0
            while start_idx + str_len < len(expression) and expression[start_idx + str_len] not in order:
                str_len += 1
            if str_len == 0:
                start_idx += 1
                continue
            postfix.append(expression[start_idx:start_idx + str_len])
            start_idx += str_len
        print(curr, start_idx)
        print(operand)
        print(postfix)
    return postfix

def solution(expression):
    operand = {'*', '+', '-'}
    primarity = {
        '*': 1,
        '+': 2,
        '-': 3
    }
    print(to_postfix(expression, primarity))
    # while start_idx < len(expression):
    #     if expression[start_idx] in operand:
    #         start_idx += 1
    #         exp_li.append(expression[start_idx])
    #     else:
    #         str_len = 0
    #         while expression[start_idx + str_len] not in operand:
    #             str_len += 1
    #         exp_li.append(expression[start_idx:start_idx + str_len])
    #         start_idx += str_len
    # print(exp_li)


expression = "100-200*300-500+20"
solution(expression)