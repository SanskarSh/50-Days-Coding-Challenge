# Day 7 - Array and String Problems 📚

## Problem Links 🔗

[codingninjas](https://www.codingninjas.com/studio/problems/print-pascal-s-triangle_6917910)
[leetcode](https://leetcode.com/problems/set-matrix-zeroes/)

### Problem Statement 📝

You are given an integer ‘N’. You need to return the first ‘N’ rows of Pascal’s triangle.

**Example:**

```
Input:
N = 4

Output:
1
1 1
1 2 1
1 3 3 1

Explanation: The output matrix has the first four rows of Pascal’s Triangle.
```

## My Approach 🛠️

I used a list to store the rows of the Pascal's triangle. I used the previous row to calculate the current row. I used the formula `C(n, r) = C(n-1, r-1) + C(n-1, r)` to calculate the current row. I used a nested loop to iterate through the rows and columns of the triangle and stored the values in the list.

### Code 🚀

[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Pascal’s%20Triangle/Solution.py)
