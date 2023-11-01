x, y, w, h = map(int, input().split())
r_d = min(x, abs(w-x))
c_d = min(y, abs(h-y))
print(min(r_d, c_d))
