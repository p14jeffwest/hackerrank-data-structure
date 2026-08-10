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

    // Appends the keys of the subtree in preorder to sb.
    static void preorder(Node node, StringBuilder sb) {
        if (node == null) return;
        if (sb.length() > 0 && sb.charAt(sb.length() - 1) != '\n') sb.append(' ');
        sb.append(node.key);
        preorder(node.left, sb);
        preorder(node.right, sb);
    }

    // The height of the tree, counted in edges. An empty tree is -1.
    static int height(Node node) {
        if (node == null) return -1;
        return 1 + Math.max(height(node.left), height(node.right));
    }

    // Write the method below.
    //
    //   sortedArrayToBST(nums) : build a balanced BST over the ascending
    //                            array `nums` and return its root.
    //
    // For a range, the root must be nums[(lo + hi) / 2] -- integer division,
    // so the left of the two middles when the range holds an even number of
    // keys. Any other choice also balances the tree, but gives a different
    // one.

    static Node sortedArrayToBST(int[] nums) {
        // TODO
        return null;
    }

    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            nums[i] = (int) in.nval;
        }

        Node root = sortedArrayToBST(nums);

        StringBuilder sb = new StringBuilder();
        preorder(root, sb);
        sb.append('\n').append(height(root)).append('\n');

        System.out.print(sb);
    }
}
