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

    // Write the method below.
    //
    //   selectionPasses(a, k) : the array after exactly k passes of selection
    //                           sort.
    //
    // In pass i, find the smallest value in positions i..end and swap it with
    // position i. k = 0 means no pass at all, and a value already in place
    // still uses up a pass.
    //
    // Do not modify the array you are given; copy it first.

    static int[] selectionPasses(int[] a, int k) {
        // TODO
        return new int[a.length];
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
