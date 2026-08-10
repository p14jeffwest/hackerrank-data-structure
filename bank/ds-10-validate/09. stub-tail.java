
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            br.readLine();                              // number of tokens
            String[] tokens = br.readLine().trim().split("\\s+");
            sb.append(isValidBST(build(tokens))).append('\n');
        }

        System.out.print(sb);
    }
}
