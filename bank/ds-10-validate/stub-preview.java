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

    // Write the method below.
    //
    //   isValidBST(root) : true if every key in a node's left subtree is
    //                      smaller than that node's key, and every key in its
    //                      right subtree is larger -- at EVERY node.
    //
    // Keys can be any int, including Integer.MIN_VALUE and Integer.MAX_VALUE.

    static boolean isValidBST(Node root) {
        // TODO
        return false;
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
