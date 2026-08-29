class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for letter_1, letter_2 in zip(s,t):
            dict_s[letter_1] = dict_s.get(letter_1,0) + 1
            dict_t[letter_2] = dict_t.get(letter_2,0) + 1

        return dict_s == dict_t


