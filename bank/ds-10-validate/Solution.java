import java.io.*;
import java.util.*;

class Node {
    int key;         // key stored in this node
    Node left;       // left child, null if there is none
    Node right;      // right child, null if there is none

    Node(int key) {
        this.key = key;
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

    // A node is not constrained by its parent alone but by every ancestor.
    // Going left tightens the upper bound to the current key; going right
    // tightens the lower bound. Each node must sit strictly inside the
    // window its ancestors have left it.
    //
    // Comparing only parent against child is the usual wrong answer, and it
    // accepts trees like 10 -> (5, 25 -> (2, 45)): 2 is a legal left child of
    // 25 and still wrong, because it sits in 10's right subtree.
    //
    // The bounds are long, not int. Keys reach Integer.MIN_VALUE and
    // Integer.MAX_VALUE, so an int-based sentinel has no value left to mean
    // "no bound yet" -- a root of Integer.MIN_VALUE would be rejected by its
    // own starting bound.
    //
    // O(n) time, O(h) stack.

    static boolean isValidBST(Node root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private static boolean validate(Node node, long low, long high) {
        if (node == null) return true;
        if (node.key <= low || node.key >= high) return false;
        return validate(node.left, low, node.key)
            && validate(node.right, node.key, high);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            br.readLine();                              // number of tokens
            String[] tokens = br.readLine().trim().split("\\s+");
            sb.append(isValidBST(build(tokens))).append('\n');
        }

        System.out.print(sb);
    }
}
