1class Solution:
2    def romanToInt(self, s: str) -> int:
3        romanMap = {
4            "I" : 1,
5            "V" : 5,
6            "X" : 10,
7            "L" : 50,
8            "C" : 100,
9            "D" : 500,
10            "M" : 1000        
11        }
12
13        total = 0
14        n = len(s)
15
16        for i in range(n):
17            current = romanMap[s[i]]
18
19            if i+1 < n and current < romanMap[s[i+1]]:
20                total = total - current
21            else:
22                total = total + current
23
24        return total
25