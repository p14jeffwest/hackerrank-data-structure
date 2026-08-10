import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below.
    //
    //   longestConsecutive(nums) : the length of the longest run of
    //                              consecutive integers present in nums,
    //                              in any order.
    //
    // Duplicates count once. An empty array gives 0.
    //
    // O(n) is expected, so the values may not be sorted first.

    static int longestConsecutive(int[] nums) {
        // TODO
        return 0;
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
