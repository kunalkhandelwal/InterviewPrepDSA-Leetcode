#Sol 0: Took almost 40mins to solve with all the test cases
#But learnt a lot as I solved it myself and my solution beats - 84, 97

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        for i in range(len(timePoints)):
            #timePoints[i] = "".join((timePoints[i].split(":")))

            hours = int(timePoints[i][:2])
            mins = int(timePoints[i][3:])
            timePoints[i] = hours*60 + mins
        
        timePoints.sort()

        min_time = 9999
        for i in range(1,len(timePoints)):
            if timePoints[i] - timePoints[i-1] < min_time:
                min_time = timePoints[i] - timePoints[i-1]

            if min_time == 0:
                return 0

        circular_diff = 1440 + timePoints[0] - timePoints[-1] # # Circular difference between the last and first time point (handling wrap-around)
        #It is for test cases like: ["12:12","00:13"] which instead of going from 
        min_time = min(min_time, circular_diff)

        return min_time
