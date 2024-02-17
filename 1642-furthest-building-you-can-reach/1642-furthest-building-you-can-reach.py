class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        #This questions is tricky.
        #In order to reach nth position, we should have either sufficient bricks or 
        #sufficient ladders
        #But we only require 1 ladder to climb any height difference no matter how big it is.
        #-> what if we use a ladder for highest height differences and bricks for lowest height differences. seems like a good strategy. Turns out it is ! 
        #For every position, calculate top K height differences upto that position, where K = no of ladders.
        #Since we can cover these top K height differences using ladders, we only have to worry about covering remaining height difference with bricks!
        
        bricksArr = [0]
        cumBricks = [0]
        for i in range (1, len(heights)):
            curr = heights[i] - heights[i-1]
            if (curr <= 0): curr = 0
            bricksArr.append(curr)
            cumBricks.append(cumBricks[-1]+curr)
        
        heap = []
        maxKSum = []
        for i in range (0, ladders):
            heapq.heappush(heap, bricksArr[i])
            maxKSum.append(cumBricks[i])
        
        for i in range (ladders, len(heights)):
            if heap and bricksArr[i] > heap[0]:
                maxKSum.append(maxKSum[-1] -heap[0] + bricksArr[i])
                heapq.heappop(heap)
                heapq.heappush(heap, bricksArr[i])
            elif maxKSum:
                maxKSum.append(maxKSum[-1])
            if (cumBricks[i] - (maxKSum[i] if maxKSum else 0) - bricks > 0): return i-1
            
        return len(heights)-1