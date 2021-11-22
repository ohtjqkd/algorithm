import os, sys

def get_str_list():
    ret = []
    while sys.stdin.readable:
        string = sys.stdin.readline()
        print(string)
        ret.append(string)
    return ret

def print_board(board):
    for b in board:
        print(b)
    print()