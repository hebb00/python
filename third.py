class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=[]
        cmn=""
        equal= 0
        tem=0
        for i in range(len(strs)-1):
            for j in range(len(strs[i])):
                for t in range(len(strs[i+1])):
                    
                    if strs[i][j] == strs[i][t]:
                         cmn+=strs[i][j] 
                         break
              
              
            prefix.append(cmn)
        
        res = min(len(ele) for ele in  prefix)
        for ele in range(len(prefix)-1):
            if res == len(prefix[ele]):
                x = prefix[ele]
        if x:
            return x
        else:
             return ""
     
    

    






        