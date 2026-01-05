class Solution:
    def largest(self, arr):
        # code here
        maxx = 0
        
        for i in range(len(arr)):
            if(maxx < arr[i]):
                maxx = arr[i]
            
        return maxx
