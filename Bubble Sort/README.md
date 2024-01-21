# Day 4 - Array and String Problems 📚

## Problem: [Bubble Sort](https://www.codingninjas.com/studio/problems/bubble-sort_980524)

### Problem Statement 📝
Bubble Sort is one of the sorting algorithms that works by repeatedly swapping the adjacent elements of the array if they are not in sorted order.

You are given an unsorted array consisting of N non-negative integers. Your task is to sort the array in non-decreasing order using the Bubble Sort algorithm.

## My Approach 🛠️
The provided Python implementation of the bubble sort algorithm follows a slightly unconventional approach. The algorithm employs a while True loop and a count variable to track whether any swaps were made during an iteration. If no swaps occur, the algorithm assumes that the list is already sorted and terminates early. While this approach differs from the conventional nested loop structure, it aims to optimize the algorithm by reducing unnecessary iterations when the list is already sorted.

Feel free to explore and compare this approach with the more standard implementation provided in the comments for a better understanding of bubble sort.

### Code 🚀
[Solution.py](https://github.com/SanskarSh/50-Days-Coding-Challenge/blob/main/Bubble%20Sort/Solution.py)
