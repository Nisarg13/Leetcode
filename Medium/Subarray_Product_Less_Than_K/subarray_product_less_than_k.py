from typing import List, Tuple


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> Tuple[int, List[List[int]]]:
        if k <= 1:
            return 0, []

        ans = left = 0
        curr = 1
        subarrays_set = set()

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

            # Generate subarrays including individual elements
            for i in range(left, right + 1):
                subarray = []
                for j in range(i, right + 1):
                    subarray.append(nums[j])
                    subarrays_set.add(tuple(subarray))

        # Convert the set to a list
        subarrays = [list(subarray) for subarray in subarrays_set]

        return ans, subarrays


solution = Solution()
result, subarrays = solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
print(result)
print(subarrays)
