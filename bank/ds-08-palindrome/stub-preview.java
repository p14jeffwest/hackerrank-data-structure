import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below using recursion.
    //
    // isPalindrome(s) alone cannot remember which part of the string is still
    // being examined. A private helper method taking those positions as
    // parameters is the usual way round that.

    static boolean isPalindrome(String s) {
        // TODO
        return false;
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
