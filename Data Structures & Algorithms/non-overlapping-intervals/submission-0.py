class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        count=0
        for start,end in intervals[1:]:
            if start>= prev_end:
                prev_end = end
            else:
                count+=1
        return count
