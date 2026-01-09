#User function Template for python3

class Solution:
    def removeDuplicate(self, arr):
        # code here
        s = set()
        n = len(arr)
        new_arr = []

        for i in range(n):
            if arr[i] not in s:
                s.add(arr[i])
                new_arr.append(arr[i])
                
        return new_arr
    

