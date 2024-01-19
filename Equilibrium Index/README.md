# Day 2 - Array and String Problems 📚

## Problem: [Equilibrium Index](https://www.codingninjas.com/studio/problems/equilibrium-index_893014)

### Problem Statement 📝
You are given an array Arr consisting of N integers. You need to find the equilibrium index of the array.

An index is considered as an equilibrium index if the sum of elements of the array to the left of that index is equal to the sum of elements to the right of it.

**Note:**

1. The array follows 0-based indexing, so you need to return the 0-based index of the element.
2. Note that the element at the equilibrium index won’t be considered for either left sum or right sum.
3. If there are multiple indices which satisfy the given condition, then return the left-most index i.e if there are indices i,j,k…. which are equilibrium indices, return the minimum among them
4. If no such index is present in the array, return -1.

### My Approach 💡
Calculate prefix and suffix sums for each element: Efficiently track cumulative sums from both ends of the array.
Find index where those sums are equal: Indicates equilibrium where left and right sums balance.

### Code 🚀
[Solution.cpp](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Equilibrium%20Index/Solution.cpp)
