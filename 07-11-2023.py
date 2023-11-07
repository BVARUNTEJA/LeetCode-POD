class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # calculate the lenght 
        n=len(dist)
        # calculate the time required for i monster
        for i in range(n):
            dist[i]=(dist[i]+speed[i]-1)//speed[i]
        # sort the distant
        dist.sort()
        for i in range(n):
            # if time is greater than weapon
            if i>=dist[i]:return i
        return n
