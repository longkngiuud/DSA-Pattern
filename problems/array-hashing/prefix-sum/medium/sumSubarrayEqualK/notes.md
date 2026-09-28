1. Main Idea

We want:

subarray_sum = k

Using prefix sums:

current_prefix - previous_prefix = k

Therefore:

previous_prefix = current_prefix - k

So for every current prefix sum, find how many times:

prefix_sum - k

has appeared before.

2. Core Code
   from collections import defaultdict

class Solution:
def subarraySum(self, nums, k):
prefix_sum = 0
count = 0

        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k
            count += prefix_cnt[needed]

            prefix_cnt[prefix_sum] += 1

        return count

3. Why {0: 1}?
   prefix_cnt[0] = 1

Represents a prefix sum of 0 before the array starts.

This lets us count subarrays that begin at index 0.

Example:

nums = [3], k = 3

prefix_sum = 3
needed = 3 - 3 = 0

prefix_cnt[0] = 1
→ found [3] 4. Why Frequency?

We store:

prefix sum → frequency

because the same prefix sum can appear multiple times.

count += prefix_cnt[needed]

Each previous matching prefix creates one valid subarray.

5. Pattern to Memorize
   BUILD → FIND → COUNT → STORE

prefix_sum += num
needed = prefix_sum - k
count += prefix_cnt[needed]
prefix_cnt[prefix_sum] += 1 6. Common Mistakes

❌ Only check:

prefix_sum == k

This misses subarrays starting later.

❌ Use remainder:

prefix_sum % k

That's the key idea for LC 974, not LC 560.

❌ Store only one index.

LC 560 needs:

prefix sum → frequency 7. Complexity
Time: O(n)
Space: O(n)
One Sentence to Remember

For every current prefix sum, find current_prefix - k; every previous occurrence represents one valid subarray.
![alt text](image.png)
![Step 4](image-1.png)
![Step 5](image-2.png)
![Step 6](image-3.png)
![Step 7](image-4.png)
![Step 8](image-5.png)
![Step 9](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
