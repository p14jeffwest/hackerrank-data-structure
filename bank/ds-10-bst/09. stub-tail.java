
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
