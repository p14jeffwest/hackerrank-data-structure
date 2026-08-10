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

    // The middle key becomes the root, and the two halves become the two
    // subtrees by the same rule. Because the array is ascending, everything
    // left of the middle is smaller and everything right is larger, so the
    // BST rule holds for free -- no comparisons are needed at all.
    //
    // Each half is at most one larger than the other, so the height is
    // floor(log2(n)), the minimum possible for n keys.
    //
    // The range is passed as two INDICES rather than a copied subarray.
    // Copying would allocate n log n elements over the whole build; indices
    // allocate nothing. The tree itself is the only allocation.
    //
    // O(n) time: every element becomes exactly one node.

    static Node sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }

    private static Node build(int[] nums, int lo, int hi) {
        if (lo > hi) return null;
        int mid = (lo + hi) / 2;
        Node node = new Node(nums[mid]);
        node.left = build(nums, lo, mid - 1);
        node.right = build(nums, mid + 1, hi);
        return node;
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
