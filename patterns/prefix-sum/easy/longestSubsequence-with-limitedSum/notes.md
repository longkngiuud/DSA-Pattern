# Answer Queries

## 1. Problem

Given:

```python
nums = [...]
queries = [...]
```

For each `query`, find the **maximum number of elements** that can be selected from `nums` such that their sum is `<= query`.

Example:

```text
nums = [4, 5, 2, 1]
queries = [3, 10, 21]

Output = [2, 3, 4]
```

---

# 2. Understand the Problem

The important phrase is:

> maximum number of elements

We want to choose as **many elements as possible**, while keeping their total sum `<= query`.

Therefore, we should always try to take the **smallest elements first**.

Example:

```text
nums = [4, 5, 2, 1]
```

Sort:

```text
[1, 2, 4, 5]
```

For `query = 7`:

```text
1          → sum = 1
1 + 2      → sum = 3
1 + 2 + 4  → sum = 7
```

We can take 3 elements.

Adding `5` would give:

```text
1 + 2 + 4 + 5 = 12
```

which is too large.

Answer:

```text
3
```

---

# 3. Brute Force Approach

A simple approach is:

```python
for every query:
    try elements one by one
    calculate the sum
```

But repeatedly calculating the sum is expensive.

For example:

```python
sum(ans)
```

takes `O(n)`.

If we put it inside another loop, we can get approximately:

```text
O(m * n²)
```

where:

- `n = len(nums)`
- `m = len(queries)`

We can do much better.

---

# 4. Key Observation #1 — Sort

Sort `nums`:

```python
nums.sort()
```

Why?

Because we want the **maximum number of elements**.

The smallest numbers give us the best chance of fitting more elements within the query.

Example:

```text
Original:
[4, 5, 2, 1]

Sorted:
[1, 2, 4, 5]
```

Now the first `k` elements always represent the cheapest way to select `k` elements.

For example:

```text
1 element → [1]
2 elements → [1, 2]
3 elements → [1, 2, 4]
4 elements → [1, 2, 4, 5]
```

Therefore, after sorting, we only need to consider **prefixes** of the array.

---

# 5. Key Observation #2 — Prefix Sum

Instead of repeatedly calculating:

```python
sum(nums[:i])
```

we precompute the sums.

For:

```text
nums = [1, 2, 4, 5]
```

the prefix sums are:

```text
[1, 3, 7, 12]
```

Meaning:

```text
1 element  → 1
2 elements → 1 + 2 = 3
3 elements → 1 + 2 + 4 = 7
4 elements → 1 + 2 + 4 + 5 = 12
```

We can build this in `O(n)`:

```python
prefix = [0] * n

prefix[0] = nums[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + nums[i]
```

Or:

```python
prefix = []
total = 0

for num in nums:
    total += num
    prefix.append(total)
```

Result:

```text
nums   = [1, 2, 4, 5]
prefix = [1, 3, 7, 12]
```

---

# 6. Why Prefix Sum Helps

Suppose:

```text
prefix = [1, 3, 7, 12]
query = 7
```

We need to find the maximum number of elements whose sum is `<= 7`.

Look at the prefix sums:

```text
1  ≤ 7 ✓
3  ≤ 7 ✓
7  ≤ 7 ✓
12 ≤ 7 ✗
```

Therefore:

```text
answer = 3
```

So the problem has now become:

> Find how many values in the sorted `prefix` array are `<= query`.

This is a **binary search problem**.

---

# 7. Key Observation #3 — Binary Search

Because:

```text
prefix = [1, 3, 7, 12]
```

is sorted, we don't need to check every element.

We can use binary search.

We want to find:

> The first position where `prefix[i] > query`.

For:

```text
query = 7
```

we have:

```text
[1, 3, 7 | 12]
          ↑
       boundary
```

The first value greater than `7` is `12`.

Its index is:

```text
3
```

Therefore the answer is:

```text
3
```

---

# 8. Binary Search Implementation

```python
def binarySearch(arr, k):
    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) // 2

        if arr[mid] <= k:
            left = mid + 1
        else:
            right = mid

    return left
```

This finds the first index where:

```python
arr[index] > k
```

This is sometimes called an **upper bound**.

---

# 9. Understanding `left` and `right`

We start with:

```python
left = 0
right = len(arr)
```

For:

```text
arr = [1, 3, 7, 12]
```

we have:

```text
indices:  0   1   2   3
values:  [1,  3,  7, 12]
```

`right = 4` means the search range is:

```text
[0, 4)
```

So indices:

```text
0, 1, 2, 3
```

are possible.

---

# 10. Why Do We Use `right = len(arr)`?

We use:

```python
right = len(arr)
```

instead of:

```python
right = len(arr) - 1
```

because we are searching for a **position**, not necessarily an existing element.

Consider:

```text
arr = [1, 3, 7, 12]
query = 100
```

Every value is `<= 100`.

Therefore the answer is:

```text
4
```

But index `4` does not exist.

The position `4` means:

```text
[1, 3, 7, 12 |]
              ↑
          insertion point
```

This is why `right = len(arr)` is useful.

---

# 11. What Does `left` Mean?

This is the most important part.

At the end of binary search:

```python
return left
```

`left` represents:

> The first index where `arr[index] > k`.

Equivalently:

> The number of elements that are `<= k`.

Example:

```text
arr = [1, 3, 7, 12]
k = 7
```

We have:

```text
index:   0   1   2   3
value:  [1,  3,  7, 12]
         ✓   ✓   ✓   ✗
```

The first invalid index is:

```text
3
```

Therefore:

```python
left == 3
```

And there are exactly 3 valid values.

So:

```python
return left
```

returns:

```text
3
```

---

# 12. Why Don't We Check Index 0 First?

Binary search does NOT necessarily start at index `0`.

It starts at the middle.

For:

```text
[1, 3, 7, 12]
```

we start with:

```python
left = 0
right = 4
mid = 2
```

So we check:

```text
index 2 → 7
```

If:

```text
7 > query
```

we know:

```text
7 and everything after it
```

is too large because the array is sorted.

So we eliminate that entire section.

Binary search doesn't need to check every element individually.

The sorted property allows us to eliminate large portions of the search space.

---

# 13. Why `left = mid + 1`?

Suppose:

```python
arr[mid] <= k
```

Example:

```text
arr = [1, 3, 7, 12]
k = 7

mid = 2
arr[mid] = 7
```

Since:

```text
7 <= 7
```

`mid` is definitely a valid position.

Therefore we don't need to search `mid` anymore.

We move right:

```python
left = mid + 1
```

Meaning:

> `mid` is valid. Search for the first invalid position after it.

---

# 14. Why `right = mid`?

Suppose:

```python
arr[mid] > k
```

Example:

```text
arr = [1, 3, 7, 12]
k = 3

mid = 2
arr[mid] = 7
```

Since:

```text
7 > 3
```

`mid` could be the first invalid position.

So we keep `mid`:

```python
right = mid
```

We search the left side.

---

# 15. Complete Algorithm

```text
Step 1:
Sort nums

Step 2:
Build prefix sums

Step 3:
For each query:
    Binary search prefix
    Find first prefix sum > query
    Return its index

Step 4:
Store answers
```

---

# 16. Complete Solution

```python
class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()

        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        result = []

        for query in queries:
            k = self.binarySearch(prefix, query)
            result.append(k)

        return result

    def binarySearch(self, arr, k):
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2

            if arr[mid] <= k:
                left = mid + 1
            else:
                right = mid

        return left
```

---

# 17. Trace Example

Input:

```python
nums = [4, 5, 2, 1]
queries = [3, 10, 21]
```

### Sort

```text
[1, 2, 4, 5]
```

### Prefix Sum

```text
[1, 3, 7, 12]
```

### Query = 3

```text
[1, 3, 7, 12]
 ✓  ✓  ✗  ✗
```

Answer:

```text
2
```

### Query = 10

```text
[1, 3, 7, 12]
 ✓  ✓  ✓  ✗
```

Answer:

```text
3
```

### Query = 21

```text
[1, 3, 7, 12]
 ✓  ✓  ✓  ✓
```

Answer:

```text
4
```

Final:

```text
[2, 3, 4]
```

---

# 18. Complexity

Let:

```text
n = len(nums)
m = len(queries)
```

### Sorting

```python
nums.sort()
```

Time:

```text
O(n log n)
```

### Prefix Sum

```text
O(n)
```

### Binary Search

Each query:

```text
O(log n)
```

For `m` queries:

```text
O(m log n)
```

### Total

```text
O(n log n + m log n)
```

More precisely:

```text
O(n log n + m log n + n)
```

but we drop the smaller `O(n)` term:

```text
O(n log n + m log n)
```

### Space

Prefix array:

```text
O(n)
```

Result:

```text
O(m)
```

Therefore:

```text
Space = O(n + m)
```

If considering the output array separately, auxiliary space is `O(n)`.

---

# 19. DSA Pattern

The main pattern is:

```text
SORT
  ↓
PREFIX SUM
  ↓
BINARY SEARCH
```

This combination is useful when you see:

- "maximum number of elements"
- "sum must be <= X"
- many queries
- choosing the smallest elements is optimal
- sorted prefix sums
- need to repeatedly find how many values fit within a limit

---

# 20. How to Recognize This Pattern

Ask yourself these questions:

### Question 1

Do I want to maximize the **number of elements**?

If yes, try taking the smallest elements first.

### Question 2

Does the problem involve a **sum limit**?

If yes, consider prefix sums.

### Question 3

Do I have **many queries** asking different limits?

If yes, preprocessing can help.

### Question 4

After preprocessing, is my array sorted?

If yes, consider binary search.

This leads to:

```text
Sort
→ Prefix Sum
→ Binary Search
```

---

# 21. Mistakes I Made / Important Lessons

### Mistake 1 — Checking individual numbers

Wrong idea:

```python
if nums[j] < query:
```

A number being smaller than the query doesn't mean it can be included with the other numbers.

We care about the **total sum**.
--> One importance thing is : Binary search finds the first invalid position; because all positions before it are valid, that position equals the number of valid elements.

---

### Mistake 2 — Repeated `sum()`

Avoid:

```python
sum(ans)
```

inside a loop.

`sum()` itself is `O(n)`.

Instead maintain a running total:

```python
total += nums[i]
```

---

### Mistake 3 — Incorrect prefix sum

Wrong:

```python
ans[i] += nums[i - 1]
```

because `ans[i]` starts at zero.

Correct:

```python
prefix[i] = prefix[i - 1] + nums[i]
```

Each prefix value must contain the **entire sum from index 0 to i**.

---

### Mistake 4 — Thinking `left` is the last valid index

It is NOT.

For:

```text
[1, 3, 7, 12]
```

and:

```text
query = 7
```

the last valid index is:

```text
2
```

but binary search returns:

```text
3
```

because `3` is the **first invalid position**.

That position also tells us:

```text
number of valid elements = 3
```

So:

```python
return left
```

is correct.

---

# 22. Core Idea to Remember

The entire problem can be reduced to:

```text
nums = [4, 5, 2, 1]

        ↓ sort

[1, 2, 4, 5]

        ↓ prefix sum

[1, 3, 7, 12]

        ↓ binary search(query)

Find first value > query

        ↓

Its index = number of elements we can take
```

The most important mental model is:

> **After sorting, the cheapest way to choose `k` elements is to take the first `k` elements. Prefix sums tell us the cost of taking those `k` elements. Binary search tells us the largest `k` whose cost fits the query.**

That is the reason the solution works.
