class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        j=0
        for i in range(1,n+1):
            # reached the end
            if j>=len(target):
                break
            # first append the number to check
            ans.append('Push')
            if target[j]==i:
                j+=1
                # if number are equal then no need to pop the number
                continue
            #  pop the number which we append recently
            ans.append('Pop')
        return ans

