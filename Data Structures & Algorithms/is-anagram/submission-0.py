class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for char in s: 
            letters[char] = letters.get(char , 0) +1

        for char in t: 
            if char not in letters: 
                return False
            letters[char] -= 1
            if letters[char] < 0: 
                return False
        return all(count == 0 for count in letters.values())
