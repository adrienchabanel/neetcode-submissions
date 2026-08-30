class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_of_anagrams = {}
        for word in strs:
            count_letters = [0] * 26
            for letter in word:
                count_letters[ord(letter) - ord('a')] += 1
            dict_of_anagrams.setdefault(tuple(count_letters),[]).append(word)
        return list(dict_of_anagrams.values())