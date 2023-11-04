# 실행속도가 빠른 순서대로

# x = int(input())

def solution(n: int):
    count = 0
    i = 666
    while True:
        #내장 in method
        if '666' in str(i):
            count += 1
        if count == n:
            print(i)
            break
        i += 1
for i in range(1, 500):
    solution(i)


    # 단방향 세개씩
    # str_i = str(i)
    # for j in range(1, len(str_i)-1):
    #     if str_i[j-1] == '6' and str_i[j] == '6' and str_i[j+1] == '6':
    #         count += 1
    #         break
    # if count == n:
    #     print(i)
    #     break
    # i += 1

    # 단방향 탐색
    # for j in str(i):
    #     if j == '6':
    #         six_cnt += 1
    #     else:
    #         six_cnt = 0
    #     if six_cnt == 3:
    #         count += 1
    #         break

    # 양방향 탐색
    # l_six_cnt = 0
    # r_six_cnt = 0
    # str_i = str(i)
    # for j in range(len(str_i)):
    #     if str_i[j] == '6':
    #         l_six_cnt += 1
    #     else:
    #         l_six_cnt = 0
    #     if str_i[-(j+1)] == '6':
    #         r_six_cnt += 1
    #     else:
    #         r_six_cnt = 0
    #     if l_six_cnt == 3 or r_six_cnt == 3:
    #         count += 1
    #         break

    # 666, 1666, 2666, 3666, 4666, 5666, 6660, 6661, 6662, 6663, 6664, 6665, 6666, 6667, 6668,6669
