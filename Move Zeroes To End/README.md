# Day 6 - Array and String Problems 📚

## Problem: [Move Zeroes To End](https://www.codingninjas.com/studio/problems/interview-shuriken-41-move-zeroes-to-end_240143)

### Problem Statement 📝
Given an unsorted array of integers, you have to move the array elements in a way such that all the zeroes are transferred to the end, and all the non-zero elements are moved to the front. The non-zero elements must be ordered in their order of appearance.

**Example:**
```
If the input array is: [0, 1, -2, 3, 4, 0, 5, -27, 9, 0]
Then the output array must be: [1, -2, 3, 4, 5, -27, 9, 0, 0, 0].
```
## My Approach 🛠️
1. *Two-Pointer Technique:*
    - Use two pointers to iterate through the array.
    - One pointer (i) scans the array from left to right.
    - Another pointer (j) tracks the position for non-zero elements.
2. *Preserving Order:*
    - Move non-zero elements to the position indicated by the j pointer.
    - Increment the j pointer for the next position of a non-zero element.
3. *Zeroes at the End:*
    - Fill remaining positions from the j pointer onward with zeroes.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Move%20Zeroes%20To%20End/Solution.py)
