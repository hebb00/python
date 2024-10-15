def removeDuplicates( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        j = 1
        i = 0

        while i < len(nums):
            while j < len(nums)-i:
                if nums[i] == nums[j]:
                    nums.pop(j)
                    break
                j+= 1
            i+= 1
       
        return len(nums)
        
if __name__ == "__main__":
    print(removeDuplicates([4,4,4,5]))
            
