# Leetcode: https://leetcode.com/problems/video-stitching/
# Medium, beats 100%, my slow shift into C++

"""
Take a greedy approach, try to extend the ending of the videos as far as you can whilst not missing gaps
Identify thresholds of when our current ending time is over: The next starting time is greater than our ending time.
At that point, we are FORCED to extend the tape, we should use the maximum then.

After sort:
[[0, 2], [1, 5], [1, 9], [4, 6], [5, 9], [8, 10]] 

Steps
1. At [1, 5] our ending time has passed. We find the maximum tape we can extend BEFORE this step (ending_time=2)
2. At [4, 6] our ending time (=2) has passed. We find max extension before that (ending_time=9)
3. At [8, 10] our ending time hasn't expired but it's the last index, so we should take that as long as there is no gap.
"""

class Solution {
public:
    // Ascending left index, if tied ascending right element
    static bool cmp(vector<int> &a, vector<int> &b) {
        if (a[0] == b[0]) {
            return a[1] < b[1];
        }
        return a[0] < b[0];
    }

    int videoStitching(vector<vector<int>>& clips, int T) {
        sort(clips.begin(), clips.end(), cmp);
        int count = 0;
        int ending_time = 0;
        int local_max = 0;
        for (int i = 0; i < clips.size(); i++) {
            local_max = max(local_max, clips[i][1]);
            if (clips[i][0] <= ending_time && 
                ((i < clips.size() - 1 && clips[i+1][0] > ending_time) || i == clips.size() - 1)) {
                ending_time = local_max;
                local_max = 0;
                count++;
            }
            if (ending_time >= T) {
                return count;
            }
        }
        return -1;
    }
};
