#user input
def twoSum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        needed = target - nums[i]
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[nums[i]] = i


# ---- Taking Input From User ----
nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter target: "))

result = twoSum(nums, target)

print("Output:", result)


#leetcode logic
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in seen:
                return [seen[needed], i]
            
            seen[nums[i]] = i