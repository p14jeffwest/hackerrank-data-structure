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

    // All three are the same recursion with a different combining step.
    //
    // countLeaves: an empty subtree has none; a node with no children is one;
    //   otherwise the two sides add up. Note the middle case -- testing
    //   "no children" and not "no left child", which is what makes a
    //   one-sided node correctly not a leaf.
    //
    // height and maxDepth measure the same thing in different units, and the
    //   book uses both: 9.1 counts EDGES, 9.5 counts NODES. They differ by
    //   exactly one on any non-empty tree, and their empty cases differ too
    //   -- -1 against 0. The -1 is what makes height work: a leaf's children
    //   report -1, so 1 + max(-1, -1) is 0, which is the leaf's height.
    //
    // O(n) each; the stack goes as deep as the tree is tall.

    static int countLeaves(Node node) {
        if (node == null) return 0;
        if (node.left == null && node.right == null) return 1;
        return countLeaves(node.left) + countLeaves(node.right);
    }

    static int height(Node node) {
        if (node == null) return -1;
        return 1 + Math.max(height(node.left), height(node.right));
    }

    static int maxDepth(Node node) {
        if (node == null) return 0;
        return 1 + Math.max(maxDepth(node.left), maxDepth(node.right));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        StringBuilder sb = new StringBuilder();
        sb.append(countLeaves(root)).append('\n');
        sb.append(height(root)).append('\n');
        sb.append(maxDepth(root)).append('\n');

        System.out.print(sb);
    }
}
