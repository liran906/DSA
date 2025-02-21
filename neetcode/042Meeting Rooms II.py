# Meeting Rooms II
# https://neetcode.io/problems/meeting-schedule-ii
# m

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Recursion O(n^2)
class Solution:
    def minMeetingRooms(self, intervals):
        if intervals == []:
            return 0
        
        # sort the initial interval list
        intervals.sort(key = lambda x: x.start)

        # helper method to find the max meetings one room can contain:
        # interval is the meeting list, d is practically the room number
        def helper(intervals, d):
            nextInterval = []
            j = 1 # j is lag factor, if m1 confilcts with m2, then in next loop, compare m3 with m1 instead of m2
            for i in range(1, len(intervals)):
                if intervals[i-j].end > intervals[i].start:
                    nextInterval.append(intervals[i])
                    j += 1
                else:
                    j = 1 # initialize j to 1
            
            # if there is anything in nextInterval, recursively call the helper function
            if nextInterval:
                return helper(nextInterval, d + 1)
            
            # if not, return the current (last) room number
            return d
        
        return helper(intervals, 1)

# without recursion. O(n^2)
class Solution:
    def minMeetingRooms(self, intervals):
        # sort the initial interval list
        intervals.sort(key = lambda x: x.start)
        d = 0 # d is practically the room number
        while intervals:
            d += 1
            curr = intervals
            intervals = [] # this is now for the conflicting meetings
            j = 1 # j is lag factor, if m1 confilcts with m2, then in next loop, compare m3 with m1 instead of m2
            for i in range(1, len(curr)):
                if curr[i-j].end > curr[i].start:
                    intervals.append(curr[i])
                    j += 1
                else:
                    j = 1
        return d

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
intervals = [(0, 10), (1, 2), (2, 9)]
i1 = Interval(0,10)
i2 = Interval(1,2)
i3 = Interval(2,9)
s = Solution()
print(s.minMeetingRooms([i1, i2, i3]))

# find max overlap in intervals: FAILS THE UPPER CASE
# class Solution:
#     def minMeetingRooms(self, intervals):
#         # sort the initial interval list
#         intervals.sort(key = lambda x: x.start)
#         n = 0 # n is max number of rooms
#         for i in range(len(intervals)):
#             d = 1 # d for delta
#             while i + d < len(intervals) and intervals[i].end > intervals[i+d].start:
#                 d += 1
#             n = max(n, d)
#         return n

# two pointers O(nlogn) (actually its just going through time, need 2 pointer to indecate wheather is start or end)
class Solution:
    def minMeetingRooms(self, intervals):
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        i = j = 0 # two pointers
        count = max_count = 0 # current count & max count
        while i < len(intervals): # max will only occur before or when i reaches the end
            if start[i] < end[j]:
                i += 1
                count += 1
                max_count = max(max_count, count)
            else:
                j += 1
                count -= 1
        return max_count