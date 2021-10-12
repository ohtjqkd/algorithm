n = int(input())

bricks = [list(map(int, input().split(' ')+[i]) for i in range(n)]
print(bricks)

def dfs(bricks, prev_area, prev_weight, height):
    if len(bricks) == 0:
        return height, []
    ret = []
    curr_node = 0
    ret = max([dfs(b[:i]+b[i+1:], b[0], b[1],height+b[2]) for b in bricks if b[0] < prev_area and b[1] < prev_weight], key=lambda x: x[0])
    return 
    for i, b in enumerate(bricks):
        if b[0] < prev_area and b[1] < prev_weight:
            dfs(b[:i]+b[i+1:], b[0], b[1], height+b[2])