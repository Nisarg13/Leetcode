# Find Subarray with Largest Sum of Length k

This Python code snippet provides a solution to find the sum of the subarray with the largest sum of length `k` in an integer array.

## Problem Description

Given an integer array `nums` and an integer `k`, the goal is to find the sum of the subarray with the largest sum whose length is exactly `k`.

## Approach

The code uses a sliding window approach to find the subarray with the largest sum of length `k`. Here's a brief overview of the approach:

1. Initialize a variable `curr` to store the sum of the first `k` elements in the array. This is done by iterating through the array from index 0 to `k-1` and adding each element to `curr`.

2. Initialize a variable `ans` to `curr`. This variable will keep track of the maximum sum found during the iterations.

3. Iterate through the array starting from index `k`. For each new element at index `i`, add it to `curr` and subtract the element that was `k` steps back (at index `i - k`) from `curr`.

4. Update the `ans` variable by taking the maximum of the current `ans` and `curr` at each step. This way, you ensure that `ans` always contains the maximum sum of a subarray of length `k`.

5. Finally, return the value of `ans`, which represents the sum of the subarray with the largest sum of length `k`.

## Code Usage

You can use the `find_best_subarray` function to find the sum of the subarray with the largest sum of length `k` in a given integer array.

```python
print(find_best_subarray([1, 2, 3, 4], 2))
```

This code will output the sum of the subarray with the largest sum of length `2` for the provided example.

Feel free to integrate this code into your Python projects for similar tasks.