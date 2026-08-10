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

    // The BST rule says where the answer cannot be, and that is the whole
    // saving. If this node's key is already above `high`, every key in its
    // right subtree is higher still, so the right side is skipped entirely.
    // If the key is below `low`, the left side goes.
    //
    // Only when the key falls inside the range does the walk continue both
    // ways -- and by then it is inside the answer, so the work is paid for.
    //
    // Without the pruning this is a full traversal per query: O(n) each, and
    // O(nQ) over the whole input, which does not finish here. With it, a
    // query costs the height plus the number of keys it reports.
    //
    // The total is accumulated in a long. There can be 200,000 keys of up to
    // 10^9 each, so a single query can reach 2 * 10^14.

    static long rangeSum(Node root, int low, int high) {
        if (root == null) return 0;
        if (root.key > high) return rangeSum(root.left, low, high);
        if (root.key < low) return rangeSum(root.right, low, high);
        return (long) root.key
             + rangeSum(root.left, low, high)
             + rangeSum(root.right, low, high);
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
