N = input()
S = "1"*len(N)
ret = len(N) if int(N) >= int(S) or int(N) == 0 else len(N)-1
# if int(N) >= int(S) or int(N) == 0:
# ret = len(N)
# else:
# ret = len(N)-1
# init = int(N[0])
# ret = 0
# mins = ""
# base = len(N)-1
# for i in range(base+1):
#     mins += "1"
# if len(N) == 1:
#     ret = 1
# else:
#     ret = base+1 if int(mins) <= int(N) else base
print(ret)
