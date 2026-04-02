import java.io.*;
import java.util.*;

public class Main {
    static int G;
    static int L;

    static long gcd(long a, long b) {
        while (a % b != 0) {
            long temp = a;
            a = b;
            b = temp % b;
        }
        return b;
    }

    static long lcm(int a, int b) {
        return (long) a * b / gcd(a, b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        G = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        long target = L / G;
        long[] answer = new long[]{Long.MAX_VALUE, 0, 0};

        for (long a = 1; a <= target; a++) {
            if (target % a != 0) continue;

            long b = target / a;

            if (gcd(a, b) == 1 && answer[0] > a + b) {
                answer[0] = a + b;
                answer[1] = (long) G * a;
                answer[2] = (long) G * b;
            }
        }

        System.out.println(answer[1] + " " + answer[2]);
    }
}
