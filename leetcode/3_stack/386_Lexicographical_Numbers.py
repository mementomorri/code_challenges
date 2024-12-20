"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.



Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:

Input: n = 2
Output: [1,2]



Constraints:

    1 <= n <= 5 * 104
"""


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1
        while len(res) < n:
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1
        return res
