import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below using recursion.
    //
    // Two things to decide:
    //   - when should the recursion stop, and what should it return then?
    //   - what happens on the very first call when a is smaller than b?

    static int gcd(int a, int b) {
        // TODO
        return 1;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int t = (int) in.nval;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            int a = (int) in.nval;
            in.nextToken();
            int b = (int) in.nval;
            sb.append(gcd(a, b)).append('\n');
        }

        System.out.print(sb);
    }
}
