class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def solve(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:
            m = len(start2)
            
            # Pair up and sort the second ride category by start time
            v = sorted(zip(start2, dur2))
            
            lmin = [0] * m
            rmin = [0] * m
            
            # Prefix minimum of durations
            lmin[0] = v[0][1]
            for i in range(1, m):
                lmin[i] = min(lmin[i-1], v[i][1])
                
            # Suffix minimum of (start time + duration)
            rmin[m-1] = v[m-1][0] + v[m-1][1]
            for i in range(m-2, -1, -1):
                rmin[i] = min(rmin[i+1], v[i][0] + v[i][1])
                
            # Extract just the start times for bisect
            starts = [x[0] for x in v]
            
            min_finish = float('inf')
            
            # Iterate through all possible first rides
            for i in range(len(start1)):
                finish_time1 = start1[i] + dur1[i]
                
                # Binary search (equivalent to C++ upper_bound)
                idx = bisect.bisect_right(starts, finish_time1)
                
                # If there are rides opening strictly after finish_time1
                if idx < m:
                    min_finish = min(min_finish, rmin[idx])
                # If there are rides that are already open by finish_time1
                if idx > 0:
                    min_finish = min(min_finish, finish_time1 + lmin[idx-1])
                    
            return min_finish

        # Return the minimum of both possible orderings
        return min(solve(landStartTime,landDuration,waterStartTime ,waterDuration), solve(waterStartTime ,waterDuration,landStartTime,landDuration))
        