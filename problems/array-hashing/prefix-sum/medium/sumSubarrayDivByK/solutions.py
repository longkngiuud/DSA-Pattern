
from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for i in nums:
            prefix_sum += i

            remainder = prefix_sum % k 
            
            count += prefix_cnt[remainder]
            prefix_cnt[remainder] += 1
        return count
           