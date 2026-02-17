import java.io.*;
import java.util.*;

public class Main {
    static int T;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            long N = Long.parseLong(br.readLine());

            long left = 0;
            long right = 2000000000L; // right 크기 제한 10**16으로 할 시 long 오버플로우

            long answer = 0;

            while (left <= right) {
                long mid = (left + right) / 2;
                long value = (mid * (mid + 1)) / 2;

                if (N < value) {
                    right = mid - 1;
                } else {
                    answer = mid;
                    left = mid + 1;
                }
            }

            System.out.println(answer);
        }
    }
}
