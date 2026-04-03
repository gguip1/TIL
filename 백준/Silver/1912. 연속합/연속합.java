import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] sequence;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        sequence = new int[n];
        dp = new int[n];

        for (int i = 0; i < n; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = sequence[0];
        for (int i = 1; i < n; i++) {
            if (dp[i - 1] < 0) {
                dp[i] = sequence[i];
            } else {
                dp[i] = dp[i - 1] + sequence[i];
            }
        }

        int answer = dp[0];
        for (int x : dp) {
            if (x > answer) answer = x;
        }

        System.out.println(answer);
    }
}
