class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = Counter(nums)
        
        # Step 2: Use the most_common method to get the top k elements
        most_common = count.most_common(k)
        
        # Step 3: Extract just the elements (ignoring the counts)
        return [item[0] for item in most_common]