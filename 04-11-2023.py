class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        t=0
        # find max value for the left
        for i in left:
            t=max(t,i)
        # find min value for the right
        for i in right:
            t=max(t,n-i)
        return t
    # one line answer
    class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = max(max(left) if left else 0,n-min(right) if right else 0)
        return ans
        
        
