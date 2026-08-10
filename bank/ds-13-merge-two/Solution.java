import java.io.*;
import java.util.*;

public class Solution {

    // The merge step of merge sort. Two indices walk forward, one per array,
    // and the smaller of the two front values is taken each time. Neither
    // index ever goes back, so every value is looked at once: O(n + m).
    //
    // Taking from the left when the two are EQUAL is what makes the merge
    // stable. It changes nothing for plain ints, where equal values cannot be
    // told apart, but it is the line that matters when the same merge is used
    // on records -- and it costs nothing to write it correctly now.
    //
    // One array runs out before the other, so the two tail loops copy
    // whatever is left. Exactly one of them does any work.
    //
    // Concatenating and calling Arrays.sort would be O((n+m) log(n+m)) and
    // would throw away the fact that the inputs are already ordered.

    static int[] mergeSorted(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;

        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) result[k++] = a[i++];
            else result[k++] = b[j++];
        }
        while (i < a.length) result[k++] = a[i++];
        while (j < b.length) result[k++] = b[j++];

        return result;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            a[i] = (int) in.nval;
        }

        in.nextToken();
        int m = (int) in.nval;
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            in.nextToken();
            b[i] = (int) in.nval;
        }

        int[] merged = mergeSorted(a, b);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < merged.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(merged[i]);
        }
        sb.append('\n');

        System.out.print(sb);
    }
}
