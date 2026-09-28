# Contribution Technique — Odd-Length Subarrays

## Core Idea

When a problem asks for the **sum of many subarrays**, don't immediately generate every subarray.

Instead, ask:

> **How many valid subarrays contain each element?**

Then calculate the contribution of each element.

```text
contribution = number of valid subarrays containing arr[i] × arr[i]
```

Finally:

```text
answer = sum of all element contributions
```

---

## Example: Sum of Odd-Length Subarrays

Given:

```python
arr = [1, 4, 2, 5, 3]
```

Instead of generating every odd-length subarray, consider each element individually.

### Step 1 — Count all subarrays containing `arr[i]`

For an element at index `i`:

```python
left_choices = i + 1
right_choices = n - i
```

Therefore:

```python
total_sub = (i + 1) * (n - i)
```

### Why?

For `arr[i]` to be inside a subarray:

- The starting index can be anywhere from `0` to `i` → `i + 1` choices.
- The ending index can be anywhere from `i` to `n - 1` → `n - i` choices.

Therefore:

```text
total subarrays containing arr[i]
= (i + 1) × (n - i)
```

---

## Step 2 — Count the Odd-Length Ones

Among these subarrays, the number with odd length is:

```python
odd = (total_sub + 1) // 2
```

This is equivalent to:

```text
ceil(total_sub / 2)
```

Therefore:

```text
odd_count
= ceil(((i + 1)(n - i)) / 2)
```

---

## Step 3 — Calculate the Element's Contribution

If `arr[i]` appears in `odd_count` valid subarrays:

```python
total += odd_count * arr[i]
```

So:

```text
contribution
= odd_count × arr[i]
```

---

## Complete Formula

The entire solution can be represented as:

```text
answer =
Σ arr[i] × ceil(((i + 1)(n - i)) / 2)
```

Or in Python:

```python
for i in range(n):
    total_sub = (i + 1) * (n - i)
    odd = (total_sub + 1) // 2
    total += odd * arr[i]
```

---

## Pattern Recognition

### Contribution Technique

Use this pattern when:

- The problem asks for a **sum/count over many subarrays**.
- Brute force would enumerate `O(n²)` subarrays.
- Each element contributes independently to the final answer.
- You can mathematically count how many valid subarrays contain each element.

Think:

```text
Instead of:

    generate every subarray
            ↓
    calculate its value
            ↓
    add to answer

Try:

    for each element
            ↓
    count how many valid subarrays contain it
            ↓
    calculate its contribution
            ↓
    add contribution
```

### Mental Trigger

When you see:

> "Sum of all subarrays..."

Ask yourself:

> **"How many times does each element appear across all valid subarrays?"**

If that number can be calculated with a formula, you may be able to reduce an `O(n²)` brute-force solution to `O(n)`.

---

## Complexity

```text
Time:  O(n)
Space: O(1)
```

There is only one loop and no additional array is created.

---

## Important Distinction

This is **not**:

- Two Pointers
- Sliding Window
- Prefix Sum

The main pattern is:

```text
Contribution Technique
        +
Mathematical Counting Formula
```

The key skill is recognizing when **counting element contributions** is easier than **enumerating every subarray**.
