def move_zeros(nums):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1  
        i += 1

    while j < len(nums):
        nums[j] = 0
        j += 1

    return nums


nums = [0,1,0,3,12]

nums1 = [1,2,3,0,5,0,6,0,7,8,9,0]
print(move_zeros(nums1))