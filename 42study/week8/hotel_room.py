from collections import defaultdict

def solution(k, room_number):
    answer = []
    next_room = defaultdict(int)
    for rn in room_number:
        stack = [rn]
        while next_room.get(stack[-1], False):
            stack.append(next_room.get(stack[-1]))

        avail_room = stack[-1]
        answer.append(avail_room)
        while stack:
            next_room[stack.pop()] = avail_room + 1

    return answer


k, room = 10,	[1,3,4,1,3,1]#	[1,3,4,2,5,6]

solution(k, room)