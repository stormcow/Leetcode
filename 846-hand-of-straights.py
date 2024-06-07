class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort(reverse=True)
        while hand:
            if hand[0] == hand[-1] and groupSize != 1:
                return False
            group = []
            dups = []
            while len(group) != groupSize and hand:
                card = hand.pop()
                if group and card == group[-1]:
                    dups.append(card)
                elif not group or abs(card - group[-1]) == 1:
                    group.append(card)
                else:
                    return False

            hand.extend(dups[::-1])
        return True
