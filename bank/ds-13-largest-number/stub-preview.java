import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below.
    //
    //   largestNumber(nums) : the largest number that can be made by writing
    //                         all of these numbers one after another, as a
    //                         String.
    //
    // Sorting by value does not work. For 3 and 30, "330" beats "303", so 3
    // must come first even though 30 is the larger number.
    //
    // If every number is 0, the answer is "0" and not "000".

    static String largestNumber(int[] nums) {
        // TODO
        return "";
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

        System.out.println(largestNumber(nums));
    }
}
