
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();                                  // number of tokens
        String[] tokens = br.readLine().trim().split("\\s+");

        Node root = build(tokens);

        List<Integer> pre = new ArrayList<>();
        List<Integer> in = new ArrayList<>();
        List<Integer> post = new ArrayList<>();
        List<Integer> level = new ArrayList<>();
        preorder(root, pre);
        inorder(root, in);
        postorder(root, post);
        levelOrder(root, level);

        StringBuilder sb = new StringBuilder();
        sb.append(join(pre)).append('\n');
        sb.append(join(in)).append('\n');
        sb.append(join(post)).append('\n');
        sb.append(join(level)).append('\n');

        System.out.print(sb);
    }
}
