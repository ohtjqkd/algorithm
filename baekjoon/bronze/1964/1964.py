# input: 3, 1, 19
# output: 22, 5, 590

# 등차수열의 합: n*(초항*2+공차*(n-1))/2
N = int(input())
print(((N+1)*(1+3*N+1)//2)%45678)