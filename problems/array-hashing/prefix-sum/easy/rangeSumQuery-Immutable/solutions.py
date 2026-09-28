class NumArray:

    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)

        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


def prefix_sum(nums, queries):

    obj = NumArray(nums)

    res = [None]

    for l, r in queries:
        res.append(obj.sumRange(l, r))

    return res


if __name__ == '__main__':

    nums = [-2, 0, 3, -5, 2, -1]

    queries = [
        [0, 2],
        [2, 5],
        [0, 5]
    ]

    print(prefix_sum(nums, queries))