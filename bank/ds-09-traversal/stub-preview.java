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

    // Write the four traversals below.
    //
    // Each one visits every node once and appends the value of each node it
    // visits to "out", in that traversal's order.
    //
    //   preorder    node, left subtree, right subtree
    //   inorder     left subtree, node, right subtree
    //   postorder   left subtree, right subtree, node
    //   levelOrder  level by level from the top, left to right within a level
    //
    // The first three do the same three things in different orders, so
    // writing one gives the other two. The fourth is not like them at all.
    //
    // Remember that a child may be null.

    static void preorder(Node node, List<Integer> out) {
        // TODO
    }

    static void inorder(Node node, List<Integer> out) {
        // TODO
    }

    static void postorder(Node node, List<Integer> out) {
        // TODO
    }

    static void levelOrder(Node root, List<Integer> out) {
        // TODO
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        List<Integer> pre = new ArrayList<>();
        List<Integer> in = new ArrayList<>();
        List<Integer> post = new ArrayList<>();
        List<Integer> level = new ArrayList<>();
        preorder(root, pre);
        inorder(root, in);
        postorder(root, post);
        levelOrder(root, level);

        StringBuilder sb = new StringBuilder();
        sb.append(join(pre)).append('\n');
        sb.append(join(in)).append('\n');
        sb.append(join(post)).append('\n');
        sb.append(join(level)).append('\n');

        System.out.print(sb);
    }
}
