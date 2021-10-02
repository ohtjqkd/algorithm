board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]

def solution(board):
    answer = 0
    n = len(board)
    while True:
        result = searchBlock(board, n)
        if not result:
            break
        answer += result
    print(board)
    return answer

def getArea(blockNum, loc, board, visited, n, areaLoc, locations):
    locations.append(loc)
    visited[loc[0]][loc[1]] = 1
    result = []
    areaLoc[0], areaLoc[1], areaLoc[2], areaLoc[3] = min(areaLoc[0], loc[0]), min(areaLoc[1], loc[1]), max(areaLoc[2], loc[0]), max(areaLoc[3], loc[1])
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    for i in range(4):
        xx, yy = loc[0] + dx[i], loc[1] + dy[i]
        if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0 and board[xx][yy] == blockNum:
            getArea(blockNum, (xx, yy), board, visited, n, areaLoc, locations)

def searchBlock(board, n):
    ret = 0
    visitedBlock = dict()
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and visitedBlock.get(board[i][j]) == None:
                visited = [[0 for _ in range(n)] for _ in range(n)]
                areaLoc = [i, j, i, j]
                locations = []
                getArea(board[i][j], (i, j), board, visited, n, areaLoc, locations)
                if isRemovable(areaLoc, board, board[i][j]):
                    ret += 1
                    for loc in locations:
                        board[loc[0]][loc[1]] = 0

                visitedBlock[board[i][j]] = 1
    return ret

def isRemovable(areaLoc, board, blockNum):
    maxX, minX, minY, maxY = areaLoc[2], areaLoc[0], areaLoc[1], areaLoc[3]
    for i in range(maxX, minX-1, -1):
        for j in range(minY, maxY+1):
            if board[i][j] == 0:
                for k in range(i):
                    if board[k][j] != 0:
                        return False
            elif board[i][j] != blockNum:
                return False
    return True
print(solution(board))