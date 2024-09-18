# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 



class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=''
        preArr = []

        if len(strs) == 0: 
            return ''
        elif len(strs) == 1:
            return strs[0]

        for i in range(len(strs)-1):
  
            if len(strs[i]) <= len(strs[i+1]):
                length = len(strs[i])
            else:
                length = len(strs[i+1])
            
            t=0
            while t < length:
                if strs[i][t] == strs[i+1][t]:    
                    prefix+=strs[i][t]
                else:
                    break
                
                t+=1

            preArr.append(prefix)
            prefix=''
     
        if len(preArr) == 0:
            return ""
        else: 
            return   min(preArr)
 
   

        