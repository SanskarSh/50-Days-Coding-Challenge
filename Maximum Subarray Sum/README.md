# Day 6 - Array and String Problems 📚

## Problem: [Maximum Subarray Sum](https://www.codingninjas.com/studio/problems/630526)

### Problem Statement 📝
You are given an array 'arr' of length 'n', consisting of integers.

A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.

Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.

The sum of an empty subarray is 0.

**Example:**
```
Input: 'arr' = [1, 2, 7, -4, 3, 2, -10, 9, 1]
Output: 11
```
## My Approach 🛠️
Utilizing Kadane's Algorithm, the function iterates through the array, maintaining two variables - temp and max_val. temp represents the maximum subarray sum ending at the current index, while max_val tracks the maximum sum encountered so far. By dynamically updating these values, the algorithm efficiently finds the maximum subarray sum.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Maximum%20Subarray%20Sum/Solution.py)
