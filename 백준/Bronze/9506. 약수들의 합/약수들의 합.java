import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            n = Integer.parseInt(br.readLine());

            if (n == -1) {
                break;
            }

            List<Integer> sums = new ArrayList<>();

            for (int i = 1; i < n; i++) {
                if (n % i == 0) {
                    sums.add(i);
                }
            }

            int sum = sums.stream().mapToInt(Integer::intValue).sum();

            if (sum == n) {
                System.out.print(n + " = ");

                var sj = new StringJoiner(" + ");
                for (int x : sums) sj.add(Integer.toString(x));

                System.out.println(sj);
            } else {
                System.out.printf("%d is NOT perfect.\n", n);
            }
        }
    }
}
