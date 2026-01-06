#User function Template for python3

class Solution:
    def countArray (self, arr, x) : 
        #Complete the function
        freq = {}
    
        average = 0
        n = len(arr)
        arr2 = [0]*n
        
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
            
        for i in range(n):
            average = (arr[i]+x)//2
            
            arr2[i] = freq.get(average, 0)
            
        return arr2
        