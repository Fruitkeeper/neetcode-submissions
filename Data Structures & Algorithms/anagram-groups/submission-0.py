class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs: 
            word_ordered = "".join(sorted(word)) 
            if word_ordered not in anagrams: 
                anagrams[word_ordered] = []
            anagrams[word_ordered].append(word)
        
        return list(anagrams.values())
                