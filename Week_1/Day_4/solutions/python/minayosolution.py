def move_zeroes(nums):
    
    non_zero_index = 0
    
   
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    
    
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0


nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1) 

nums2 = [0]
move_zeroes(nums2)
print(nums2)  