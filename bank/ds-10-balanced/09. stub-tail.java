
    public static void main(String[] args) throws IOException {
        StreamTokenizer in = new StreamTokenizer(
                new BufferedReader(new InputStreamReader(System.in)));

        in.nextToken();
        int n = (int) in.nval;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            nums[i] = (int) in.nval;
        }

        Node root = sortedArrayToBST(nums);

        StringBuilder sb = new StringBuilder();
        preorder(root, sb);
        sb.append('\n').append(height(root)).append('\n');

        System.out.print(sb);
    }
}
