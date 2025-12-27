import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] t = new int[N];
        int[] p = new int[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            t[i] = Integer.parseInt(st.nextToken());
            p[i] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[N + 1];
        int currentMax = 0;
        int ans = 0;

        for (int i = 0; i < N; i++) {
            currentMax = Math.max(currentMax, dp[i]);

            int next = i + t[i];
            if (next <= N) {
                dp[next] = Math.max(dp[next], currentMax + p[i]);
                ans = Math.max(ans, dp[next]);
            } else {
                ans = Math.max(ans, currentMax);
            }
        }

        ans = Math.max(ans, Math.max(currentMax, dp[N]));
        System.out.println(ans);
    }
}
