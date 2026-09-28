# Prefix Sum + Remainder Map

## LeetCode 974 — Subarray Sums Divisible by K

---

## 1. What is the problem asking?

Given:

```python
nums = [...]
k = ...
```

Count how many **contiguous subarrays** have a sum that is divisible by `k`.

Example:

```text
nums = [1, 2, 3]
k = 3
```

Valid subarrays:

```text
[1, 2]       → 3  → divisible by 3
[3]          → 3  → divisible by 3
[1, 2, 3]    → 6  → divisible by 3
```

Answer:

```text
3
```

---

# 2. Brute Force Idea

Try every possible subarray.

```python
count = 0

for i in range(len(nums)):
    total = 0

    for j in range(i, len(nums)):
        total += nums[j]

        if total % k == 0:
            count += 1

return count
```

### Complexity

```text
Time:  O(n²)
Space: O(1)
```

Why `O(n²)`?

Because we use two loops to consider every possible starting and ending position.

---

# 3. Why Prefix Sum?

Instead of repeatedly calculating subarray sums, we can use prefix sums.

Suppose:

```text
nums = [1, 2, 3]
```

Prefix sums:

```text
Before array → 0
After 1      → 1
After 2      → 3
After 3      → 6
```

We can find a subarray sum using:

```text
subarray sum = prefix_B - prefix_A
```

Example:

```text
prefix_A = 1
prefix_B = 6

6 - 1 = 5
```

This represents the sum of the elements between those two prefix positions:

```text
[2, 3]

2 + 3 = 5
```

---

# 4. The Important Math

We want:

```text
prefix_B - prefix_A
```

to be divisible by `k`.

That means:

```text
(prefix_B - prefix_A) % k == 0
```

This happens when:

```text
prefix_B % k == prefix_A % k
```

In other words:

> If two prefix sums have the SAME remainder when divided by `k`, their difference is guaranteed to be divisible by `k`.

---

# 5. Why Does the Same Remainder Work?

Suppose:

```text
prefix_A % k = r
prefix_B % k = r
```

We can write:

```text
prefix_A = a*k + r
prefix_B = b*k + r
```

Subtract:

```text
prefix_B - prefix_A
= (b*k + r) - (a*k + r)
```

The `r` cancels:

```text
= b*k - a*k
= (b-a)*k
```

Therefore:

```text
prefix_B - prefix_A
```

is divisible by `k`.

### The rule

```text
SAME remainder
      ↓
prefix_B - prefix_A is divisible by k
      ↓
subarray between them is valid
```

But:

```text
DIFFERENT remainder
      ↓
NO guarantee
```

---

# 6. Example: k = 5

```text
nums = [1, 2, 3]
k = 5
```

Prefix sums:

```text
0
1
3
6
```

Remainders:

```text
0 % 5 = 0
1 % 5 = 1
3 % 5 = 3
6 % 5 = 1
```

Notice:

```text
1 → remainder 1
6 → remainder 1
```

They have the same remainder.

Therefore:

```text
6 - 1 = 5
```

And:

```text
5 % 5 = 0
```

The corresponding subarray is:

```text
[2, 3]
```

because:

```text
2 + 3 = 5
```

So `[2,3]` is a valid subarray.

---

# 7. Example: k = 4

```text
nums = [1, 2, 3]
k = 4
```

Prefix sums:

```text
0
1
3
6
```

Remainders:

```text
0 % 4 = 0
1 % 4 = 1
3 % 4 = 3
6 % 4 = 2
```

We have:

```text
0, 1, 3, 2
```

There are NO repeated remainders.

Therefore, there is no pair of prefix sums whose difference is guaranteed to be divisible by `4`.

Indeed:

```text
[1]       → 1
[2]       → 2
[3]       → 3
[1,2]     → 3
[2,3]     → 5
[1,2,3]   → 6
```

None are divisible by `4`.

Answer:

```text
0
```

---

# 8. The Hash Map

We use:

```python
prefix_cnt = {0: 1}
```

The map stores:

```text
remainder → how many times we have seen it
```

Example:

```python
prefix_cnt = {
    0: 1,
    1: 3,
    2: 2
}
```

Means:

```text
remainder 0 → seen 1 time
remainder 1 → seen 3 times
remainder 2 → seen 2 times
```

---

# 9. Why `{0: 1}`?

This is extremely important.

```python
prefix_cnt = {0: 1}
```

means:

> Before processing the array, we have already seen a prefix sum of `0` once.

Think of it as a **virtual prefix sum before the array starts**:

```text
             array
               ↓
       [ 1, 2, 3, ... ]

       ↑
   prefix sum = 0
```

It allows us to count subarrays that start at index `0`.

---

# 10. Example of Why `{0: 1}` Is Needed

```text
nums = [5]
k = 5
```

Before processing:

```python
prefix_cnt = {0: 1}
```

Process `5`:

```text
prefix_sum = 5
remainder = 5 % 5
           = 0
```

We already have:

```text
prefix_cnt[0] = 1
```

Therefore:

```python
res += prefix_cnt[0]
```

gives:

```text
res = 1
```

The valid subarray is:

```text
[5]
```

Without `{0: 1}`, we would not have a previous remainder `0` to pair with the current remainder `0`.

---

# 11. What Does `res += prefix_cnt[remainder]` Mean?

This is the HEART of the algorithm.

```python
res += prefix_cnt[remainder]
```

It means:

> "How many previous prefix sums have the SAME remainder as my current prefix sum?"

Every one of those previous prefix sums creates **one new valid subarray**.

Therefore:

```text
number of previous matching remainders
                    ↓
          number of new valid subarrays
```

---

# 12. Why Does Every Matching Remainder Create One Subarray?

Suppose the current prefix sum is:

```text
prefix_B
```

and we previously saw three prefix sums with the same remainder:

```text
prefix_A1
prefix_A2
prefix_A3
```

Because they all have the same remainder:

```text
prefix_B - prefix_A1 → divisible by k
prefix_B - prefix_A2 → divisible by k
prefix_B - prefix_A3 → divisible by k
```

Therefore, we get **3 different valid subarrays**.

So:

```python
prefix_cnt[remainder] = 3
```

means:

```text
3 previous prefix positions
          ↓
3 possible valid subarrays ending at current position
```

Therefore:

```python
res += 3
```

---

# 13. Very Important Mental Model

Do NOT think:

```text
prefix_cnt[remainder]
=
number of subarrays
```

Instead think:

```text
prefix_cnt[remainder]
=
number of previous PREFIX SUMS
with this remainder
```

Then:

```text
Each previous matching prefix sum
              ↓
creates one valid subarray
              ↓
so add that frequency to res
```

---

# 14. What Does `prefix_cnt[remainder] += 1` Mean?

After using the previous occurrences, we record the current remainder.

```python
prefix_cnt[remainder] += 1
```

Means:

> "I have now seen this remainder one more time."

Example:

```text
prefix_cnt = {0: 1, 4: 2}
```

Current:

```text
remainder = 4
```

First:

```python
res += prefix_cnt[4]
```

Use the old frequency:

```text
prefix_cnt[4] = 2
```

So we found:

```text
2 new valid subarrays
```

Then:

```python
prefix_cnt[4] += 1
```

Now:

```text
prefix_cnt[4] = 3
```

We are recording the current prefix sum so that it can be used by a future prefix sum.

---

# 15. Why Is the Order Important?

We do:

```python
res += prefix_cnt[remainder]
prefix_cnt[remainder] += 1
```

NOT the other way around.

Why?

Because the current prefix sum should not pair with **itself**.

We first ask:

```text
How many previous matching prefix sums exist?
```

Then we record:

```text
The current prefix sum has now appeared.
```

---

# 16. Complete Optimized Code

```python
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0

        prefix_cnt = {0: 1}

        for i in nums:
            prefix_sum += i

            remainder = prefix_sum % k

            res += prefix_cnt.get(remainder, 0)

            prefix_cnt[remainder] = prefix_cnt.get(remainder, 0) + 1

        return res
```

You can also use `defaultdict(int)`:

```python
from collections import defaultdict

prefix_cnt = defaultdict(int)
prefix_cnt[0] = 1
```

Then:

```python
res += prefix_cnt[remainder]
prefix_cnt[remainder] += 1
```

works directly.

---

# 17. Full Execution Example

```text
nums = [1, 2, 3]
k = 3
```

Start:

```text
prefix_sum = 0
res = 0
prefix_cnt = {0: 1}
```

### Process 1

```text
prefix_sum = 1
remainder = 1
```

Previous remainder `1`:

```text
0 times
```

So:

```text
res = 0
```

Record it:

```text
prefix_cnt = {0: 1, 1: 1}
```

---

### Process 2

```text
prefix_sum = 3
remainder = 0
```

Previous remainder `0`:

```text
1 time
```

So:

```text
res = 1
```

This represents:

```text
[1,2]
```

Record current remainder:

```text
prefix_cnt = {0: 2, 1: 1}
```

---

### Process 3

```text
prefix_sum = 6
remainder = 0
```

Previous remainder `0`:

```text
2 times
```

Therefore:

```text
res += 2
```

```text
res = 3
```

The two new valid subarrays are:

```text
[3]
[1,2,3]
```

Final:

```text
res = 3
```

---

# 18. Why Directly Checking `prefix_sum % k == 0` Is Not Enough

You might think:

```python
if prefix_sum % k == 0:
    res += 1
```

This only finds subarrays that start at index `0`.

Example:

```text
nums = [1, 3]
k = 3
```

Prefix sums:

```text
0
1
4
```

Remainders:

```text
0
1
1
```

Neither `1` nor `4` is divisible by `3`.

But:

```text
[3] → 3
```

IS divisible by `3`.

Why?

Because:

```text
4 - 1 = 3
```

And:

```text
4 % 3 = 1
1 % 3 = 1
```

Same remainder!

So the remainder map finds `[3]`, while checking only:

```python
prefix_sum % k == 0
```

would miss it.

---

# 19. The Difference Between These Two Problems

## Continuous Subarray Sum — LeetCode 523

Usually asks:

> Does at least one valid subarray exist?

We need to know **WHERE** a remainder first appeared.

Therefore:

```python
remainder = {0: -1}
```

Map:

```text
remainder → earliest index
```

---

## Subarray Sums Divisible by K — LeetCode 974

Asks:

> How many valid subarrays exist?

We need to know **HOW MANY TIMES** each remainder appeared.

Therefore:

```python
prefix_cnt = {0: 1}
```

Map:

```text
remainder → frequency
```

### Remember:

```text
523:
remainder → index
        ↓
"WHERE did I see this?"

974:
remainder → count
        ↓
"HOW MANY times did I see this?"
```

---

# 20. Common Mistakes

### Mistake 1 — Thinking only divisible prefix sums matter

Wrong:

```python
if prefix_sum % k == 0:
    res += 1
```

This misses subarrays that start somewhere other than index `0`.

Correct idea:

```text
Same remainder between two prefix sums
→ their difference is divisible by k
```

---

### Mistake 2 — Thinking different remainders work

Wrong:

```text
prefix_A % k != prefix_B % k
```

does NOT guarantee divisibility.

Example:

```text
6 % 4 = 2
1 % 4 = 1
```

Different remainders.

```text
6 - 1 = 5
```

But:

```text
5 % 4 != 0
```

---

### Mistake 3 — Forgetting `{0: 1}`

```python
prefix_cnt = {0: 1}
```

represents the virtual prefix sum:

```text
before the array = 0
```

It allows subarrays starting at index `0` to be counted.

---

### Mistake 4 — Updating the count before using it

Prefer:

```python
res += prefix_cnt[remainder]
prefix_cnt[remainder] += 1
```

First use previous occurrences.

Then record the current occurrence.

---

# 21. Complexity

Optimized solution:

```text
Time:  O(n)
Space: O(k)
```

More precisely, the number of distinct remainders is at most `k` (assuming the usual positive `k` formulation).

Why `O(n)` time?

We process every number once.

Why `O(k)` space?

There can be at most `k` different remainders:

```text
0, 1, 2, ..., k-1
```

---

# 22. The Pattern to Memorize

When you see:

> **Count subarrays whose sum is divisible by `k`**

Think:

```text
1. Prefix sum
       ↓
2. prefix_sum % k
       ↓
3. Store remainder frequencies
       ↓
4. Same remainder?
       ↓
5. Every previous occurrence creates
   one valid subarray
       ↓
6. Add its frequency to answer
```

Code pattern:

```python
prefix_sum = 0
res = 0

prefix_cnt = {0: 1}

for num in nums:
    prefix_sum += num

    remainder = prefix_sum % k

    res += prefix_cnt[remainder]

    prefix_cnt[remainder] += 1

return res
```

---

# 23. One Sentence to Remember

> **Same remainder means the difference between two prefix sums is divisible by `k`, and every previous occurrence of that remainder gives me one new valid subarray.**

This is the core idea of **Prefix Sum + Remainder Frequency Map**.
