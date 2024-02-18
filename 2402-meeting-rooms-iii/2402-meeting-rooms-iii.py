from heapq import heappop, heappush
from operator import itemgetter

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = list(range(n))
        used_rooms = []
        meetings_per_room = [0] * n
 
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                room = heappop(available_rooms)
                heappush(used_rooms, (end, room))
            else:
                room_end, room = heappop(used_rooms)
                room_end += end - start
                heappush(used_rooms, (room_end, room))
            meetings_per_room[room] += 1

        max_index, max_value = max(enumerate(meetings_per_room), key=operator.itemgetter(1))
        return max_index