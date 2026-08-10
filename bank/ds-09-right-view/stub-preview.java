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

    // Write the method below.
    //
    // rightSideView(root) : the nodes visible when the tree is viewed from
    //                       the right, from the top down. Append their values
    //                       to "out".
    //
    // At each level, the node you see is the rightmost one AT THAT LEVEL --
    // which is not always a right child, and not always deep in the tree.

    static void rightSideView(Node root, List<Integer> out) {
        // TODO
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        List<Integer> view = new ArrayList<>();
        rightSideView(root, view);

        System.out.println(join(view));
    }
}
