import java.io.*;
import java.util.*;

public class Solution {

    // Sorting by start is what makes one pass enough: once the intervals are
    // in that order, everything that overlaps a given interval is adjacent to
    // it, so a group can be closed as soon as a gap appears. Without the sort
    // there is no way to know that nothing later reaches back.
    //
    // Walking through them, the current group ends at `end`. The next
    // interval either starts at or before that -- so it belongs to the group,
    // and the group's end stretches to whichever end is further -- or it
    // starts after, and the group is finished.
    //
    // The comparison is `start > end`, not `>=`: touching intervals merge,
    // which the book states and which is the opposite of the rule in
    // ds-11-meeting-rooms.
    //
    // The end must be the MAXIMUM, not simply the newer one. An interval can
    // sit entirely inside the group it joins -- [1,10] then [2,3] -- and
    // taking the newer end would shrink the group.
    //
    // O(n log n): the sort. The pass itself is O(n).

    static int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

        List<int[]> merged = new ArrayList<>();
        for (int[] interval : intervals) {
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < interval[0]) {
                merged.add(new int[]{interval[0], interval[1]});
            } else {
                int[] last = merged.get(merged.size() - 1);
                last[1] = Math.max(last[1], interval[1]);
            }
        }
        return merged.toArray(new int[0][]);
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[][] intervals = new int[n][2];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            intervals[i][0] = (int) in.nval;
            in.nextToken();
            intervals[i][1] = (int) in.nval;
        }

        int[][] result = merge(intervals);

        StringBuilder sb = new StringBuilder();
        sb.append(result.length).append('\n');
        for (int[] iv : result) {
            sb.append(iv[0]).append(' ').append(iv[1]).append('\n');
        }

        System.out.print(sb);
    }
}
