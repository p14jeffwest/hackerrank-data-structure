
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");
        Node root = build(tokens);

        int q = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        StringTokenizer tk = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int target = Integer.parseInt(tk.nextToken());
            sb.append(hasPathSum(root, target)).append('\n');
        }

        System.out.print(sb);
    }
}
