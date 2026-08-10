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

    // Merge sort, with a count hung on the merge.
    //
    // The moment that matters is taking a value from the RIGHT half. Every
    // value still unconsumed in the left half is larger than it -- the halves
    // are sorted, so if the left front is larger, so is everything behind it
    // -- and each of them sits at an earlier index. So that one step accounts
    // for exactly (left values remaining) inversions, all at once.
    //
    // Taking from the left when the two are EQUAL is what keeps equal values
    // out of the count. Using < instead of <= there would count them.
    //
    // Every inversion is counted once and only once, because the pair is
    // counted in the single merge where its two values first end up in
    // different halves.
    //
    // O(n log n) time. The sorting is a by-product; the count is the answer.
    //
    // The total needs a long: 200,000 values in descending order give
    // 199,999 * 200,000 / 2, about 2 * 10^10.

    private static long count;

    static long countInversions(int[] a) {
        count = 0;
        sort(a, 0, a.length - 1, new int[a.length]);
        return count;
    }

    private static void sort(int[] a, int lo, int hi, int[] buf) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        sort(a, lo, mid, buf);
        sort(a, mid + 1, hi, buf);
        merge(a, lo, mid, hi, buf);
    }

    private static void merge(int[] a, int lo, int mid, int hi, int[] buf) {
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid && j <= hi) {
            if (a[i] <= a[j]) {
                buf[k++] = a[i++];
            } else {
                buf[k++] = a[j++];
                count += mid - i + 1;          // everything left in the left half
            }
        }
        while (i <= mid) buf[k++] = a[i++];
        while (j <= hi) buf[k++] = a[j++];
        System.arraycopy(buf, lo, a, lo, hi - lo + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        int[] a = readArray(br, n);
        System.out.println(countInversions(a));
    }
}
