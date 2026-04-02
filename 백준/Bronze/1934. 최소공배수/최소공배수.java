import java.io.*;
import java.util.*;

public class Main {
    static int T;

    static int gcd(int x, int y) {

        while (x % y != 0) {
            int temp = x;
            x = y;
            y = temp % y;
        }

        return y;
    }

    static long lcm(int x, int y) {
        return (long) x / gcd(x, y) * y;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        StringTokenizer st;

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            System.out.println(lcm(Math.max(A, B), Math.min(A, B)));
        }
    }
}
