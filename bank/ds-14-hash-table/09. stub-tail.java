
public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(br.readLine());
        int size = Integer.parseInt(header.nextToken());
        int m = Integer.parseInt(header.nextToken());

        HashTable table = new HashTable(size);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < m; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            switch (op) {
                case "put":
                    table.put(Integer.parseInt(t.nextToken()),
                              Integer.parseInt(t.nextToken()));
                    break;
                case "get":
                    sb.append(table.get(Integer.parseInt(t.nextToken()))).append('\n');
                    break;
                case "remove":
                    table.remove(Integer.parseInt(t.nextToken()));
                    break;
                case "print":
                    sb.append(table).append('\n');
                    break;
                default:
                    break;
            }
        }

        System.out.print(sb);
    }
}
