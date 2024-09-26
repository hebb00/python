def searchInsert(nums, target):
    low = 0
    high = len(nums)- 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if nums[mid]< target:
            low = mid + 1
        elif nums[mid]> target:
            high = mid - 1
        else:
            return mid
    return low





if __name__ == "__main__":
    print(searchInsert([0,3,5,7],2))
