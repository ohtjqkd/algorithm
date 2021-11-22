# 파동합치기 가능
# 1초에 1거리만큼 움직임

def solution(wave1, wave2):
    ret = float('inf')
    if len(wave1) > len(wave2):
        wave1, wave2 = wave2, wave1
    def gcd(a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    def divide(wave):
        for i in range(1, len(wave)//2+1):
            start_wave = wave[:i]
            for j in range(i, len(wave), i):
                if wave[j-i:j] != start_wave:
                    break
            else:
                return start_wave
        return wave
    origin_h = len(wave1) * len(wave2) // gcd(len(wave1), len(wave2))
    for i in range(len(wave1)):
        d_wave = wave1[i:]+wave1[:i]
        new_wave1 = [d_wave[i%len(d_wave)] for i in range(origin_h)]
        new_wave2 = [wave2[i%len(wave2)] for i in range(origin_h)]
        final_wave = []
        for j in range(origin_h):
            final_wave.append(new_wave1[j]+new_wave2[j])
        divided_wave = divide(final_wave)
        if len(divided_wave) == 1:
            return 0
        else:
            ret = min(ret, sum(map(lambda x: x**2, divided_wave)))
    return ret


tc = [
    [[1,2,2,1,1,2],[-2,-1],2],
    [[2,-1,3],[-1,-1],9],
    [[0,1,1,1,1,1],[0,0,1,0,0,0],0],
    [[2,0,1,1,1,0],[0,0,-1],1]
]

for t in tc:
    print("expected", t[2])
    print("my answer", solution(t[0], t[1]))