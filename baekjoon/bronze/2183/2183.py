# input
# 3 BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
# output
# B

I = input().split()
N = int(I[0])
S = I[1]

def init_board():
  return [0] * N

def get_index(c):
  return ord(c) - ord('A')

def judge_game(score_board, idx):
  if score_board[idx] == 4:
    for j in range(N):
      if j == idx:
        continue
      if score_board[j] > 2:
        break
    else:
      return True
  elif score_board[idx] == 5:
    return True
  return False

def judge_set(game_board, idx):
  if game_board[idx] >= 6:
    another_player_winner_cnt = 0
    for j in range(N):
      if j == idx:
        continue
      if game_board[idx] - game_board[j] < 2:
        break
      another_player_winner_cnt += game_board[j]
    else:
      if another_player_winner_cnt == 0:
        return True, 2
      else:
        return True, 1
  return False, 0
  
  

score_board = init_board()
game_board = init_board()
set_board = init_board()
for i in range(len(S)):
  idx = get_index(S[i])
  score_board[idx] += 1
  if judge_game(score_board, idx):
    game_board[idx] += 1
    score_board = init_board()
    is_game, s = judge_set(game_board, idx)
    if is_game:
      game_board = init_board()
      set_board[idx] += s
      if set_board[idx] >= 3:
        print(chr(ord('A') + idx))
        break