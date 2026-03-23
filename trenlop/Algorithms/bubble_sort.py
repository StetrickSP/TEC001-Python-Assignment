def bub_sort(nums):
    for i in range(len(nums)):
        print(i)
        try:
            if nums[i] >= nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                print(nums)
        except IndexError: return nums         

print(bub_sort([2,4,1,5]))