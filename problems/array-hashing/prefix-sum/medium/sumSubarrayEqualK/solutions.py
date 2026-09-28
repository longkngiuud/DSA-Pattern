from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0 
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1
        for num in nums:
            prefix_sum += num
            needed = prefix_sum - k
            if needed in prefix_cnt:     
                count += prefix_cnt[needed]
            prefix_cnt[prefix_sum] += 1
            
        return count