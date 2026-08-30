class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        
        for letter_s, letter_t in zip(s, t):
            count_s[letter_s] = count_s.get(letter_s,0) + 1
            count_t[letter_t] = count_t.get(letter_t,0) + 1
        
        return count_s == count_t