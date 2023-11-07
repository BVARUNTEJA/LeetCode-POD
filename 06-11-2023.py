import heapq
class SeatManager:

    def __init__(self, n: int):
        # constructor intially all seats are not reserved
        # heap is used to keep ths array sorted 
        # for adding & removing the number it just cost log2(n)
        self.seat=list(range(1,n+1))
        self.s=set()

    def reserve(self) -> int:
        # assign the seat with lowest number and return it
        a=heapq.heappop(self.seat)
        self.s.add(a)
        return a

    def unreserve(self, seatNumber: int) -> None:
        # unreserve the seat with seatnumber
        if seatNumber in self.s:
            self.s.remove(seatNumber)
            heapq.heappush(self.seat,seatNumber)
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
