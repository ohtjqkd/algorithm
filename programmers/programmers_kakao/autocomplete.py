from collections import defaultdict


class Node:
    def __init__(self, char=None, number=0):
        self.value = char
        self.number = number
        self.children = defaultdict(dict)
        self.endpoint = False

    def isEndPoint(self):
        if


class Tree:
    def __init__(self):
        self.root = Node('root')

    def addNode(self, node, char, number):
        node.children[char] = Node(char, number+1)
        # print(f'{char} added in {node.value} Children: {node.children}')

    def addWord(self, word):
        node = self.root
        for i in range(len(word)):
            if not node.children.get(word[i]):
                self.addNode(node, word[i], node.number)
                node = node.children.get(word[i])
            else:
                node = node.children.get(word[i])
        # node.endpoint = True

    def isEnd(self, node):
        node = node
        while len(node.children) != 0:
            if len(node.children) > 1:
                return False
            node = node.children.popitem()[1]
        return True

    def setEndPoint(self):
        node = self.root
        need_visit = [node]
        while need_visit:
            poped = need_visit.pop()
            if self.isEnd(poped):
                poped.endpoint = True
            need_visit.extend(poped.children.values())

            # poped.children.

    def parseNode(self):
        answer = 0
        need_type_count = 0
        node = self.root
        need_visit = [node]
        while need_visit:
            need_type_count += 1
            poped = need_visit.pop()
            if poped.endpoint:
                print(poped.number)
                answer += need_type_count
                need_type_count = 0
            need_visit.extend(poped.children.values())

        return need_type_count

    def getAllNodeInfo(self):
        node = self.root
        need_visit = [node]
        while need_visit:
            poped = need_visit.pop()
            print(f'{poped.value}: {poped.number}, {poped.endpoint}')
            need_visit.extend(poped.children.values())


def solution(words):
    answer = 0
    tree = Tree()
    for w in words:
        tree.addWord(w)
    tree.setEndPoint()
    answer += tree.parseNode()
    tree.getAllNodeInfo()
    return answer


tc = [["go", "gone", "guild"], ["abc", "def", "ghi", "jklm"],
      ["word", "war", "warrior", "world"]]

for c in tc:
    print(solution(c))

# test = {'a': 'aa', 'b': 'bb'}
# print(test.values())
