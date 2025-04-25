"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 1:
            return True

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            prev, curr = intervals[i-1], intervals[i]
            if prev.end > curr.start:
                return False

        return True