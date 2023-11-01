# input
# 13:52:30
# 14:00:00
# output
# 00:07:30

def str2time(str_arr):
    time = 0
    for i in range(len(str_arr)):
        time += int(str_arr[i])*60**(2-i)
    return time
def time2str(time):
    str_arr = []
    for i in range(3):
        n = time // 60**(2-i)
        if n < 10:
            n = "0" + str(n)
        else:
            n = str(n)
        str_arr.append(n)
        time %= 60**(2-i)
    return ':'.join(str_arr)
now_time = str2time(input().split(":"))
start_time = str2time(input().split(":"))

if start_time < now_time:
    start_time += (3600*24)
print(time2str(start_time-now_time))