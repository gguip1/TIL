import java.io.*;
import java.util.*;

public class Main {
    static class Item {
        int a, b;

        Item(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }

    static int K;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        Item[] dp = new Item[46];

        dp[0] = new Item(1, 0);

        for (int i = 1; i < 46; i++) {
            dp[i] = new Item(dp[i - 1].b, dp[i - 1].a + dp[i - 1].b);
        }

        System.out.println(dp[K].a + " " + dp[K].b);
    }
}
