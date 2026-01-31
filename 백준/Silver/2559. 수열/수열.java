import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[] temperatures;
    static int[] prefixSum;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        temperatures = new int[N + 1];
        prefixSum = new int[N + 1];

        st = new StringTokenizer(br.readLine());

        for (int i = 1; i < N + 1; i++) {
            temperatures[i] = Integer.parseInt(st.nextToken());
        }

        prefixSum[1] = temperatures[1];

        for (int i = 2; i < N + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + temperatures[i];
        }

        int answer = Integer.MIN_VALUE;

        for (int i = K; i < N + 1; i++) {
            answer = Integer.max(answer, prefixSum[i] - prefixSum[i - K]);
        }

        System.out.println(answer);
    }
}
