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

    // Every operation makes one comparison per level and then commits to one
    // side, so each costs the height of the tree.
    //
    // insert and deleteKey return the subtree root because they may CHANGE
    // it: inserting into an empty subtree produces a new node, and deleting
    // the subtree's own root promotes something else. Reassigning on the way
    // back up -- root.left = insert(root.left, key) -- is what keeps the
    // parent's link correct without ever tracking a parent pointer.
    //
    // Deletion splits three ways:
    //   no left child   -> promote the right (this also covers a leaf, where
    //                      the right is null too)
    //   no right child  -> promote the left
    //   both children   -> the node cannot simply be removed, so its KEY is
    //                      overwritten with the predecessor -- the largest
    //                      key in the left subtree -- and that node is
    //                      deleted instead. Being the rightmost of the left
    //                      subtree, it has no right child, so removing it
    //                      falls into one of the first two cases.

    static Node insert(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.key) root.left = insert(root.left, key);
        else if (key > root.key) root.right = insert(root.right, key);
        return root;                                  // equal: already present
    }

    static Node search(Node root, int key) {
        if (root == null) return null;
        if (key == root.key) return root;
        return key < root.key ? search(root.left, key) : search(root.right, key);
    }

    private static Node findMax(Node node) {
        while (node.right != null) node = node.right;
        return node;
    }

    static Node deleteKey(Node root, int key) {
        if (root == null) return null;
        if (key < root.key) {
            root.left = deleteKey(root.left, key);
        } else if (key > root.key) {
            root.right = deleteKey(root.right, key);
        } else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            Node pred = findMax(root.left);
            root.key = pred.key;
            root.left = deleteKey(root.left, pred.key);
        }
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
