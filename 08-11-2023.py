class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        xmin=abs(sx-fx)
        ymin=abs(sy-fy)
        dig=min(xmin,ymin)
        xmin-=dig
        ymin-=dig
        dig+=(xmin+ymin)
        if dig==0:
            if t==1:return False
            else:
                return True
        return t>=dig
