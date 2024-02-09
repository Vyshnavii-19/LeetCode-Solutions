class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Distinct positive integers
        # We want to find the largest subset `result` such that for any `result[i]` and `result[j]`,
        # either `result[i] % result[j] == 0` or `result[j] % result[i] == 0`.

        # If the values are sorted in each subset: if a | b, and b | c, then a | c.
        # So this problem is similar to the Longest Increasing Subsequence (LIS) problem.

        # Suppose we know the longest sequence ending with each number thus far.
        # Then, when we look at number x, we look at prior values that divide x.
        # We pick the set with the longest sequence and append x to it.

        nums.sort()  # Sort the input numbers in ascending order.

        # Initialize dictionaries to store the parent and length of the subsets.
        parent = {}  # Stores the parent of each number in the longest subset ending with that number.
        length = {}  # Stores the length of the longest subset ending with each number.
        result_end = nums[0]  # Store the ending of the result subset.

        # Iterate through each number in the sorted list of numbers.
        for num in nums:
            best = None  # Initialize the best number that divides `num`.

            # Iterate through previous numbers to find the best divisor for `num`.
            for prev_num in nums:
                # If the double of `prev_num` is greater than `num`, break the loop as we only need to check smaller divisors.
                if 2 * prev_num > num:
                    break

                # Check if `prev_num` divides `num` and if it results in a longer subset.
                if num % prev_num == 0 and length[prev_num] > length.get(best, -1):
                    best = prev_num

            # If a valid best divisor is found, update the parent and length for the current number `num`.
            if best:
                parent[num] = best
                length[num] = length[best] + 1
            else:
                # If no valid divisor is found, set the length of the current number to 1.
                length[num] = 1

            # Update the ending of the result subset if the length of the subset ending with `num` is greater.
            if length[num] > length[result_end]:
                result_end = num

        # Reconstruct the result list using the parent map.
        result = []  # Initialize the result list.
        while result_end:
            result.append(result_end)  # Append the current number to the result list.
            result_end = parent.get(result_end, None)  # Update the current number to its parent.

        # Return the result list in descending order.
        return result[::-1]
