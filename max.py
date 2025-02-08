def allMaxSubArrays(nums):
    current_sum=0
    max_sum=nums[0]
    for i in range(len(nums)):
        if current_sum<0:
            current_sum=0
            start=i
        current_sum+=nums[i]
        if current_sum>max_sum:
            max_sum=current_sum
            end=i
    return max_sum, nums[start:end+1]            




nums =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarrays = allMaxSubArrays(nums)
print("Max Sum:", max_sum)  
print("All Subarrays:", subarrays)