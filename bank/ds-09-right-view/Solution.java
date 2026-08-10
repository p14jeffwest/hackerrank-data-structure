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

    // A level-order traversal with the levels kept apart.
    //
    // The trick is the one line `int levelSize = queue.size();`. At the top of
    // each round the queue holds exactly the nodes of one level, so taking
    // that many out processes that level and no more -- and whatever is added
    // meanwhile belongs to the next one. Without that count the queue is just
    // a flat stream and the level boundaries are lost.
    //
    // The last node taken out of each round is the one seen from the right.
    //
    // Note what "rightmost at that level" does NOT mean. It is not the
    // rightmost child, and it need not be reached by going right: on a tree
    // that leans left, every visible node is a left child, because at each
    // level there is nothing else there.
    //
    // O(n) time. The queue holds at most one level, so the space is the width
    // of the widest level, not the height.

    static void rightSideView(Node root, List<Integer> out) {
        if (root == null) return;

        Deque<Node> queue = new ArrayDeque<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();          // this level, and only this level
            for (int i = 0; i < levelSize; i++) {
                Node node = queue.poll();
                if (i == levelSize - 1) out.add(node.data);   // the last one is visible
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        List<Integer> view = new ArrayList<>();
        rightSideView(root, view);

        System.out.println(join(view));
    }
}
