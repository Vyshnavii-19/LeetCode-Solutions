class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dic1 = Counter(students)
        dic2 = Counter(sandwiches)
        for c in sandwiches:
            if dic1[c] != 0:
                dic1[c] -= 1
            else:
                break
        return sum(dic1.values())