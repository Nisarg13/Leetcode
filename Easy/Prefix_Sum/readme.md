# Subarray Sum Checker

## Overview

This Python script, `subarray_sum_checker.py`, offers a solution to the problem of determining whether the sum of subarrays in an integer array `nums` falls below a specified limit for a set of queries. The approach used in this script employs the prefix sum technique to efficiently compute subarray sums and compare them with the given limit.

## Approach

The script follows these steps to solve the problem efficiently:

1. **Prefix Sum Calculation**: The first step involves calculating the prefix sum of the input array `nums`. The prefix sum at each index `i` represents the sum of elements from the beginning of the array up to index `i`. This precomputation optimizes the subsequent query processing.

2. **Query Processing**: For each query `[x, y]` in the `queries` list, the script calculates the sum of the subarray from index `x` to `y` using the prefix sum. The sum is computed as `prefix[y] - prefix[x] + nums[x]`.

3. **Comparison with Limit**: The sum obtained from each query is then compared with the specified `limit`. If the sum is less than the `limit`, the result for that query is `True`, indicating that the sum falls below the limit. Otherwise, the result is `False`, indicating that the sum is equal to or exceeds the limit.

4. **Building the Result List**: The results of each query are stored in a list called `ans`, which is returned as the final output.

## Usage

To use this script, follow these steps:

1. Clone this repository or download the `subarray_sum_checker.py` script.

2. Ensure that you have Python 3 installed on your system.

3. Modify the `nums` list, `queries` list, and `limit` variable in the script to suit your requirements.

4. Run the script using the following command:

   ```
   python subarray_sum_checker.py
   ```

5. The script will execute and print a boolean array representing the answers to each query. Each boolean value indicates whether the sum of the corresponding subarray in the `queries` list falls below the specified `limit`.

## Input

The input to the script includes the following variables:

- `nums`: A list of integers representing the input array.

- `queries`: A list of queries, where each query is a list `[x, y]` representing a subarray from index `x` to `y` (inclusive) that needs to be checked.

- `limit`: An integer representing the maximum allowed sum for a subarray.

## Output

The script produces a list of Boolean values as output, where each value corresponds to a query and indicates whether the sum of the subarray specified in that query falls below the `limit`.

## Example

```python
nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

result = answer_queries(nums, queries, limit)
print(result)  # Output: [True, False, True]
```

## License

This code is provided under the MIT License, allowing you to freely use and modify it for your needs. For more details, refer to the [LICENSE](LICENSE) file.

## Contributing

Contributions to this project are welcome. If you have any improvements or suggestions, please fork the repository, make your changes, and submit a pull request. We appreciate community contributions.

---

Feel free to customize this README file further if needed, adding more information or details about the problem statement and how your solution works.