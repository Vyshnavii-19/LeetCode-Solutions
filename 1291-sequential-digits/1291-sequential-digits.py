class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        string = "123456789"
        
        # Iterate over the possible lengths of sequential digits
        for i in range(len(str(low)), len(str(high))+1):
            # Iterate over the possible starting positions
            for j in range(len(string)-i+1):
                # Check if the current substring converted to an integer is within the specified range
                if low <= int(string[j:j+i]) <= high:
                    ans.append(int(string[j:j+i]))

        return ans

