import java.io.*;
import java.util.*;

public class Solution {

    // Counting sort, in the three steps of 13.4.
    //
    //   1. count how many times each value occurs
    //   2. turn the counts into a PREFIX SUM, so count[v] becomes the number
    //      of values at most v -- which is the position just past where the
    //      v's belong
    //   3. walk the input FROM THE BACK, placing each value at --count[v]
    //
    // Step 3 going backwards is what makes the sort stable. It changes
    // nothing for plain ints, where equal values are indistinguishable, but
    // it is the property radix sort in 13.5 is built on: that section sorts
    // by one digit at a time and needs each pass to leave the previous
    // digit's order alone.
    //
    // The count array has maxValue + 1 entries, so the whole thing is
    // O(n + maxValue) in time and space. That beats a comparison sort's
    // O(n log n) only while maxValue stays comparable to n -- which is the
    // condition 13.4 states and 13.5 works around.
    //
    // No two values are ever compared with each other.

    static int[] countingSort(int[] a, int maxValue) {
        int[] count = new int[maxValue + 1];
        for (int v : a) count[v]++;

        for (int v = 1; v <= maxValue; v++) count[v] += count[v - 1];

        int[] out = new int[a.length];
        for (int i = a.length - 1; i >= 0; i--) {
            out[--count[a[i]]] = a[i];
        }
        return out;
    }

    public static void main(String[] args) throws IOException {
        DataInputStream in = new DataInputStream(
                new BufferedInputStream(System.in, 1 << 16));

        int n = nextInt(in);
        int maxValue = nextInt(in);
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = nextInt(in);

        int[] sorted = countingSort(a, maxValue);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < sorted.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(sorted[i]);
        }
        sb.append('\n');

        System.out.print(sb);
    }

    // Reads one non-negative integer. Leave this part unchanged.
    private static int nextInt(DataInputStream in) throws IOException {
        int c = in.read();
        while (c < '0') c = in.read();
        int x = 0;
        while (c >= '0') {
            x = x * 10 + (c - '0');
            c = in.read();
        }
        return x;
    }
}
