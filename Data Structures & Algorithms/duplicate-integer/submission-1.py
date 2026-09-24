class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lib = set()
        for n in nums: 
            if n in lib: 
                return True 
            else: 
                lib.add(n)
        return False