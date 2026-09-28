# Two Pointers

## 1. Core Idea

**Two Pointers** is a technique where we use two indexes/pointers to traverse an array, string, or linked list while moving them according to a logical condition.

The main goal is to **avoid checking every possible pair/position**.

Instead of:

```text
O(n²) brute force
    ↓
check many combinations
```

we use:

```text
two pointers
    ↓
eliminate impossible possibilities
    ↓
move pointers intelligently
    ↓
often O(n)
```

### The most important question

> **Why is it safe to move this pointer?**

If you cannot explain why a pointer can move, you probably haven't found the correct Two Pointer strategy yet.

---

# 2. Main Patterns

There are 3 major forms to know.

## Pattern 1 — Opposite Directions

Pointers start at opposite ends:

```text
L →              ← R

[1, 2, 3, 4, 5, 6]
```

Typical template:

```python
left = 0
right = len(nums) - 1

while left < right:

    if condition:
        left += 1
    elif condition:
        right -= 1
    else:
        ...
```

Common uses:

- Sorted pair problems
- Palindromes
- Reverse array/string
- Container With Most Water
- 3Sum

---

## Pattern 2 — Same Direction

Both pointers move from left to right.

```text
slow → fast →
```

Usually:

```text
fast = explorer
slow = position for useful data
```

Example:

```python
slow = 0

for fast in range(len(nums)):
    if condition:
        nums[slow] = nums[fast]
        slow += 1
```

Common uses:

- Remove duplicates
- Remove elements
- Move zeroes
- In-place filtering
- Partitioning

---

## Pattern 3 — Fast and Slow

One pointer moves faster than the other.

```text
slow →
fast → →
```

Common in linked lists:

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

Common uses:

- Find middle of linked list
- Detect linked-list cycle
- Find cycle entry
- Remove nth node from end

---

# 3. Opposite-Direction Two Pointers

This is especially powerful when the array is **sorted**.

Example:

```text
nums = [1, 2, 3, 5, 7, 9]
```

```text
L               R
↓               ↓
[1, 2, 3, 5, 7, 9]
```

Suppose we want:

```text
nums[L] + nums[R] = target
```

If:

```text
sum < target
```

move:

```python
left += 1
```

Why?

Because the array is sorted, moving `L` right gives us a larger number and therefore a larger sum.

If:

```text
sum > target
```

move:

```python
right -= 1
```

Why?

Because moving `R` left gives us a smaller number and therefore a smaller sum.

### Sorted Pair Rule

```text
sum < target → L++
sum > target → R--
sum == target → found
```

Do NOT memorize this without understanding the reason.

The reason is:

> **Sorted order tells us which direction can improve the current result.**

---

# 4. Why Sorting Is Important

Two Pointers often depends on knowing the relationship between neighboring values.

Example:

```text
[1, 2, 3, 5, 7, 9]
```

If:

```text
1 + 9 > target
```

we know replacing `9` with a smaller value can decrease the sum.

Therefore we can safely move `R`.

Without sorted order:

```text
[5, 1, 9, 2, 7, 3]
```

we cannot make the same guarantee.

### Important

Sorting costs:

```text
O(n log n)
```

Two Pointers after sorting often costs:

```text
O(n)
```

So the total may be:

```text
O(n log n)
```

Also ask:

> **Does sorting destroy information such as original indexes/order?**

If yes, sorting may not be appropriate.

---

# 5. The Real Power: Eliminating Possibilities

Two Pointers is not simply:

> "Use two indexes."

The real idea is:

> **Use information from the current pointers to eliminate a whole group of impossible possibilities.**

Example:

```text
[1, 2, 3, 5, 7, 10]
 L              R
```

If:

```text
1 + 10 > target
```

and the array is sorted, then using `10` with any larger left value will also produce a sum that is too large.

Therefore we can eliminate that possibility and move:

```text
R--
```

Instead of checking every combination individually.

---

# 6. Complexity

If both pointers only move in one direction:

```text
L → → → →
← ← ← R
```

each pointer can move at most `n` times.

Therefore:

```text
O(n) + O(n)
= O(n)
```

### Important

A `while` loop containing two pointers is **not automatically O(n²)**.

Ask:

> **How many times can each pointer move?**

If each pointer moves at most `n` times:

```text
O(n)
```

This is sometimes called **amortized reasoning**.

---

# 7. Example — Two Sum II

```python
def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]

        elif total < target:
            left += 1

        else:
            right -= 1
```

For:

```text
nums = [2, 7, 11, 15]
target = 9
```

Start:

```text
L           R
↓           ↓
2  7  11  15
```

```text
2 + 15 = 17 > 9
```

Move `R`.

```text
L       R
↓       ↓
2  7  11  15
```

```text
2 + 11 = 13 > 9
```

Move `R`.

```text
L   R
↓   ↓
2  7  11  15
```

```text
2 + 7 = 9
```

Found.

---

# 8. Example — Valid Palindrome

Compare characters from both ends:

```text
L               R
↓               ↓
r a c e c a r
```

If:

```python
s[left] != s[right]
```

the string is not a palindrome.

Otherwise:

```python
left += 1
right -= 1
```

Template:

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

---

# 9. Example — Remove Duplicates

For:

```text
[1, 1, 2, 2, 3]
```

use:

```text
fast = explorer
slow = write position
```

```python
def remove_duplicates(nums):
    slow = 1

    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1

    return slow
```

Mental model:

```text
fast → searches
slow → stores useful values
```

This is an **in-place Two Pointer** pattern.

---

# 10. Example — Container With Most Water

Area:

```text
width × height
```

Specifically:

```python
area = (right - left) * min(height[left], height[right])
```

The important insight:

> **The shorter side limits the area.**

Therefore, after calculating the current area, move the pointer at the shorter height.

```python
if height[left] < height[right]:
    left += 1
else:
    right -= 1
```

Why?

Moving the taller side alone cannot increase the limiting height, while the width becomes smaller.

So we need to search for a taller version of the shorter side.

---

# 11. 3Sum = Sorting + Two Pointers

Example:

```text
[-1, 0, 1, 2, -1, -4]
```

First:

```python
nums.sort()
```

Result:

```text
[-4, -1, -1, 0, 1, 2]
```

Then fix one number:

```text
 i   L           R
 ↓   ↓           ↓
[-4, -1, -1, 0, 1, 2]
```

Calculate:

```text
nums[i] + nums[L] + nums[R]
```

Rules:

```text
sum < 0 → L++
sum > 0 → R--
sum == 0 → record answer
```

Complexity:

```text
Sorting       O(n log n)
Two Pointers  O(n²)
---------------------
Overall       O(n²)
```

Why isn't it `O(n³)`?

For every fixed `i`, `L` and `R` together move through the array only `O(n)` times.

Therefore:

```text
n choices for i
×
O(n) Two Pointer work
=
O(n²)
```

---

# 12. Two Pointers vs Sliding Window

They are related but not identical.

### Two Pointers

Uses two indexes to navigate through data.

```text
L ↔ R
```

or:

```text
slow → fast
```

### Sliding Window

Maintains a **contiguous range**:

```text
[ L ........ R ]
```

Example:

```python
left = 0

for right in range(len(nums)):
    ...

    while invalid:
        left += 1
```

### Key distinction

> **Sliding Window usually uses Two Pointers, but not every Two Pointer problem is a Sliding Window problem.**

---

# 13. Two Pointers vs Prefix Sum

### Prefix Sum

Main idea:

```text
Reuse previously calculated cumulative information.
```

Used for:

- Range sums
- Subarray sums
- Running totals

### Two Pointers

Main idea:

```text
Use pointer movement to eliminate possibilities.
```

Used for:

- Pairs
- Triplets
- Palindromes
- In-place modifications
- Linked-list fast/slow problems

---

# 14. Two Pointers vs Hash Map

For a pair-sum problem:

### Hash Map

```text
Time:  O(n)
Space: O(n)
```

### Two Pointers on sorted data

```text
Time:  O(n)
Space: O(1)
```

But sorting may add:

```text
O(n log n)
```

and may destroy original ordering/index information.

So always consider the trade-off.

---

# 15. How to Recognize Two Pointers

When reading a new problem, ask:

### 1. Is the input an array/string/linked list?

Possible Two Pointers.

### 2. Is the array sorted?

Strong signal, especially for:

```text
pair sum
triplet
closest sum
```

### 3. Do I need to compare both ends?

Think:

```text
L ↔ R
```

Examples:

- Palindrome
- Reverse
- Container

### 4. Do I need in-place modification?

Think:

```text
slow + fast
```

Examples:

- Remove duplicates
- Remove elements
- Move zeroes

### 5. Is this a linked list?

Think:

```text
slow + fast
```

especially:

- cycle
- middle
- nth node

### 6. Can I safely eliminate possibilities by moving one pointer?

If yes, Two Pointers is a strong candidate.

---

# 16. Common Mistakes

## Mistake 1 — Moving pointers randomly

Wrong:

```python
if something:
    left += 1
else:
    right -= 1
```

without understanding why.

Always ask:

> Why can I eliminate everything behind/in front of this pointer?

---

## Mistake 2 — Assuming two indexes = Two Pointers

Having:

```python
i
j
```

doesn't automatically mean Two Pointers.

There must be a **logical movement strategy**.

---

## Mistake 3 — Forgetting sorted order

The rule:

```text
sum < target → left++
sum > target → right--
```

depends on the array being sorted.

---

## Mistake 4 — Sorting when order matters

Sorting can destroy:

```text
original indexes
original ordering
```

Check the problem requirements first.

---

## Mistake 5 — Incorrect loop condition

Usually:

```python
while left < right:
```

because the two pointers represent two different positions.

But use `<=` when the problem specifically allows the pointers to meet and use the same position.

---

## Mistake 6 — Ignoring duplicates

Important in problems like:

```text
3Sum
4Sum
```

You often need to skip duplicate values to avoid duplicate answers.

---

# 17. Master Mental Model

Think of Two Pointers as:

```text
                 TWO POINTERS
                      |
          +-----------+-----------+
          |                       |
     Opposite Ends          Same Direction
          |                       |
        L ↔ R                 slow → fast
          |                       |
     sorted pairs            in-place
     palindrome              filtering
     3Sum                     duplicates
     container                partition
          |
      Fast / Slow
          |
      Linked Lists
      cycle / middle
```

The universal process is:

```text
1. Put two pointers somewhere useful.
            ↓
2. Evaluate the current positions.
            ↓
3. Determine what information you learned.
            ↓
4. Eliminate impossible possibilities.
            ↓
5. Move the pointer that can improve the situation.
            ↓
6. Repeat until the search is finished.
```

---

# 18. The One Rule to Remember

> **Two Pointers = intelligently moving two positions so that each movement eliminates unnecessary possibilities.**

Don't memorize solutions.

For every Two Pointer problem, explain:

```text
Where do my pointers start?

What does each pointer represent?

What condition do I check?

Which pointer should move?

WHY is it safe to move that pointer?

How many times can each pointer move?

What is the final complexity?
```

If you can answer those six questions, you understand the pattern.

---

# 19. Recommended Problems

Learn them in this order:

1. Valid Palindrome
2. Reverse String
3. Two Sum II
4. Remove Duplicates from Sorted Array
5. Move Zeroes
6. Squares of a Sorted Array
7. Container With Most Water
8. 3Sum
9. 4Sum
10. Linked List Cycle
11. Middle of the Linked List
12. Remove Nth Node From End of List

---

# Quick Review

```text
TWO POINTERS
============

Core idea:
Use two pointers and move them intelligently to eliminate
unnecessary possibilities.

Main patterns:
1. Opposite ends: L ↔ R
2. Same direction: slow → fast
3. Fast/slow: different speeds
4. Fixed-gap pointers

Strong clues:
- sorted array + pair/triplet
- compare both ends
- palindrome
- reverse
- in-place modification
- remove duplicates/elements
- linked-list cycle/middle

Key question:
"Why is it safe to move this pointer?"

Sorted pair:
sum < target → L++
sum > target → R--
sum == target → found

Complexity:
If each pointer moves at most O(n):
→ O(n)

Sorting:
O(n log n)

3Sum:
sort + Two Pointers
→ O(n²)

Advantages:
- often O(n)
- often O(1) extra space
- avoids brute force

Warning:
Two indexes ≠ automatically Two Pointers.
There must be a logical movement strategy.
```
