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

    // One pass, with the answer kept on the side.
    //
    // At each node, the longest path THROUGH that node has
    //     height(left) + height(right) + 2   edges
    // counting the two edges down to the children. So if every node reports
    // its own height upward, the largest of those sums over all nodes is the
    // diameter -- and the recursion can do both jobs at once.
    //
    // The method returns the height (in edges, empty = -1) and updates a
    // field on the way back up. That separation is the whole trick: the
    // RETURN VALUE is what the parent needs, and the FIELD is what the answer
    // needs. They are different quantities and confusing them is the usual
    // way this goes wrong.
    //
    // Writing it as "at every node, compute height(left) + height(right)"
    // instead is correct and O(n^2): every height call walks its whole
    // subtree, and on a skewed tree that is 100,000 walks of up to 100,000
    // nodes.
    //
    // O(n) time, O(h) stack.

    private static int best;

    static int diameter(Node root) {
        best = 0;
        heightAndScan(root);
        return best;
    }

    private static int heightAndScan(Node node) {
        if (node == null) return -1;                 // empty subtree
        int leftHeight = heightAndScan(node.left);
        int rightHeight = heightAndScan(node.right);
        int through = leftHeight + rightHeight + 2;  // edges of the path through here
        if (through > best) best = through;
        return 1 + Math.max(leftHeight, rightHeight);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        System.out.println(diameter(root));
    }
}
