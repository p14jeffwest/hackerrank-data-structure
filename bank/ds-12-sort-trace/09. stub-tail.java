
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] a = readArray(br, n);
        int[] result = selectionPasses(a, k);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            if (i > 0) {
                sb.append(' ');
            }
            sb.append(result[i]);
        }
        sb.append('\n');
        System.out.print(sb);
    }
}
