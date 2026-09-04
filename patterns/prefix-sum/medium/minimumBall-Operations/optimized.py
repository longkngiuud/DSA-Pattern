def minimumTotalMoves(boxes):

    n = len(boxes)
    ans = [0] * n
    count = 0
    moves = 0

    for i in range(n):

        if boxes[i] == '1':
            count += 1
        ans[i] += moves

        moves += count

    count = 0
    moves = 0
    for i in range(n-1, -1, -1):
        if boxes[i] == '1':
            count += 1
        ans[i] += moves

        moves += count

    return ans
print(minimumTotalMoves("001011"))
