import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below.
    //
    //   merge(intervals) : the given intervals with every overlapping group
    //                      replaced by the single interval covering it,
    //                      in ascending order of start.
    //
    // intervals[i] is {start, end}, in no particular order. You may rearrange
    // the array.
    //
    // Intervals that merely touch -- one ending where the next begins -- do
    // overlap for this purpose and must be merged.
    //
    // Comparing every pair is O(n^2) and is too slow here.

    static int[][] merge(int[][] intervals) {
        // TODO
        return new int[0][];
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
