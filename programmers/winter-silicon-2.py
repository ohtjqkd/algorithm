# 학점 높을 수록
# 하지만 3.9와 3.7은 다른 기준으로
# 학점의 앞자리가 같으면 거주지역까지의 직서거리가 더 멀 때 순위가 높음
# 학교는 0, 0에 위치
# 학점 앞자리와 거리가 같을 경우 이름이 빠를 수록

def solution(names, homes, grades):
    answer = ['' for _ in range(len(names))]
    li = list(zip(grades, homes, names, range(len(names))))
    li.sort(key=lambda x: (-int(x[0]), -(x[1][0]**2+x[1][1]**2), x[2]))
    for idx, l in enumerate(li):
        answer[l[3]] = idx+1
    return answer


tc = [
    [["azad","andy","louis","will","edward"],[[3,4],[-1,5],[-4,4],[3,4],[-5,0]],[4.19, 3.77, 4.41, 3.65, 3.58],[2,3,1,5,4]],
    [["clanguage","csharp","java","python"],[[3,-3],[-2,7],[-1,-1],[5,4]],[1.27, 4.31, 4.26, 3.99],[4,1,2,3]],
    [["zzzzzzzzzz"],[[9999,-9999]],[1.0],[1]]
]

for t in tc:
    print("expected answer", t[3])
    print("my answer", solution(t[0], t[1], t[2]))