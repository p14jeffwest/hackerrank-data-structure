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

    // Write the three methods below using recursion.
    //
    //   countLeaves(node) : how many leaves are in this subtree.
    //                       A leaf has NO children at all; a node with one
    //                       child is not a leaf.
    //
    //   height(node)      : the height of this subtree, counted in EDGES.
    //                       A single node has height 0.
    //                       An empty subtree has height -1.
    //
    //   maxDepth(node)    : the same measurement counted in NODES.
    //                       A single node has depth 1.
    //                       An empty subtree has depth 0.
    //
    // All three have the same shape: settle the empty case, then combine what
    // comes back from the two children.

    static int countLeaves(Node node) {
        // TODO
        return 0;
    }

    static int height(Node node) {
        // TODO
        return -1;
    }

    static int maxDepth(Node node) {
        // TODO
        return 0;
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
