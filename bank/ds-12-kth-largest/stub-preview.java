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
    //   kthLargest(nums, k) : the k-th largest value. k starts at 1, so k = 1
    //                         is the maximum.
    //
    // Equal values are counted separately: in 5 5 3, the 2nd largest is 5.
    //
    // Taking the maximum out k times is O(n*k) and is too slow here.

    static int kthLargest(int[] nums, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] nums = readArray(br, n);
        System.out.println(kthLargest(nums, k));
    }
}
