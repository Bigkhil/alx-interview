#!/usr/bin/python3
"""
check if all the boxes are unlocked or not
"""


def canUnlockAll(boxes):
    """this function should return if the boxes can be opened or not"""
    if len(boxes) == 0:
        return False

    vis = [0] * len(boxes)
    stack = [0]
    vis[0] = 1
    cntr = 1

    while stack:
        st = stack.pop()
        for neg in boxes[st]:
            if neg < len(boxes) and not vis[neg]:
                vis[neg] = 1
                cntr += 1
                stack.append(neg)

    return cntr == len(boxes)
