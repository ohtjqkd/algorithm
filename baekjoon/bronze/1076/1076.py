colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
col_dic = dict(list(zip(colors, range(len(colors)))))

first = input()
second = input()
third = input()

print((col_dic.get(first)*10+col_dic.get(second))*(10**col_dic.get(third)))


# input

# yellow
# violet
# red