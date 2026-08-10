
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
