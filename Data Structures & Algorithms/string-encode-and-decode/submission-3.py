class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for st in strs:
            res += str(len(st)) + '#' + st
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delimiter = s.index('#', i)
            str_length = int(s[i:delimiter])
            str_start_index = delimiter + 1
            cur = s[str_start_index: str_start_index + str_length]
            res.append(cur)
            i = str_start_index + str_length

        return res