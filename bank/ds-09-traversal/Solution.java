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

    // The three depth-first traversals differ in ONE line: where the visit
    // sits relative to the two recursive calls. Nothing else changes.
    //
    // The level-order traversal is a different animal. It cannot be written
    // this way at all, because recursion follows one branch to the bottom
    // before touching the next, which is the opposite of what is wanted. A
    // queue gives the right order: take a node, visit it, put its children at
    // the back, and the first-in-first-out rule keeps every level ahead of
    // the one below it.
    //
    // All four are O(n). Their extra space differs: the recursive three use
    // stack proportional to the HEIGHT, the queue holds up to one level's
    // WIDTH.

    static void preorder(Node node, List<Integer> out) {
        if (node == null) return;
        out.add(node.data);                 // visit first
        preorder(node.left, out);
        preorder(node.right, out);
    }

    static void inorder(Node node, List<Integer> out) {
        if (node == null) return;
        inorder(node.left, out);
        out.add(node.data);                 // visit between the two sides
        inorder(node.right, out);
    }

    static void postorder(Node node, List<Integer> out) {
        if (node == null) return;
        postorder(node.left, out);
        postorder(node.right, out);
        out.add(node.data);                 // visit last
    }

    static void levelOrder(Node root, List<Integer> out) {
        if (root == null) return;
        Deque<Node> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            out.add(node.data);
            if (node.left != null) queue.offer(node.left);
            if (node.right != null) queue.offer(node.right);
        }
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
