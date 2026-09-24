class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            x = 1
            for j in range(len(nums)):
                if i != j:
                    x = x * nums[j]
            result.append(x)
        return result