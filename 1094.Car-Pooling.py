class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(n)
        passChange = [0] * 1001
        for t in trips:
            numPass, start, end = t
            passChange[start] += numPass
            passChange[end] -= numPass
            
        curPass = 0
        for i in range(1001):
            curPass += passChange[i]
            if curPass > capacity:
                return False
        return True
        
        trips.sort(key = lambda t: t[1])
        
        minHeap = [] #the pair of [end, numpassengers]
        curPass = 0
        for t in trips:
            numPass, start, end = t
            while minHeap and minHeap[0][0] <= start:
                curPass -= heappop(minHeap)
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end,numPass])
        return True
            
