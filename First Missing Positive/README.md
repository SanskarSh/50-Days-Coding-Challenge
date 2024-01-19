# Day 2 - Array and String Problems 📚

## Problem: [First Missing Positive](https://www.codingninjas.com/studio/problems/first-missing-positive_699946)

### Problem Statement 📝
You are given an array 'ARR' of integers of length N. Your task is to find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can have negative numbers as well.

For example, the input [3, 4, -1, 1] should give output 2 because it is the smallest positive number that is missing in the input array.

**Example:**
```
Sample Input :
1
5
3 2 -6 1 0

Sample Output:
4
```

### My Approach 💡
Filter and sort positive, iterate through gaps to find: the first missing positive value.
Handle empty or non-starting-at-1 arrays: return 1.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/First%20Missing%20Positive/Solution.py)
