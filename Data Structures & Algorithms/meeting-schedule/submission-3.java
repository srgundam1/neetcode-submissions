/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        // 1. sort intervals by start time
        // 2. If curr interval.end > next interval.start: return false 
            Collections.sort(intervals, Comparator.comparingInt(i -> i.start));
            for (int i = 1; i < intervals.size(); i++) {
                Interval x = intervals.get(i-1);
                Interval y = intervals.get(i);
                if (x.end > y.start) {
                    return false;
                }
            }
            return true;
    }
}
