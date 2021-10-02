# 조건
#3 < len(id) < 16
# "-", "_", "." are only available special characters
# but "." can't be used at the start or the end of id

# rules
# 1. converting new_id from uppercase to lowercase
# 2. removing all characters except for lowercases, number, "-", "_", "."
# 3. if "." is repeated more than twice at anysection, it have to be converted to just "."
# 4. if "." is located at the start or the end of id, it have to be removed
# 5. if id is "", where the length of id is zero, id is "a"
# 6. if the length of id is more than 16, remove the text located from 16 to end
#   after removing, if "." is lcoated at the end of id, remove it
# 7. if the length of id less than 2, put the last character at the end of id until the length of id get to be 3

import sys
import re
input = sys.stdin.readline
comp = re.compile('(?<=\.)\.*')
available = {
    ".": True,
    "-": True,
    "_": True
}


def isAvailable(char):
    asc = ord(char)
    if 48 <= asc <= 57:  # 숫자
        return True
    if 97 <= asc <= 122:  # 소문자
        return True
    return False


test = ["a", "b", "c"]
test = str(test)
print(test)

while True:
    # step 1 - in backjoon
    new_id = input().strip()
    if not new_id:
        break
    new_id = list(new_id.lower())

    # step 1 - in programmers
    # new_id = new_id.lower()

    # step 2
    new_id = [new_id[i] for i in range(len(new_id)) if available.get(
        new_id[i]) or isAvailable(new_id[i])]
    # step 3
    idx = 1
    while len(new_id) >= 2:
        if new_id[idx-1] == "." and new_id[idx] == ".":
            new_id = new_id[:idx] + new_id[idx+1:]
        else:
            idx += 1
        if idx > len(new_id)-1:
            break
    # step 4
    if new_id and new_id[0] == ".":
        new_id = new_id[1:]
    elif new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    # step 5
    if not new_id:
        new_id = "a"
    # step 6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    # step 7
    if len(new_id) < 3:
        lastChar = new_id[-1]
        while len(new_id) < 3:
            new_id += lastChar
    print(new_id)
