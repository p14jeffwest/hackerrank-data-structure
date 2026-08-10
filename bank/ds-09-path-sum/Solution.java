import java.io.*;
import java.util.*;

class Node {
    int data;        // value stored in this node
    Node left;       // left child, null if there is none
    Node right;      // right child, null if there is none

    Node(int data) {
        this.data = data;
    }
}

public class Solution {

    // Builds a binary tree from a level-order listing.
    // "#" marks a missing child; children of a missing node are not listed.
    static Node build(String[] tokens) {
        if (tokens.length == 0 || tokens[0].equals("#")) {
            return null;
        }
        Node root = new Node(Integer.parseInt(tokens[0]));
        Deque<Node> q = new ArrayDeque<>();
        q.offer(root);

        int i = 1;
        while (!q.isEmpty() && i < tokens.length) {
            Node cur = q.poll();
            if (i < tokens.length) {
                if (!tokens[i].equals("#")) {
                    cur.left = new Node(Integer.parseInt(tokens[i]));
                    q.offer(cur.left);
                }
                i++;
            }
            if (i < tokens.length) {
                if (!tokens[i].equals("#")) {
                    cur.right = new Node(Integer.parseInt(tokens[i]));
                    q.offer(cur.right);
                }
                i++;
            }
        }
        return root;
    }

    // Joins the visited values with single spaces.
    static String join(List<Integer> values) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < values.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(values.get(i));
        }
        return sb.toString();
    }

    // Carry the remaining amount downward rather than the running sum upward.
    // Subtract the current node's value from target and ask the two children
    // the same question with what is left.
    //
    // Two decisions do all the work.
    //
    //   At a LEAF, the answer is whether what remains is exactly this node's
    //   value -- there is nowhere further to go.
    //
    //   At a MISSING child, the answer is false, not true. Returning true
    //   there would let a path stop at a one-sided node, and the statement
    //   says a path must end at a leaf. This is why the leaf test comes
    //   BEFORE the recursion and cannot be replaced by "target reached zero".
    //
    // Negative values matter: the running total can fall as well as rise, so
    // there is no cutting a branch off because the remainder went past zero.
    //
    // O(n) per query.

    static boolean hasPathSum(Node node, int target) {
        if (node == null) return false;
        if (node.left == null && node.right == null) return target == node.data;
        int rest = target - node.data;
        return hasPathSum(node.left, rest) || hasPathSum(node.right, rest);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");
        Node root = build(tokens);

        int q = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        StringTokenizer tk = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int target = Integer.parseInt(tk.nextToken());
            sb.append(hasPathSum(root, target)).append('\n');
        }

        System.out.print(sb);
    }
}
