import java.io.*;
import java.util.*;

public class Main {
    static long A;
    static long B;

    static int gcd(long a, long b) {
        if (b == 0) {
            return (int) a;
        }
        return gcd(b, a % b);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        A = Long.parseLong(st.nextToken());
        B = Long.parseLong(st.nextToken());

        System.out.println("1".repeat(gcd(Math.max(A, B), Math.min(A, B))));
    }
}
