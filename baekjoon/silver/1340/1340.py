# input
# January 31, 1900 00:47
# output
# 8.228120243531203

month = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12
}

def is_leap_yaer(year: int) -> bool:
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def get_total_time(year: int) -> int:
  return 366 if is_leap_yaer(year) else 365

leap_year = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31 ,30, 31]
non_leap_year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ,30, 31]

for i in range(1, 13):
  leap_year[i] += leap_year[i - 1]
  non_leap_year[i] += non_leap_year[i - 1]

arr = input().split()
y, m, d, h, mm = map(int, [arr[2], month[arr[0]], arr[1][:-1]] + arr[3].split(':'))

total = get_total_time(y) * 24 * 60
now = (((leap_year[m - 1] if is_leap_yaer(y) else non_leap_year[m - 1]) + d - 1) * 24 + h) * 60 + mm
print(now / total * 100)
