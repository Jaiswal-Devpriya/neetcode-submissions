"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        max_rooms=1
        intervals.sort(key=lambda x:x.start)
        heap=[intervals[0].end]
        for i in range(1,len(intervals)):
            
            while heap and intervals[i].start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i].end)
            max_rooms = max(max_rooms, len(heap))
        return max_rooms
