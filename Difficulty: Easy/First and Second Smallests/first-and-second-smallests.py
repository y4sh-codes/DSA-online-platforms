class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        mini = float('inf')
        second_mini = float('inf')
        
        if (len(arr)<2):
            
            return [-1]
        
        for x in arr:
            if mini > x:
                mini = x
        
        for x in arr:
            if second_mini > x and x!=mini:
                second_mini = x
                
        return [mini,second_mini] if second_mini != float('inf') else [-1]