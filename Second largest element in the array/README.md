# Day 1 - Array and String Problems 📚

## Problem: [Second largest element in the array](https://www.codingninjas.com/studio/problems/second-largest-element-in-the-array_873375)

### Problem Statement 📝
You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

**Note:**

a) Duplicate elements may be present.

b) If no such element is present return -1.

**Example:**
```
Input: Given a sequence of five numbers 2, 4, 5, 6, 8.

Output:  6
```

### My Approach 💡

Remove duplicates and sort: temp = sorted(list(set(arr))) ensures uniqueness and order for accurate comparison. Return the penultimate element: return temp[len(temp)-2] if len(temp) > 1 else -1 handles cases with/without a second largest value.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Second%20largest%20element%20in%20the%20array/Solution.py)
