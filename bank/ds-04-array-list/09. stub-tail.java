}

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int q = Integer.parseInt(br.readLine().trim());

        ListInterface<Integer> list = new Array_List<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < q; i++) {
            StringTokenizer t = new StringTokenizer(br.readLine());
            String op = t.nextToken();
            try {
                switch (op) {
                    case "add":
                        list.add(Integer.parseInt(t.nextToken()));
                        break;
                    case "addAt":
                        list.add(Integer.parseInt(t.nextToken()),
                                 Integer.parseInt(t.nextToken()));
                        break;
                    case "removeAt":
                        sb.append(list.remove(Integer.parseInt(t.nextToken())))
                          .append('\n');
                        break;
                    case "removeValue":
                        sb.append(list.remove((Integer) Integer.parseInt(t.nextToken())) ? 1 : 0)
                          .append('\n');
                        break;
                    case "get":
                        sb.append(list.get(Integer.parseInt(t.nextToken())))
                          .append('\n');
                        break;
                    case "indexOf":
                        sb.append(list.indexOf(Integer.parseInt(t.nextToken())))
                          .append('\n');
                        break;
                    case "size":
                        sb.append(list.size()).append('\n');
                        break;
                    case "print":
                        sb.append(list).append('\n');
                        break;
                    default:
                        break;
                }
            } catch (IndexOutOfBoundsException e) {
                sb.append("error").append('\n');
            }
        }

        System.out.print(sb);
    }
}
