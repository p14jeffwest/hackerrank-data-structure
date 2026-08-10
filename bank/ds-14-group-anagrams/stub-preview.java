import java.io.*;
import java.util.*;

public class Solution {

    // Write the method below.
    //
    //   groupAnagrams(strs) : the words grouped so that words made of the
    //                         same letters are together.
    //
    // The order is fixed and is part of the answer:
    //   - within a group, the words keep the order they had in `strs`;
    //   - the groups come in the order their FIRST word appeared in `strs`.
    //
    // A plain HashMap has no order of its own, so returning map.values()
    // gives the groups in whatever order it happens to hold them.

    static List<List<String>> groupAnagrams(String[] strs) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        String[] strs = new String[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            strs[i] = st.nextToken();
        }

        List<List<String>> groups = groupAnagrams(strs);

        StringBuilder sb = new StringBuilder();
        sb.append(groups.size()).append('\n');
        for (List<String> group : groups) {
            for (int i = 0; i < group.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(group.get(i));
            }
            sb.append('\n');
        }

        System.out.print(sb);
    }
}
