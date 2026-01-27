import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] xs;
    static int[] prefixSum;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        xs = new int[n];
        prefixSum = new int[n + 1];

        for (int i = 0; i < n; i++) {
            xs[i] = Integer.parseInt(st.nextToken());
        }

        long answer = 0;

        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + xs[i];
        }

        for (int i = 0; i < n; i++) {
            answer += (long) xs[i] * (prefixSum[n] - prefixSum[i + 1]);
        }

        System.out.println(answer);
    }
}
