class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        maxx = float('-inf')
        second_maxx = float('-inf')
        
        for x in arr:
            if maxx < x:
                maxx = x
        
        for x in arr:
            if second_maxx < x and x != maxx:
                second_maxx = x
                
        return second_maxx if second_maxx != float('-inf') else -1