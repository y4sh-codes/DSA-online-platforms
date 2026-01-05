class Solution:
    def reverseArray(self, arr):
        # code here
        temp = 0
        n = len(arr)
        
        for i in range(n//2):
            
            temp = arr[i]
            arr[i] = arr[n-i-1]
            arr[n-i-1] = temp
        
        
        
        
        