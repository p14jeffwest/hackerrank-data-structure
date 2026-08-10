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
    //   rangeSum(root, low, high) : the sum of every key in this subtree that
    //                               satisfies low <= key <= high.
    //
    // The tree is a valid BST, and there are many queries against the same
    // tree. Visiting every node for each of them is too slow.
    //
    // The sum can exceed the range of an int.

    static long rangeSum(Node root, int low, int high) {
        // TODO
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");
        Node root = build(tokens);

        int q = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            int low = Integer.parseInt(t.nextToken());
            int high = Integer.parseInt(t.nextToken());
            sb.append(rangeSum(root, low, high)).append('\n');
        }

        System.out.print(sb);
    }
}
