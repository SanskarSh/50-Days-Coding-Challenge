# Day 1 - Array and String Problems 📚

## Problem: [Rotate array](https://www.codingninjas.com/studio/problems/rotate-array_1230543)

### Problem Statement 📝
Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.

**Example:**
```
'arr '= [1,2,3,4,5]
'k' = 1  rotated array = [2,3,4,5,1]
'k' = 2  rotated array = [3,4,5,1,2]
'k' = 3  rotated array = [4,5,1,2,3] and so on.
```

### My Approach 💡
Slice the array into two parts: arr[k:] takes elements from index k to the end, forming the new beginning.
Concatenate in reverse order: + arr[0:k] appends elements from the start up to index k-1, creating the new end.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Rotate%20array/Solution.py)
