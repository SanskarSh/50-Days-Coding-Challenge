# Day 5 - Array and String Problems 📚

## Problem: [Insertion Sort](https://www.codingninjas.com/studio/problems/insertion-sort_3155179)

### Problem Statement 📝
You are given ‘N’ integers in the form of an array ‘ARR’. Print the sorted array using the insertion sort.

**Example:**
```
Let ‘ARR’ be: [1, 4, 2]
The sorted array will be: [1, 2, 4].
```

## My Approach 🛠️
- *Standard Logic:* The algorithm iteratively compares adjacent elements, swapping them if they are in the wrong order, following the conventional insertion sort approach.

- *Optimization:* After a swap, the algorithm recursively applies insertion sort to the sorted prefix of the list up to the current position, efficiently inserting the current element. This approach combines the power of recursion with the simplicity of insertion sort.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Insertion%20Sort/Solution.py)
