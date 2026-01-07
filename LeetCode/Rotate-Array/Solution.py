1class Solution:
2    def reverse(self, arr : list, low : int, high : int):
3
4        while (low<high):
5            arr[low], arr[high] = arr[high], arr[low]
6            low = low + 1
7            high = high - 1
8
9    def rotate(self, nums: List[int], k: int) -> None:
10        """
11        Do not return anything, modify nums in-place instead.
12        """
13        n = len(nums)
14        k = k % n
15        
16        self.reverse(nums, 0, n-1)
17        self.reverse(nums, 0, k-1)
18        self.reverse(nums, k, n-1)
19        
20
21        