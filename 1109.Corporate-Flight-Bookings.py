class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = []
        
        for(start, end, seats) in bookings:
            events.append((start - 1, seats))
            events.append((end + 1 - 1 , -seats))
            
        events.sort()
        results = [0] * n
        for event in events:
            if event[0] >= n:
                continue
            results[event[0]] += event[1]
        for i in range(1, n):
            results[i] += results[i-1]
        return results
