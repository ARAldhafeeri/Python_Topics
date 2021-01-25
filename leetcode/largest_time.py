# Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

# Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.

 

# Example 1:

# Input: A = [1,2,3,4]
# Output: "23:41"
# Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
# Example 2:

# Input: A = [5,5,5,5]
# Output: ""
# Explanation: There are no valid 24-hour times as "55:55" is not valid.

from itertools import permutations   
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr = sorted(arr)
        perm = permutations(arr, 4)
        ans = []
        temp = ''
        count = 0
        for i in perm:
            for j in i:
                if count == 2:
                    temp += ":"
                    temp += str(j)
                else:
                    temp += str(j)
                count += 1
            count = 0
            ans.append(temp)
            temp = ''
        for i in range(0, len(ans)):
            flag1 = int(ans[i][0] + ans[i][1]) > 23
            flag2 = int(ans[i][3] + ans[i][4]) > 59
            if  flag1 or flag2:
                ans[i] = 'NAN'
        ans = list(filter(('NAN').__ne__, ans))
        if not ans:
            return ""
        maxHour = 0
        maxMinutes = 0
        maxIndex = 0
        for i in range(0, len(ans)):
            flag2 = maxMinutes < int(ans[i][3] +ans[i][4])
            flag1 =  maxHour <= int(ans[i][0] +ans[i][1] )
            if flag1:
                flag2 = True
            if flag1 & flag2:
                maxHour = int(ans[i][0] +ans[i][1])
                maxMinutes = int(ans[i][3] +ans[i][4])
                maxIndex = i
        return ans[maxIndex]
        
       
        
                

    