# Two Pointers vs Running Sum

## Important Correction

A common mistake is thinking:

> "If my brute-force solution recalculates the array, I should use Two Pointers."

This is **NOT always true**.

The better rule is:

> **If my brute-force solution repeatedly recalculates overlapping information, look for a way to maintain that information incrementally.**

Then ask:

> **What pattern is actually being used to maintain it?**

Possible answers include:

- Prefix Sum / Running Sum
- Two Pointers
- Sliding Window
- HashMap
- Math
- or a combination of patterns

---

# 1. Recalculating Does NOT Automatically Mean Two Pointers

Suppose we have:

```python
for i in range(n):
    left = sum(nums[:i])
    right = sum(nums[i+1:])
```

This repeatedly calculates overlapping sums.

The optimization is:

```python
left += nums[i]
right -= nums[i]
```

But this is primarily a **Running Sum / Prefix Sum idea**.

Why?

Because the important optimization is:

> Don't calculate the same sum repeatedly. Update the previous sum.

---

# 2. How to Recognize True Two Pointers

Two Pointers usually means we have **two indices/pointers** that represent positions in the data.

Example:

```text
L →                 ← R
[ 1  2  3  4  5  6  7 ]
```

The pointers move according to some condition:

```python
if condition:
    left += 1
else:
    right -= 1
```

The important characteristic is:

> **Two positions are being manipulated to search or shrink/expand a region.**

Examples:

- Two Sum II
- 3Sum
- Container With Most Water
- Valid Palindrome
- Remove Duplicates
- Trapping Rain Water

---

# 3. Running Sum / Prefix Sum

Running Sum means we maintain accumulated information as we move through the array.

Instead of:

```python
sum(nums[:i])
```

again and again, do:

```python
left += nums[i]
```

Example:

```text
nums = [1, 2, 3, 4, 5]

i = 0
left = 1

i = 1
left = 1 + 2 = 3

i = 2
left = 3 + 3 = 6

i = 3
left = 6 + 4 = 10
```

Each element is processed once.

Therefore:

```text
O(n)
```

instead of repeatedly calculating:

```text
O(n²)
```

---

# 4. Sliding Window Is Different

Sliding Window also uses pointers, but the pointers define a **contiguous window**.

Example:

```text
L
↓
[ 1  2  3 ] 4  5  6
          ↑
          R
```

Then the window moves:

```text
   L
   ↓
[ 1  2  3 ] 4  5  6
          ↑
          R
```

becomes:

```text
      L
      ↓
1 [ 2  3  4 ] 5  6
            ↑
            R
```

Typical signs:

- "contiguous subarray"
- "longest substring"
- "shortest subarray"
- "maximum/minimum window"
- maintain a window satisfying a condition

---

# 5. Pivot Integer — Why It Can Be Two Pointers

Your Pivot Integer solution:

```python
leftValue = 1
rightValue = n

leftSum = leftValue
rightSum = rightValue
```

has actual **left and right boundaries**:

```text
L →                    ← R
[ 1  2  3  4  5  6  7  8 ]
```

You decide which boundary to move:

```python
if leftSum < rightSum:
    leftValue += 1
else:
    rightValue -= 1
```

Therefore this is legitimately:

```text
Two Pointers
+
Running Sum
```

The pointers move from opposite sides.

Eventually:

```text
L        Pivot        R
↓          ↓          ↓
1 2 3 4 5 [6] 7 8
```

And:

```text
leftSum == rightSum
```

---

# 6. Count Partitions — Why It Is NOT Really Two Pointers

Consider:

```text
[ 1  2  3 | 4  5 ]
          ↑
       partition
```

The partition moves:

```text
[ 1 | 2  3  4  5 ]

[ 1  2 | 3  4  5 ]

[ 1  2  3 | 4  5 ]
```

There is only **one moving position**.

We can maintain:

```python
left += nums[i]
right -= nums[i]
```

This is primarily:

```text
Running Sum / Prefix Sum
```

And the problem has an even stronger mathematical observation:

```text
left + right = total
```

Therefore:

```text
left - right
= left - (total - left)
= 2 * left - total
```

Since:

```text
2 * left
```

is always even, the parity of the difference depends only on `total`.

Therefore:

```text
total is even
    ↓
every partition has even difference

total is odd
    ↓
no partition has even difference
```

So the optimal solution is actually **Math + Parity**.

---

# 7. The Critical Difference

Don't classify a problem based on variable names.

This:

```python
left = ...
right = ...
```

does **NOT** automatically mean Two Pointers.

Instead ask:

### Question 1

Are `left` and `right` **indices/positions**?

```text
L →             ← R
[ 1 2 3 4 5 6 ]
```

If yes, Two Pointers may be involved.

---

### Question 2

Are `left` and `right` just **values/sums**?

```python
left_sum = ...
right_sum = ...
```

Then it is probably:

```text
Prefix Sum / Running Sum
```

---

### Question 3

Are two indices defining a **contiguous region/window**?

```text
[ 2 3 4 5 ]
  L     R
```

Then think:

```text
Sliding Window
```

---

### Question 4

Are the two pointers moving toward each other?

```text
L →       ← R
```

Then think:

```text
Two Pointers
```

---

# 8. Pattern Recognition Cheat Sheet

| What you see                              | Think                    |
| ----------------------------------------- | ------------------------ |
| Recalculate overlapping sums              | Running Sum / Prefix Sum |
| Two indices move toward each other        | Two Pointers             |
| Two boundaries define a contiguous window | Sliding Window           |
| Need accumulated sum up to index `i`      | Prefix Sum               |
| Need `sum(left...right)` quickly          | Prefix Sum               |
| Left/right positions make decisions       | Two Pointers             |
| Window expands/shrinks based on condition | Sliding Window           |
| Left/right are only sums, not positions   | Probably Running Sum     |
| Mathematical property eliminates scanning | Math                     |

---

# 9. The Correct Mental Model

Instead of memorizing:

```text
"Recalculation → Two Pointers"
```

memorize:

```text
Repeated calculation
        ↓
Can I reuse previous information?
        ↓
       YES
        ↓
What am I maintaining?
        ↓
 ┌──────┼──────────┐
 ↓      ↓          ↓
Sum   Window   Two boundaries
 ↓      ↓          ↓
Prefix Sliding   Two
Sum    Window   Pointers
```

---

# 10. General Rule

When solving a brute-force problem, ask:

### Step 1 — What work am I repeating?

Example:

```python
sum(nums[:i])
sum(nums[:i+1])
sum(nums[:i+2])
```

### Step 2 — Does the next calculation overlap the previous one?

Here:

```text
[1 2 3]
[1 2 3 4]
```

Yes.

### Step 3 — Can I update instead of recalculate?

```python
current_sum += nums[i]
```

### Step 4 — What pattern does the update represent?

If you're maintaining accumulated sums:

```text
Prefix Sum / Running Sum
```

If you're moving two positions:

```text
Two Pointers
```

If you're maintaining a contiguous region:

```text
Sliding Window
```

---

# Key Lesson

> **Optimization technique and DSA pattern are not always the same thing.**

For example:

```text
Brute Force
    ↓
Repeated sum calculations
    ↓
Running Sum
```

doesn't automatically become:

```text
Two Pointers
```

And:

```text
Two Pointers
+
Running Sum
```

is also possible, as in your **Pivot Integer** solution.

The safest question is:

> **"What are my pointers actually doing?"**

If they are **positions moving through the data**, Two Pointers may be the pattern.

If they are simply **values that I update incrementally**, you're probably looking at Running Sum / Prefix Sum instead.
