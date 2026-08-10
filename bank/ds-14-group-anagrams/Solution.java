import java.io.*;
import java.util.*;

public class Solution {

    // Two words are anagrams exactly when they are made of the same letters
    // in the same quantities, so any faithful summary of "which letters, how
    // many" works as a key. Sorting the letters is the shortest one: "eat",
    // "tea" and "ate" all become "aet".
    //
    // What must NOT be used is anything that loses information -- the sum of
    // the character codes, say. "ad" and "bc" both sum to 197 and are not
    // anagrams, so that key merges groups that should stay apart.
    //
    // LinkedHashMap is what gives the required order. A plain HashMap holds
    // its entries in whatever order its own hashing produces, so
    // map.values() would come out in an order that depends on the keys rather
    // than on the input. LinkedHashMap keeps insertion order, and a key is
    // first inserted when its group's first word is met -- which is exactly
    // the order the problem asks for.
    //
    // Within a group the words are appended as they are met, so they keep
    // their input order for free.
    //
    // O(n * k log k) for the sorting of n words of length k; the map
    // operations are O(1) on average.

    static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new LinkedHashMap<>();

        for (String s : strs) {
            char[] letters = s.toCharArray();
            Arrays.sort(letters);
            String key = new String(letters);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(groups.values());
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
