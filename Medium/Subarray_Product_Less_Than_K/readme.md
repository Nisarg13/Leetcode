# Count Subarrays with Product Less Than K

This Python code snippet provides a solution to count the number of subarrays where the product of all elements in the subarray is strictly less than a given threshold `k`. It also includes logic to generate unique subarrays, including individual elements.

## Problem Description

Given an array of positive integers `nums` and an integer `k`, the goal is to count the number of subarrays in which the product of all elements is strictly less than `k`.

## Approach

The code uses a sliding window approach to find subarrays with a product less than `k`. Here's a brief overview of the approach:

1. Initialize variables `ans`, `left`, and `curr` to 0. `ans` stores the count of valid subarrays, `left` represents the left pointer of the window, and `curr` is used to calculate the product of elements in the current window.

2. Iterate through the `nums` array using a right pointer (`right`) to expand the window.

3. Calculate the product of elements in the current window using `curr *= nums[right]`.

4. Use a while loop to ensure that the product of elements in the window is less than `k`. If it becomes greater than or equal to `k`, shrink the window by incrementing `left` and dividing `curr` by `nums[left]`.

5. Update the `ans` variable by adding the count of valid subarrays found during each iteration.

6. Generate subarrays, including individual elements, by nested looping from `left` to `right`. Add these subarrays to a set (`subarrays_set`) to ensure uniqueness.

7. Finally, convert the set of subarrays to a list to provide the desired output.

## Code Usage

You can use the `numSubarrayProductLessThanK` method provided by the `Solution` class to find the count of subarrays and the list of unique subarrays with products less than `k`.

```python
solution = Solution()
result, subarrays = solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
print("Number of subarrays with product less than k:", result)
print("List of subarrays with product less than k:", subarrays)
```

This code will produce the desired result, counting the subarrays and listing them as described in your example.