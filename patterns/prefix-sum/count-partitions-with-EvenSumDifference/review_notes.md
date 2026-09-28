# Count Partitions with Even Sum Difference

## 1. What is the problem asking?

We need to count the number of ways to split an array into:

```text
left subarray | right subarray
```

For every possible partition, calculate:

```text
abs(sum(left) - sum(right))
```

A partition is valid if the difference is **even**.

There are exactly:

```text
n - 1
```

possible partition points.

---

# 2. My Initial Intuition

When I see a problem that repeatedly asks for the sum of the left and right parts of an array, I should think:

```text
Need repeated sums
        ↓
Prefix Sum / Running Sum
        ↓
Know the total sum
        ↓
rightSum = totalSum - leftSum
```

So the main pattern is:

> **Running Sum (Prefix Sum idea) + Total Sum**

---

# 3. Brute Force Approach

For every possible partition:

1. Calculate the sum of the left part.
2. Calculate the sum of the right part.
3. Calculate the difference.
4. Check whether the difference is even.
5. Increment the answer if it is even.

Example:

```text
[10, 10, 3 | 7, 6]

leftSum  = 23
rightSum = 13

difference = |23 - 13|
           = 10

10 is even → valid partition
```

---

# 4. Why is Brute Force O(n²)?

There are:

```text
O(n)
```

possible partition points.

For each partition, I may loop through the remaining elements to calculate the right-side sum.

Therefore:

```text
O(n) partitions
×
O(n) work per partition
=
O(n²)
```

### Important wording

Don't say:

> "It checks every subarray."

More accurately:

> **It checks every possible partition and repeatedly calculates the sums of the two sides.**

---

# 5. Optimized Idea

Instead of calculating the right-side sum from scratch every time:

### Step 1 — Calculate total sum once

```python
totalSum = sum(nums)
```

### Step 2 — Maintain a running left sum

```python
leftSum += nums[i]
```

As the partition moves:

```text
[10 | 10, 3, 7, 6]
 leftSum = 10

[10, 10 | 3, 7, 6]
 leftSum = 20

[10, 10, 3 | 7, 6]
 leftSum = 23
```

### Step 3 — Calculate right sum instantly

Because:

```text
leftSum + rightSum = totalSum
```

we know:

```text
rightSum = totalSum - leftSum
```

Therefore, we don't need another loop.

---

# 6. Why is this related to Prefix Sum?

A Prefix Sum array might look like:

```text
nums:   [10, 10, 3, 7, 6]
prefix: [10, 20, 23, 30, 36]
```

But we don't need to store the entire prefix array.

We only need the current prefix sum:

```python
leftSum += nums[i]
```

Therefore, this solution uses the **Prefix Sum idea**, implemented as a **running sum**.

### Terminology

```text
Prefix Sum
    ↓
The sum from the beginning up to the current position

Running Sum
    ↓
Continuously updating that prefix sum as we iterate
```

For this problem:

> **Running Sum is essentially the Prefix Sum we need at the current partition.**

---

# 7. Optimized Algorithm

```text
Calculate totalSum
        ↓
leftSum = 0
        ↓
Move partition from left to right
        ↓
Add nums[i] to leftSum
        ↓
rightSum = totalSum - leftSum
        ↓
Calculate |leftSum - rightSum|
        ↓
Is it even?
        ↓
Yes → count += 1
```

---

# 8. Why Does `totalSum - leftSum` Give the Right Sum?

The entire array is:

```text
left + right
```

Therefore:

```text
totalSum = leftSum + rightSum
```

Rearrange:

```text
rightSum = totalSum - leftSum
```

This allows us to calculate the right sum in:

```text
O(1)
```

time.

---

# 9. Important Parity Insight

There is an even stronger observation.

We know:

```text
leftSum + rightSum = totalSum
```

We want:

```text
leftSum - rightSum
```

Substitute:

```text
rightSum = totalSum - leftSum
```

Then:

```text
leftSum - rightSum
= leftSum - (totalSum - leftSum)
= 2 × leftSum - totalSum
```

Now:

```text
2 × leftSum
```

is **always even**.

Therefore, the parity of:

```text
2 × leftSum - totalSum
```

depends only on `totalSum`.

---

# 10. The Final Mathematical Shortcut

### If `totalSum` is even:

```text
difference = even
```

for **every partition**.

Therefore:

```text
answer = n - 1
```

because there are `n - 1` possible partitions.

### If `totalSum` is odd:

```text
difference = odd
```

for **every partition**.

Therefore:

```text
answer = 0
```

So the entire problem can actually be solved with:

```python
if sum(nums) % 2 == 0:
    return len(nums) - 1
return 0
```

---

# 11. Parity Rule to Remember

Two numbers have an **even difference** when they have the same parity:

```text
even - even = even
odd - odd   = even
```

Two numbers have an **odd difference** when their parity is different:

```text
even - odd = odd
odd - even = odd
```

### Important correction

If `totalSum` is even, it does **NOT** mean:

```text
leftSum = even
rightSum = even
```

They could both be odd:

```text
leftSum  = 5
rightSum = 7

5 + 7 = 12  → even
7 - 5 = 2   → even
```

The correct statement is:

> **If the total sum is even, the left and right sums have the same parity.**

---

# 12. Two Levels of Solution

## Level 1 — Running Sum + Total Sum

```text
totalSum
+
running leftSum
+
rightSum = totalSum - leftSum
```

Complexity:

```text
Time:  O(n)
Space: O(1)
```

This is the general approach for this problem.

---

## Level 2 — Mathematical Simplification

Notice:

```text
leftSum - rightSum
= 2 × leftSum - totalSum
```

Since `2 × leftSum` is always even:

```text
total even → difference always even
total odd  → difference always odd
```

Therefore:

```text
total even → answer = n - 1
total odd  → answer = 0
```

Complexity:

```text
Time:  O(n)   # to calculate total sum
Space: O(1)
```

---

# 13. How to Recognize This Pattern in a New Problem

When reading a new problem, ask:

### Question 1

> Is the array being split into a left part and a right part?

If yes, think:

```text
left | right
```

### Question 2

> Do I need the sum of the left and/or right side?

If yes:

```text
Prefix Sum / Running Sum
```

### Question 3

> Can I calculate the other side from the total?

Usually:

```text
rightSum = totalSum - leftSum
```

### Question 4

> Is the problem asking about even/odd, divisibility, or some mathematical property?

If yes:

> **Try algebraic simplification before writing complicated code.**

For this problem, that reveals the parity shortcut.

---

# 14. Common Mistakes

### Mistake 1 — Recalculating the right sum

Bad:

```python
for i in range(n):
    for j in range(i + 1, n):
        rightSum += nums[j]
```

This creates unnecessary O(n²) work.

Instead:

```python
rightSum = totalSum - leftSum
```

---

### Mistake 2 — Thinking the problem counts arbitrary subarrays

It doesn't.

It counts:

> **valid partition points**

There are:

```text
n - 1
```

possible partitions.

---

### Mistake 3 — Thinking an even total means both sides must be even

Wrong:

```text
total is even
→ left is even
→ right is even
```

Correct:

```text
total is even
→ left and right have the same parity
→ their difference is even
```

---

### Mistake 4 — Only memorizing the code

Don't memorize:

```python
rightSum = totalSum - leftSum
```

without understanding why.

Remember:

```text
total = left + right

therefore:

right = total - left
```

---

### Mistake 5 — Missing the mathematical shortcut

After finding:

```text
right = total - left
```

always ask:

> **Can I simplify the condition mathematically?**

Here:

```text
|left - right|
= |2 × left - total|
```

which immediately reveals the parity of the difference.

---

# 15. What I Should Be Able to Recall During My Next Review

Without looking at my solution, I should be able to say:

> "The problem splits the array into a left and right part and asks me to count valid partition points. Since I repeatedly need the sums of the two sides, I can maintain a running left sum and calculate the right sum from the total: `rightSum = totalSum - leftSum`. This gives an O(n) solution. Then I can simplify further: `leftSum - rightSum = 2 × leftSum - totalSum`, so the difference has the same parity as the total. Therefore, if the total is even, every partition is valid; if it's odd, none are."

If I can explain that **without looking at my notes**, I understand the problem rather than just recognizing the solution.

---

# 16. Review Rating

### My current understanding:

**🟡 Partial → Strong Partial**

I can:

- Identify the partition structure ✅
- Understand running sum ✅
- Understand total sum ✅
- Understand `rightSum = totalSum - leftSum` ✅
- Explain why brute force is O(n²) ✅
- Understand the even-difference condition ⚠️
- Need to strengthen the algebraic/parity insight ⚠️

### What to revisit later:

```text
1. Why does total parity determine difference parity?
2. Why does an even total mean left/right have the same parity?
3. Why are there exactly n - 1 partitions?
4. Why is running sum a Prefix Sum idea?
```

---

# 17. One-Sentence Memory Hook

> **When an array is split into left and right parts, maintain the left running sum and use `total - left` for the right; then check whether the condition can be simplified using the relationship `left + right = total`.**
