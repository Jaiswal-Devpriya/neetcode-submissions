"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            previous = intervals[i - 1]
            current = intervals[i]

            if current.start < previous.end:
                return False

        return True

