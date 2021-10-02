play_time, adv_time, logs = "02:03:55", "00:14:15", [
    "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
# play_time, adv_time, logs = "99:59:59", "00:00:30", [
# "00:00:01-00:00:02", "00:00:02-00:00:31", "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]


def secCalc(h, m, s):
    h, m, s = int(h), int(m), int(s)
    return h*3600+m*60+s


def convertToString(sTime):
    result = []
    hour = sTime//3600
    sTime %= 3600
    mins = sTime//60
    sTime %= 60
    seconds = sTime

    for t in [hour, mins, seconds]:
        if t < 10:
            t = "0"+str(t)
        else:
            t = str(t)
        result.append(t)
    return ":".join(result)


def solution(play_time, adv_time, logs):
    a_h, a_m, a_s = map(int, adv_time.split(":"))
    adv_time_s = secCalc(a_h, a_m, a_s)
    p_h, p_m, p_s = map(int, play_time.split(":"))
    play_time_s = secCalc(p_h, p_m, p_s)
    dp = [0 for _ in range(play_time_s+1)]
    # print(play_time_s)
    for log in logs:
        start, end = log.split("-")
        s_h, s_m, s_s = map(int, start.split(":"))
        e_h, e_m, e_s = map(int, end.split(":"))
        startValue = secCalc(s_h, s_m, s_s)
        endValue = secCalc(e_h, e_m, e_s)
        dp[startValue] += 1
        dp[endValue] -= 1
    for i in range(1, len(dp)):
        dp[i] = dp[i-1] + dp[i]

    nowTime = sum(dp[:adv_time_s])
    maxTime, maxTimeIdx = 0, 0
    for i in range(adv_time_s, play_time_s):
        if nowTime > maxTime:
            maxTime = nowTime
            maxTimeIdx = i
        nowTime -= dp[i-adv_time_s]
        nowTime += dp[i]
    return convertToString(maxTimeIdx-adv_time_s)

# 정답코드
# def solution(play_time, adv_time, logs):
#     play_time = str_to_int(play_time)        # 1
#     adv_time = str_to_int(adv_time)
#     all_time = [0 for i in range(play_time + 1)]

#     for l in logs:                           # 2
#         start, end = l.split('-')
#         start = str_to_int(start)
#         end = str_to_int(end)
#         all_time[start] += 1
#         all_time[end] -= 1

#     for i in range(1, len(all_time)):       # 3
#         all_time[i] = all_time[i] + all_time[i - 1]

#     for i in range(1, len(all_time)):       # 4
#         all_time[i] = all_time[i] + all_time[i - 1]

#     most_view = 0                           # 5
#     max_time = 0
#     for i in range(adv_time - 1, play_time):
#         if i >= adv_time:
#             if most_view < all_time[i] - all_time[i - adv_time]:
#                 most_view = all_time[i] - all_time[i - adv_time]
#                 max_time = i - adv_time + 1
#         else:
#             if most_view < all_time[i]:
#                 most_view = all_time[i]
#                 max_time = i - adv_time + 1
#     print(max_time, most_view)
#     return int_to_str(max_time)


# def str_to_int(time):
#     h, m, s = time.split(':')
#     return int(h) * 3600 + int(m) * 60 + int(s)


# def int_to_str(time):
#     h = time // 3600
#     h = '0' + str(h) if h < 10 else str(h)
#     time = time % 3600
#     m = time // 60
#     m = '0' + str(m) if m < 10 else str(m)
#     time = time % 60
#     s = '0' + str(time) if time < 10 else str(time)
#     return h + ':' + m + ':' + s

# def solution(play_time, adv_time, logs):
#     if play_time == adv_time:
#         return "00:00:00"
#     a_h, a_m, a_s = map(int, adv_time.split(":"))
#     adv_time_s = secCalc(a_h, a_m, a_s)
#     p_h, p_m, p_s = map(int, play_time.split(":"))
#     play_time_s = secCalc(p_h, p_m, p_s)
#     dp = [0 for _ in range(play_time_s+1)]
#     for log in logs:
#         start, end = log.split("-")
#         s_h, s_m, s_s = map(int, start.split(":"))
#         e_h, e_m, e_s = map(int, end.split(":"))
#         startValue = secCalc(s_h, s_m, s_s)
#         endValue = secCalc(e_h, e_m, e_s)
#         for i in range(startValue, endValue):
#             dp[i] += 1
#     maxTime, maxTimeIdx = 0, 0
#     nowTime = sum(dp[0:adv_time_s+1])
#     for i in range(adv_time_s+1, play_time_s):
#         nowTime -= dp[i-adv_time_s-1]
#         nowTime += dp[i]
#         if nowTime > maxTime:
#             maxTime = nowTime
#             maxTimeIdx = i
#     # print(maxTime)
#     return convertToString(maxTimeIdx-adv_time_s+1)

# def to_seconds(time_):
#     return sum([int(x)*y for x, y in zip(time_.split(':'), [3600, 60, 1])])


# def to_time(seconds):
#     m, s = divmod(seconds, 60)
#     h, m = divmod(m, 60)
#     return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


# def solution(play_time, adv_time, logs):
#     play_time_sec, adv_time_sec = to_seconds(play_time), to_seconds(adv_time)
#     logs_start_sec = []
#     logs_end_sec = []
#     for log in logs:
#         start, end = map(to_seconds, log.split('-'))
#         logs_start_sec.append(start)
#         logs_end_sec.append(end)
#     total_time = [0]*(play_time_sec+1)
#     for i in range(len(logs)):
#         total_time[logs_start_sec[i]] += 1
#         total_time[logs_end_sec[i]] -= 1
#     for i in range(1, play_time_sec):
#         total_time[i] += total_time[i - 1]
#     for i in range(1, play_time_sec):
#         total_time[i] += total_time[i - 1]
#     answer = [0, total_time[adv_time_sec-1]]
#     for i in range(play_time_sec-adv_time_sec):
#         tmp = total_time[i+adv_time_sec] - total_time[i-1]
#         if answer[1] < tmp:
#             answer = [i, tmp]

#     return to_time(answer[0])


print(solution(play_time, adv_time, logs))
