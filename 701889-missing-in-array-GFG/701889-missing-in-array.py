class Solution:
    def missingNum(self, arr):
        n = len(arr)+1
        expected_sum = (n*(n+1))//2
        sum = 0
        
        for x in arr:
            sum = sum + x
        return expected_sum - sum