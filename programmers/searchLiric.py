from collections import defaultdict

words = ["go", "gone", "guild"]


def isEnd(parent):
    children = parent.values()
    if len(children) == 0:
        pass

    if parent.get("end"):
        for node in parent.values():
            isEnd(node)

    isEnd(node)


def solution(words):
    answer = 0
    tree = dict()
    for word in words:
        node = tree
        print(word)
        for idx, char in enumerate(word):
            print(idx, char)
            if node.get(char):
                pass
            else:
                node[char] = dict()
            node = node.get(char)
            print(node)
            if idx == len(word)-1:
                node['end'] = True
    print(tree)

    return answer


solution(words)
