import java.io.*;
import java.util.*;

public class Solution {

    // Compare the two outer characters, then narrow inwards.
    //
    // Base case: a range of zero or one character has nothing left to
    // compare, so it is a palindrome. That covers both even and odd lengths
    // -- an even-length string ends with low > high, an odd-length one ends
    // with low == high.
    //
    // Recursive step: if the ends differ the answer is false immediately;
    // otherwise the answer for the whole range is the answer for the range
    // one character narrower on each side.
    //
    // The public method cannot recurse on its own, because it has no way to
    // say which part of the string is still under examination. The helper
    // carries those two positions.

    static boolean isPalindrome(String s) {
        return check(s, 0, s.length() - 1);
    }

    private static boolean check(String s, int low, int high) {
        if (low >= high) return true;                 // nothing left to compare
        if (s.charAt(low) != s.charAt(high)) return false;
        return check(s, low + 1, high - 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            String s = br.readLine();
            sb.append(isPalindrome(s)).append('\n');
        }

        System.out.print(sb);
    }
}
