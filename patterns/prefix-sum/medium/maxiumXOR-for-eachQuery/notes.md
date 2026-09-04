## Maximum XOR for Each Query

### Pattern: Running XOR / Prefix XOR + Bit Mask

### Core Idea

We are given an array `nums` and need to find the maximum value of:

    current_xor ^ k

where `k` must be between:

    0 and 2^maximumBit - 1

The maximum possible value for `k` is therefore:

    maximumXor = (1 << maximumBit) - 1

This creates a number whose lowest `maximumBit` bits are all `1`.

### Why XOR with the Maximum Mask?

To maximize:

    current_xor ^ k

we want every bit of the result to be `1`.

If a bit in `current_xor` is:

    0 → choose k bit = 1
    1 → choose k bit = 0

Therefore:

    k = current_xor ^ maximumXor

Example:

    current_xor  = 1010
    maximumXor   = 1111
                   ----
    k            = 0101

Then:

    1010 ^ 0101 = 1111

So `k` maximizes the XOR.

---

### The Important Part: Queries Are Done in Reverse

The array is processed by repeatedly removing the last element.

Initially:

    current_xor = nums[0] ^ nums[1] ^ ... ^ nums[n-1]

For the first query, use the XOR of the entire array.

After calculating the answer, remove the last number:

    current_xor ^= nums[n - 1]

Why does this work?

Because:

    a ^ a = 0

So:

    current_xor ^ nums[n-1]

cancels out `nums[n-1]`.

Example:

    current_xor = a ^ b ^ c

Remove `c`:

    (a ^ b ^ c) ^ c

Since:

    c ^ c = 0

we get:

    a ^ b

Therefore, we can update the XOR in **O(1)** instead of recalculating it.

---

### Algorithm

1.  Calculate the XOR of all elements.
2.  Create the maximum possible `k` mask:

    maximumXor = (1 << maximumBit) - 1

3.  While there are still elements:
    - Find the `k` that maximizes the current XOR:

          k = current_xor ^ maximumXor

    - Add `k` to the answer.
    - Remove the last number from the current XOR:

          current_xor ^= nums[n - 1]

    - Decrease `n`.

4.  Return the answers.

---

### Example

    nums = [3, 2, 4]
    maximumBit = 3

First calculate:

    current_xor = 3 ^ 2 ^ 4
                = 5

Maximum mask:

    2^3 - 1 = 7

So:

    k = 5 ^ 7
      = 2

After the first query, remove `4`:

    current_xor = 5 ^ 4
                = 1

Next:

    k = 1 ^ 7
      = 6

Remove `2`:

    current_xor = 1 ^ 2
                = 3

Next:

    k = 3 ^ 7
      = 4

Answer:

    [2, 6, 4]

---

### Key XOR Properties

Remember:

    x ^ x = 0

    x ^ 0 = x

    x ^ x ^ x = x

XOR is also reversible:

    a ^ b = c

    c ^ b = a

This allows us to "remove" a number from a running XOR.

---

### Complexity

Initial XOR:

    O(n)

Each query:

    O(1)

There are `n` queries.

Total:

    Time: O(n)
    Space: O(n)   # output array

---

### Recognition Pattern

When you see:

- XOR of a changing subset
- Elements being added/removed
- Need to repeatedly calculate XOR

Think:

    Running XOR

Because XOR can remove an element:

    current_xor ^= element

When the problem asks for the maximum XOR under `maximumBit` bits, think:

    mask = (1 << maximumBit) - 1

and:

    k = current_xor ^ mask

### Main Insight

Two ideas work together:

    1. XOR mask → find the maximum possible k
    2. XOR cancellation → efficiently remove elements

The combination gives an **O(n)** solution.
