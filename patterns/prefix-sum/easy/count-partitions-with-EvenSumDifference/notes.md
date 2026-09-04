Pattern:

Prefix Sum -- > Used when a problem asks about splitting an array into a left part and a right part, then comparing their sums.

Recognition clues:

Look for words like:

split / partition
left and right
before / after an index
sum of left side
sum of right side
difference between two sides
count valid partitions

My first approach : Nested loops

Time Complexity: O(n2)

Optimized Approach :

Key Idea:
The question asks about |left - right| is even ?

- So when those numbers subtract is even ? --> leftSum and rightSum have the same parity (even - even = even) and (odd - odd = even)
- For every possible split, you calculate: (leftSum - rightSum) is even ?
  ( rightSum = total_sum - leftSum) -- > leftSum - (total_sum - leftSum) = 2 \* leftSum is always is even ,
  so the parity of 2 \* leftSum - totalSum only depends on total_sum, if total_sum is even , the parity will be even ,otherwise odd
