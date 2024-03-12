class Solution(object):
	def removeZeroSumSublists(self, head):
		"""
		Based on the Java solution explained here:
		https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/discuss/507108/Java-simple-O(n)-solution-with-explanation

		The main idea is that a cumulative sum will have repeating values when there are zero sum sublists. For e.g. if the original linked list is [1,2,3,-3,-1,1], then a cumulative sum with a prehead (an artificial 0 entry before the head) will be: [0, 1, 3, 6, 3, 2, 3]. As you can see a cumulative sum of 3 occurs three times. Which implies that the sublists [3,-3] and [-1,1] add up to zero.

		:param head: 
		:return: 
		"""
		prehead = ListNode(0)
		prehead.next = head
		current = head
		sum_map = {0: prehead} #cumulative sum map
		cumsum = 0
		while current:
			cumsum += current.val
			if cumsum in sum_map: #cumulative sum in the map
				prevmatch = sum_map[cumsum]
				walker = prevmatch.next
				wsum = cumsum
				while walker != current:
					wsum += walker.val
					# delete intermediate cumulative sums in zero sublist
					del sum_map[wsum] 
					walker = walker.next
				prevmatch.next = current.next #skip zero sum sublist entries
			else:
				sum_map[cumsum] = current
			current = current.next
		return prehead.next
