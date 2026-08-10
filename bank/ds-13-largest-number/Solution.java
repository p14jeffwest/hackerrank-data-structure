import java.io.*;
import java.util.*;

public class Solution {

    // The order cannot be decided by the values themselves, because what
    // matters is what two numbers look like written side by side. So compare
    // the two ways of writing them: for a and b, weigh "a"+"b" against
    // "b"+"a" and put whichever gives the larger string first.
    //
    // Those two strings always have the same length, so comparing them as
    // text is comparing them as numbers -- no leading-zero or width question
    // arises.
    //
    // The comparison is a valid total order: it is transitive, which is what
    // lets a sort use it at all. (An arbitrary "looks bigger" rule need not
    // be, and Java throws if a comparator contradicts itself.)
    //
    // The all-zeros case is the one special case. Sorting leaves "0" at the
    // front, and if the front is "0" then every number is 0, so the answer is
    // "0" rather than a string of them.
    //
    // Values go into a String[] because Arrays.sort with a Comparator needs
    // objects. That sort is also stable, though nothing here depends on it.
    //
    // O(n log n) comparisons, each on strings of at most ten digits.

    static String largestNumber(int[] nums) {
        String[] s = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            s[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(s, (a, b) -> (b + a).compareTo(a + b));

        if (s[0].equals("0")) return "0";

        StringBuilder sb = new StringBuilder();
        for (String x : s) sb.append(x);
        return sb.toString();
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
