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

    // Two pointers, one pass.
    //
    // Send `fast` k steps ahead, then move both one step at a time. The gap
    // between them stays exactly k, so when `fast` runs off the end `slow`
    // sits k nodes from it -- which is the k-th node from the end.
    //
    // The list length is never computed, and no node is ever visited twice.
    // O(n) time, O(1) extra space.

    public static int kthFromEnd(Node head, int k) {
        Node fast = head;
        for (int i = 0; i < k; i++) {
            fast = fast.next;
        }

        Node slow = head;
        while (fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow.data;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            StringTokenizer header = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(header.nextToken());
            int k = Integer.parseInt(header.nextToken());

            // build the list, keeping only head
            Node head = null;
            Node tail = null;
            StringTokenizer values = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                Node node = new Node(Integer.parseInt(values.nextToken()));
                if (head == null) {
                    head = node;
                    tail = node;
                } else {
                    tail.next = node;
                    tail = node;
                }
            }

            sb.append(kthFromEnd(head, k)).append('\n');
        }

        System.out.print(sb);
    }
}
