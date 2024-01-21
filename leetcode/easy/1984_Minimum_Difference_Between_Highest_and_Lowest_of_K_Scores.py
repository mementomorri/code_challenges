"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

Example 1:

Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.

Constraints:

    1 <= k <= nums.length <= 1000
    0 <= nums[i] <= 105
"""

from typing import List
import sys


def minimum_difference(nums: List[int], k: int) -> int:
    if len(nums) == 1:
        return 0
    else:
        sorted_nums = sorted(nums)
        diff = sys.maxsize
        for i in range(len(sorted_nums) - k + 1):
            diff = min(diff, sorted_nums[i + k - 1] - sorted_nums[i])
        return diff


if __name__ == '__main__':
    print('nums=[90], k=1')
    res2 = minimum_difference(nums=[90], k=1)
    print(res2, res2 == 0, '\n')

    print('nums=[9, 4, 1, 7], k=2')
    res1 = minimum_difference(nums=[9, 4, 1, 7], k=2)
    print(res1, res1 == 2, '\n')

    print('nums=[87063,61094,44530,21297,95857,93551,9918], k=6')
    res1 = minimum_difference(nums=[87063, 61094, 44530, 21297, 95857, 93551, 9918], k=6)
    print(res1, res1 == 74560, '\n')
