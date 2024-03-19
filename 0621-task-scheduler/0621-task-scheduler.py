from queue import PriorityQueue
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = Counter(tasks)
        return max((n+1)*(max(l.values())-1) + len([x for x in l.values() if x == max(l.values())]) , len(tasks))
        