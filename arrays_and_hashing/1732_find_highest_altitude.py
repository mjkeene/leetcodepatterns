class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        curr_max = 0
        for i in range(len(gain)):
            curr_max += gain[i]
            max_altitude = max(max_altitude, curr_max)

        return max_altitude
    