class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adjList = defaultdict(list)
        res = set([0, firstPerson])
        visited = {0: 0, firstPerson: 0}
        for x, y, time in meetings:
            adjList[x].append((y, time))
            adjList[y].append((x, time))
        queue = [(firstPerson, 0), (0, 0)]
        while queue:
            p1, t1 = queue.pop()
            for p2, t2 in adjList[p1]:
                if t2 < t1 or (p2 in visited and t2 >= visited[p2]):
                    continue
                res.add(p2)
                visited[p2] = t2
                queue.append((p2, t2))
        return list(res)
        
            
            
        