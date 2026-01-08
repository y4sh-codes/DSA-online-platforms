1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        
6        n = len(nums)
7        left = 0
8
9        for right in range(1, n):
10            if nums[left] != nums[right]:
11                left = left+1
12                nums[left] = nums[right]
13        return left + 1