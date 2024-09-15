#Sol 0: Beats - 90, 86
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost): #If the total gas is less than total cost, then it is impossible to complete a full circle
            return -1

        start = 0
        tank = 0

        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]

            if tank < 0:
                start = i+1
                tank = 0
        
        if start < len(gas):
            return start
        else:
            return -1
