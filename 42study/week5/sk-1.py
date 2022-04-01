# sk-1

goods = input().split(" ")
print(goods)
trie = dict()

def make_trie(str, trie):
    for s in str: