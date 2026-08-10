import java.io.*;
import java.util.*;

public class Solution {

    // Put everything in a set, then walk only the runs that have a beginning.
    //
    // A value starts a run exactly when value - 1 is absent. Checking that
    // first is what keeps the whole thing linear: without it, a run of length
    // L would be walked from each of its L members, which is O(n^2) on one
    // long run. With it, each run is walked exactly once, from its smallest
    // value, so across the whole set the inner loop advances at most n times
    // in total.
    //
    // The set also removes duplicates for free, which is what "duplicates
    // count once" needs.
    //
    // Sorting would answer the same question in O(n log n). The hash's O(1)
    // membership test is what replaces it -- that is 14.7's point, and it is
    // why the constraints forbid the sort even though it would be fast enough
    // at this size.
    //
    // O(n) time and O(n) space.

    static int longestConsecutive(int[] nums) {
        Set<Integer> values = new HashSet<>();
        for (int v : nums) values.add(v);

        int best = 0;
        for (int value : values) {
            if (values.contains(value - 1)) continue;   // not the start of a run

            int length = 1;
            int next = value + 1;
            while (values.contains(next)) {
                length++;
                next++;
            }
            if (length > best) best = length;
        }
        return best;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            nums[i] = (int) in.nval;
        }

        System.out.println(longestConsecutive(nums));
    }
}
