from collections import defaultdict
from typing import DefaultDict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map: list[int] = [0 for _ in range(26)]
        un_order_map: list[int] = [0 for _ in range(26)]

        for c in s:
            if c in order:
                order_map[ord(c) - 97] += 1
            else:
                un_order_map[ord(c) - 97] += 1

        return "".join([c * order_map[ord(c) - 97] for c in order]) + "".join(
            [chr(index + 97) * count for index, count in enumerate(un_order_map)]
        )