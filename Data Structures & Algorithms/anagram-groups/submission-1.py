class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            counts = [0] * 26
            for ch in string:
                counts[ord(ch) - ord('a')] += 1
            anagrams[tuple(counts)].append(string)
        
        return list(anagrams.values())
                
        