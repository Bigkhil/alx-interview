#!/usr/bin/python3
def canUnlockAll(boxes):
    """this function should return if the boxes can be opened or not"""
    vis = [0] * len(boxes)
    cntr = 1
    def dfs(st):
        """this is depth first search algorithm"""
        nonlocal cntr
        vis[st] = 1
        for neg in boxes[st]:
            if (neg < len(boxes) and not vis[neg]):
                cntr += 1
                dfs(neg)
        return cntr
    if dfs(0) == len(boxes):
        return True
    return False
