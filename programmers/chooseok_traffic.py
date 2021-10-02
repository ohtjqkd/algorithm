import datetime
test_case = [["2016-09-15 00:00:00.000 3s"], ["2016-09-15 23:59:59.999 0.001s"], ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"], ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"], ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
                                                                                                                                                                                                                  "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"], ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]]

datetime.time().


def solution(lines):
    answer = 0
    times = []
    for line in lines:
        line = line[:-1]
        if len(line) == 25:
            line += ".0"
        line = line.replace(":", " ").replace(".", " ")
        line = line.split(" ")
        line = line[1:]
        h, m, s, ms, ds, dms = map(int, line)

        end = ms + s * 1000 + m * 1000 * 60 + h * 1000 * 60 * 60
        start = end - ds * 1000 - dms + 1
        times.append((start, end))
    for i in range(len(times)):
        s1, e1 = times[i]
        pro = 1
        for j in range(len(times)):
            if i == j:
                continue
            s2, e2 = times[j]
            if e1 > e2 or e1+999 < s2:
                pass
            else:
                pro += 1
        answer = max(pro, answer)
    return answer
