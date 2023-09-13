def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    subarray_start = subarray_end = -1
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1

        if right - left + 1 > ans:
            ans = right - left + 1
            subarray_start = left  # Update the start index of the subarray
            subarray_end = right  # Update the end index of the subarray

    if subarray_start != -1 and subarray_end != -1:
        return ans, nums[subarray_start:subarray_end + 1]
    else:
        return 0, []


print(find_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
