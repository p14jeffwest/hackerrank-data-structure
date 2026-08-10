import java.io.*;
import java.util.*;

public class Solution {

    // Reads the array. Leave this part unchanged.
    static int[] readArray(BufferedReader br, int n) throws IOException {
        int[] a = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        return a;
    }

    // Pass i takes position i, finds the smallest value from i to the end,
    // and swaps it into place. After k passes the first k positions hold the
    // k smallest values in order, and everything from k onward is whatever
    // the swaps left behind -- NOT the original order, which is what makes
    // the intermediate state worth asking for.
    //
    // The swap happens even when the smallest value is already at position i.
    // That still counts as a pass; skipping it would change nothing in the
    // array but would break the count.
    //
    // The input array is copied, because the caller keeps it.
    //
    // O(n*k), and O(n^2) when k is n-1, which is why n stays small here.

    static int[] selectionPasses(int[] a, int k) {
        int[] b = Arrays.copyOf(a, a.length);
        for (int i = 0; i < k; i++) {
            int min = i;
            for (int j = i + 1; j < b.length; j++) {
                if (b[j] < b[min]) min = j;
            }
            int t = b[i];
            b[i] = b[min];
            b[min] = t;
        }
        return b;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] a = readArray(br, n);
        int[] result = selectionPasses(a, k);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) {
                sb.append(' ');
            }
            sb.append(result[i]);
        }
        sb.append('\n');
        System.out.print(sb);
    }
}
