def removeDuplicates( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        j = 0
        for i in range(len(nums)):
            print(j,"bfr")   
            if nums[i] not in nums[:j]:
                nums[j]=nums[i]
                j = j+1
            print(j) 
        
            return len(nums)
        
if __name__ == "__main__":
    print(removeDuplicates([4,4,4,5]))
            
