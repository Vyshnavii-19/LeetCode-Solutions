class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(set)
        if n == 2: return edges[0]
        total_edges = 0
        for n1,n2 in edges:
            adj_list[n1].add(n2)
            adj_list[n2].add(n1)
            total_edges += 2
        
        queue = deque()
        for node in adj_list:
            if len(adj_list[node]) == 1:
                queue.append(node)
        while queue:
            q_size = len(queue)
            for _ in range(q_size):
                node = queue.popleft()
                neighbor = adj_list[node].pop()
                del adj_list[node]
                adj_list[neighbor].remove(node)
                total_edges -= 2
                if len(adj_list[neighbor]) == 1: queue.append(neighbor)
            if total_edges <= 2: return list(adj_list.keys())
        return [0]