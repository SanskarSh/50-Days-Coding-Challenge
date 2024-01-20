# Day 3 - Array and String Problems 📚

## Problem: [Make Unique Array](https://www.codingninjas.com/studio/problems/make-unique-array_920329)

### Problem Statement 📝
You are given an array ‘ARR’ of size ‘N,’ and you have to tell the minimum number of elements that need to be removed such that the array contains all distinct elements. More formally, there should not be any ‘I’ and ‘J’ such that ‘I’ != ‘J’ and ‘ARR’[‘I’] = ‘ARR’[‘J’].

**Example:**
```
Given ‘N’ = 4,
'ARR' = { 1, 2, 1, 2}
Then the answer is 2 because 1 and 2 are repeated once therefore we need to remove 2 elements.
```

## My Approach 🛠️

To tackle this problem efficiently, I decided to use a set to keep track of the unique elements I've encountered so far. I started by initializing an empty set called `unique_elements` and a counter variable `count` to keep track of the number of elements that needed to be removed.

1. **Iterating through the array:**
   - For each element `i` in my array `ARR`:
     - I checked whether `i` was already present in my `unique_elements` set.
       - If it was, I knew I needed to remove this element, so I incremented my `count` variable.
       - If it wasn't, I added `i` to my `unique_elements` set.

2. **Returning the count:**
   - The final value of my `count` variable represented the minimum number of elements that needed to be removed to ensure that the array contained only distinct elements.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/[Make%20Unique%20Array/Solution.py)
