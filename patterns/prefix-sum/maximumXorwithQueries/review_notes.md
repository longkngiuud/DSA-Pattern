# Prefix XOR + Maximum XOR

## Recognition Clue

Think **Prefix XOR** when the problem involves:

- XOR (`^`)
- cumulative XOR of elements
- XOR of a subarray/prefix
- repeatedly removing elements from the end
- finding a value `k` that maximizes XOR

### Important

**Prefix Sum does NOT always mean `+`.**

There are different types of prefix accumulation:

```text
Normal Prefix Sum:
prefix[i] = prefix[i-1] + nums[i]

Prefix XOR:
prefix[i] = prefix[i-1] ^ nums[i]
```

For this problem, I need **XOR**, not addition.

---

## Core Pattern

Build cumulative XOR:

```python
prefix[0] = nums[0]

for i in range(1, n):
    prefix[i] = prefix[i-1] ^ nums[i]
```

Example:

```text
nums = [0, 1, 2, 2, 5, 7]

prefix XOR:
0
0 ^ 1 = 1
1 ^ 2 = 3
3 ^ 2 = 1
1 ^ 5 = 4
4 ^ 7 = 3

→ [0, 1, 3, 1, 4, 3]
```

---

## Why `^` Instead of `+`?

XOR has different properties from addition:

```text
a ^ a = 0
a ^ 0 = a
```

And XOR is useful for cumulative XOR because:

```text
prefix[i] = nums[0] ^ nums[1] ^ ... ^ nums[i]
```

So when the problem asks about XOR accumulation, use:

```python
^
```

not:

```python
+
```

---

## Maximum XOR Trick

The problem gives:

```python
maximumBit = 3
```

Therefore the largest possible 3-bit number is:

```text
111
```

which is:

```python
mx = (1 << maximumBit) - 1
```

For `maximumBit = 3`:

```text
1 << 3 = 1000
1000 - 1 = 0111
```

So:

```text
mx = 7
```

To maximize:

```text
current_xor ^ k
```

choose:

```python
k = current_xor ^ mx
```

because:

```text
current_xor ^ (current_xor ^ mx)
= mx
```

---

## Important Pattern

```text
Prefix XOR
    ↓
current XOR
    ↓
Need maximum XOR
    ↓
maximum possible value = (1 << maximumBit) - 1
    ↓
k = current_xor ^ maximum_value
```

Then reverse the answers because the queries are made while removing elements from the end.

---

## Recognition Rule

When I see:

> **"XOR of a prefix/subarray"**

think:

```text
Prefix XOR
```

When I see:

> **"Choose k to maximize XOR with a value under maximumBit"**

think:

```text
all 1s mask
    ↓
(1 << maximumBit) - 1
    ↓
k = current_xor ^ mask
```

---

## My Mistake to Remember

I initially remembered **Prefix Sum** as:

```python
prefix[i] = prefix[i-1] + nums[i]
```

but this problem uses **Prefix XOR**:

```python
prefix[i] = prefix[i-1] ^ nums[i]
```

### Review reminder

> **Prefix means cumulative information. The operation does not have to be `+`.**

Always check what operation the problem is asking for:

```text
Sum  → +
XOR  → ^
Product → *
Min → min()
Max → max()
```

The important skill is:

**Identify the cumulative operation first, then choose the prefix technique.**
