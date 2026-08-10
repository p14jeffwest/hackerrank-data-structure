
    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int t = (int) in.nval;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            in.nextToken();
            int a = (int) in.nval;
            in.nextToken();
            int b = (int) in.nval;
            sb.append(gcd(a, b)).append('\n');
        }

        System.out.print(sb);
    }
}
