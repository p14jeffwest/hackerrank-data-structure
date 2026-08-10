
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        StringBuilder sb = new StringBuilder();
        sb.append(countLeaves(root)).append('\n');
        sb.append(height(root)).append('\n');
        sb.append(maxDepth(root)).append('\n');

        System.out.print(sb);
    }
}
