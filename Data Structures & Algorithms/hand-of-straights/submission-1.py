class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = {}
        for card in hand:
            freq[card] = 1 + freq.get(card, 0)


        for card in sorted(hand):
            c = freq[card]
            if c == 0:
                continue
            for nxt in range(card, card + groupSize):
                if freq.get(nxt, 0) < c:
                    return False
                freq[nxt] -= c
        
        return True
