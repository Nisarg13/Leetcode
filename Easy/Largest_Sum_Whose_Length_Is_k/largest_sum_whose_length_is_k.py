def find_best_subarray(nums, k):
    curr = 0
    start_idx = 0  # Initialize the start index of the best subarray
    for i in range(k):
        curr += nums[i]

    ans = curr
    end_idx = k - 1  # Initialize the end index of the best subarray
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        if curr > ans:
            ans = curr
            start_idx = i - k + 1  # Update the start index of the best subarray
            end_idx = i  # Update the end index of the best subarray

    best_subarray = nums[start_idx:end_idx + 1]  # Extract the best subarray
    return ans, best_subarray

max_sum, subarray = find_best_subarray([1, 2, 3, 4], 2)
print("Maximum Sum:", max_sum)
print("Subarray with Maximum Sum:", subarray)
