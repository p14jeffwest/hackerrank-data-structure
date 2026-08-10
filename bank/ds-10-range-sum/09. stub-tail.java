
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
