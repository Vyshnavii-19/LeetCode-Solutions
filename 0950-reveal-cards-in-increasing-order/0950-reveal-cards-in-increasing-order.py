class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue=collections.deque()
        for card in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(card)
        return queue