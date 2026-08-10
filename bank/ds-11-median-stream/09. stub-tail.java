
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine().trim());

        MedianFinder mf = new MedianFinder();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            if (op.equals("add")) {
                mf.addNum(Integer.parseInt(t.nextToken()));
            } else if (op.equals("median")) {
                if (mf.size() == 0) {
                    sb.append("empty").append('\n');
                } else {
                    sb.append(String.format(Locale.ROOT, "%.1f", mf.findMedian()))
                      .append('\n');
                }
            } else if (op.equals("size")) {
                sb.append(mf.size()).append('\n');
            }
        }

        System.out.print(sb);
    }
}
