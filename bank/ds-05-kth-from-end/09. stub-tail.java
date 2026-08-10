
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
