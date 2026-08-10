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

    // Sort ascending and read from the far end. With the values in order the
    // largest sits at n-1, the 2nd largest at n-2, and the k-th largest at
    // n-k. Equal values occupy separate positions, which is exactly what
    // "counted separately" means.
    //
    // O(n log n), and the sort is the whole cost.
    //
    // The book also gives the size-k min-heap: push everything, and drop the
    // root whenever the heap exceeds k, so what remains are the k largest and
    // the root is the smallest of them. That is O(n log k) and is better when
    // k is small. Either is fine here.
    //
    // What is not fine is taking the maximum out k times. That is O(n*k), and
    // with k near n it does not finish.
    //
    // The array is sorted in place, which the caller does not mind -- it does
    // not look at it again.

    static int kthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
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
