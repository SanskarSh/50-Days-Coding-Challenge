# Day 3 - Array and String Problems 📚

## Problem: [Pair Sum](https://www.codingninjas.com/studio/problems/pair-sum_1171154)

### Problem Statement 📝
You are given an array/list ‘ARR’ consisting of ‘N’ distinct integers arranged in ascending order. You are also given an integer ‘TARGET’. Your task is to count all the distinct pairs in ‘ARR’ such that their sum is equal to ‘TARGET’.

**Example:**
```
Let ‘ARR’ = [1 2 3] and ‘TARGET’ = 4. Then, there exists only one pair in ‘ARR’ with a sum of 4 which is (1, 3). 
(1, 3) and (3, 1) are counted as only one pair.
```

## My Approach 🛠️

To tackle the problem of finding pairs in an ascending order array with a given target sum, I initially implemented a straightforward solution using nested loops to iterate through each element in the array. Here's a breakdown of my approach:

1. **Initialization:**
   - I started by initializing an empty set called `result` to keep track of the distinct pairs.
   - I also initialized a variable `count` to store the count of distinct pairs.

2. **Nested Loop Iteration:**
   - I used two nested loops to iterate through each pair of elements in the array (`i` and `j`).
   - I ensured that the pairs (i, j) and (j, i) were considered as the same pair to avoid duplicates.

3. **Condition Check:**
   - Checked if the sum of the current pair (`i + j`) is equal to the target.
   - Also, confirmed that `i` and `j` are not the same elements to avoid counting pairs like (1, 1).

4. **Updating Count and Set:**
   - If the condition was met, I checked if both `i` and `j` were not already in the `result` set to ensure uniqueness.
   - If not, I incremented the `count` and added both elements to the set.

5. **Final Result:**
   - Returned the final count if it was greater than zero, indicating the presence of distinct pairs.
   - Otherwise, returned -1 to signify that no such pair was found.

2. **Returning the count:**
   - The final value of my `count` variable represented the minimum number of elements that needed to be removed to ensure that the array contained only distinct elements.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/[Pair%20Sum/Solution.py)
