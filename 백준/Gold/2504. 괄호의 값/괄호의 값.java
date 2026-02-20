import java.io.*;
import java.util.*;

public class Main {
    static String string;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        string = br.readLine();

        List<Object> stack = new ArrayList<>();
        int answer = 0;

        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);

            if (c == '(' || c == '[') {
                stack.add(c);
            }
            else {
                int sum = 0;

                while (!stack.isEmpty() && stack.get(stack.size() - 1) instanceof Integer) {
                    sum += (int) stack.remove(stack.size() - 1);
                }

                if (stack.isEmpty()) {
                    System.out.println(0);
                    System.exit(0);
                }

                char open = (char) stack.remove(stack.size() - 1);

                if (c == ')' && open != '(' ||
                    c == ']' && open != '[') {
                    System.out.println(0);
                    System.exit(0);
                }

                stack.add(sum == 0 ? (c == ')' ? 2 : 3) : sum * (c == ')' ? 2 : 3));
            }
        }

        for (int i = 0; i < stack.size(); i++) {
            if (stack.get(i) instanceof Character) {
                System.out.println(0);
                System.exit(0);
            }
            answer += (int) stack.get(i);
        }

        System.out.println(answer);
    }
}
