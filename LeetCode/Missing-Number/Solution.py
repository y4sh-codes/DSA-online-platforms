1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        expected_sum = (n*(n+1))//2
5        sum = 0
6
7        for x in nums:
8            sum = sum + x
9        
10        return expected_sum - sum