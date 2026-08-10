import java.io.*;
import java.util.*;

public class Solution {

    // Reads the numbers. Leave this part unchanged.
    static int[] readArray(BufferedReader br, int n) throws IOException {
        int[] a = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        return a;
    }

    // Write the method below.
    //
    //   countInversions(a) : how many pairs (i, j) have i < j and a[i] > a[j].
    //
    // Equal values are not an inversion.
    //
    // Checking every pair is O(n^2) and will not finish. Merge sort does the
    // same comparisons in O(n log n) -- the counting can be hung on its merge
    // step.
    //
    // The count needs a long. You may rearrange `a`.

    static long countInversions(int[] a) {
        // TODO
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] a = readArray(br, n);
        System.out.println(countInversions(a));
    }
}
