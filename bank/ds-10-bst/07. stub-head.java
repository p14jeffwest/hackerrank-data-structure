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
