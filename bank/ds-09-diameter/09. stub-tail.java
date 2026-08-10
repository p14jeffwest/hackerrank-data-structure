
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        System.out.println(diameter(root));
    }
}
