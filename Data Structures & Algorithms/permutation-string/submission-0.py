class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = [0] * 26
        s2_chars = [0] * 26
        for char in s1:
            s1_chars[ord(char) - ord('a')] += 1
        
        left = 0
        for right, s2_char in enumerate(s2):
            idx = ord(s2_char) - ord('a')
            s2_chars[idx] += 1
            
            while s2_chars[idx] > s1_chars[idx]:
                s2_chars[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                return True

        return False