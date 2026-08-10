import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Solution {

    // A dummy head removes the special case of choosing the first node.
    // Without it, the first comparison has to decide which list starts the
    // result and set the head; with it, the loop body is the same every time
    // and the answer is simply dummy.next.
    //
    // Nothing is allocated except the dummy: each step re-points current.next
    // at a node that already exists. When one list runs out, the other is
    // attached whole -- its nodes are already in order, so there is nothing
    // left to compare.
    //
    // O(n + m) time. The driver checks that the merged list is exactly the
    // nodes it handed over, so copying values into fresh nodes is reported as
    // invalid rather than accepted.

    public static Node mergeSorted(Node head1, Node head2) {
        Node dummy = new Node(0);
        Node current = dummy;

        while (head1 != null && head2 != null) {
            if (head1.data <= head2.data) {
                current.next = head1;
                head1 = head1.next;
            } else {
                current.next = head2;
                head2 = head2.next;
            }
            current = current.next;
        }
        current.next = (head1 != null) ? head1 : head2;

        return dummy.next;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(header.nextToken());
            int m = Integer.parseInt(header.nextToken());

            // every node handed to mergeSorted is registered here, so that the
            // merged list can be checked against the nodes that were given
            IdentityHashMap<Node, Boolean> given = new IdentityHashMap<>();

            Node head1 = build(br.readLine(), n, given);
            Node head2 = build(br.readLine(), m, given);

            Node merged = mergeSorted(head1, head2);

            sb.append(render(merged, given, n + m)).append('\n');
        }

        System.out.print(sb);
    }

    private static Node build(String line, int count, IdentityHashMap<Node, Boolean> given) {
        Node head = null;
        Node tail = null;
        StringTokenizer values = new StringTokenizer(line);
        for (int i = 0; i < count; i++) {
            Node node = new Node(Integer.parseInt(values.nextToken()));
            given.put(node, Boolean.TRUE);
            if (head == null) {
                head = node;
                tail = node;
            } else {
                tail.next = node;
                tail = node;
            }
        }
        return head;
    }

    private static String render(Node result, IdentityHashMap<Node, Boolean> given, int total) {
        StringBuilder sb = new StringBuilder();
        IdentityHashMap<Node, Boolean> seen = new IdentityHashMap<>();
        int count = 0;

        for (Node current = result; current != null; current = current.next) {
            if (!given.containsKey(current)) return "invalid";      // not one of ours
            if (seen.put(current, Boolean.TRUE) != null) return "invalid";  // seen twice
            if (count > 0) sb.append(' ');
            sb.append(current.data);
            count++;
        }
        if (count != total) return "invalid";                       // nodes lost
        return count == 0 ? "(empty)" : sb.toString();
    }
}
