import java.io.*;
import java.util.*;

class Node {
    int key;         // value stored in this node
    Node left;       // left child, null if there is none
    Node right;      // right child, null if there is none

    Node(int key) {
        this.key = key;
    }
}

public class Solution {

    // Appends the keys of the subtree in inorder to sb.
    static void inorder(Node node, StringBuilder sb) {
        if (node == null) return;
        inorder(node.left, sb);
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) != '\n') sb.append(' ');
        sb.append(node.key);
        inorder(node.right, sb);
    }

    // Appends the keys of the subtree in preorder to sb.
    static void preorder(Node node, StringBuilder sb) {
        if (node == null) return;
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) != '\n') sb.append(' ');
        sb.append(node.key);
        preorder(node.left, sb);
        preorder(node.right, sb);
    }

    // Write the three methods below.
    //
    //   insert(root, key)    put key into this subtree and return its root.
    //                        An empty subtree is null. A key already present
    //                        changes nothing.
    //   search(root, key)    the node holding key, or null.
    //   deleteKey(root, key) remove key from this subtree and return its root.
    //                        A key that is not there changes nothing.
    //
    // insert and deleteKey return the subtree root because the caller writes
    //     root = insert(root, key);
    // and a recursive call is written the same way:
    //     root.left = insert(root.left, key);

    static Node insert(Node root, int key) {
        // TODO
        return root;
    }

    static Node search(Node root, int key) {
        // TODO
        return null;
    }

    static Node deleteKey(Node root, int key) {
        // TODO
        return root;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine().trim());

        Node root = null;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            switch (op) {
                case "insert":
                    root = insert(root, Integer.parseInt(t.nextToken()));
                    break;
                case "delete":
                    root = deleteKey(root, Integer.parseInt(t.nextToken()));
                    break;
                case "search":
                    sb.append(search(root, Integer.parseInt(t.nextToken())) != null
                              ? "YES" : "NO").append('\n');
                    break;
                case "print":
                    inorder(root, sb);
                    sb.append('\n');
                    break;
                case "preorder":
                    preorder(root, sb);
                    sb.append('\n');
                    break;
                default:
                    break;
            }
        }

        System.out.print(sb);
    }
}
