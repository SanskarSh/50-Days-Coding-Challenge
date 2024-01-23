# Day 6 - Array and String Problems 📚

## Problem: [Search In Rotated Sorted Array](https://www.codingninjas.com/studio/problems/630450)

### Problem Statement 📝
Aahad and Harshit always have fun by solving problems. Harshit took a sorted array consisting of distinct integers and rotated it clockwise by an unknown amount. For example, he took a sorted array = [1, 2, 3, 4, 5] and if he rotates it by 2, then the array becomes: [4, 5, 1, 2, 3].

After rotating a sorted array, Aahad needs to answer Q queries asked by Harshit, each of them is described by one integer Q[i]. which Harshit wanted him to search in the array. For each query, if he found it, he had to shout the index of the number, otherwise, he had to shout -1.

For each query, you have to complete the given method where 'key' denotes Q[i]. If the key exists in the array, return the index of the 'key', otherwise, return -1.

## My Approach 🛠️
1. *Binary Search Modification:* Implement a binary search algorithm tailored for a rotated sorted array.
2. *Determining Sorted Part:* Check which part of the array is sorted.
3. *Target Comparison:* Based on the sorted part, compare the target with the elements in that segment to determine the search direction.
4. *Search Iteration:* Repeat the process until the target is found or the search space is exhausted.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Search%20In%20Rotated%20Sorted%20Array/Solution.py)
