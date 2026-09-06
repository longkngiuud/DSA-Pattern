def numberOfPoints(nums):

    n = len(nums)
    line = [0] * 102
    points_on_line = 0

    for s, e in nums:
        line[s] += 1
        line[e + 1] -= 1

    for i in range(1, 102):
        line[i] += line[i - 1]
        if line[i] != 0:
            points_on_line += 1

    return points_on_line


if __name__ == '__main__':
    nums = [
        [1, 3],
        [2, 5]
    ]
    print(numberOfPoints(nums))
