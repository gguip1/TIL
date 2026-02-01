import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr;
    static int[] prefixSum1;
    static int[] prefixSum2;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N + 2];
        prefixSum1 = new int[N + 2];
        prefixSum2 = new int[N + 2];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= N; i++) {
            prefixSum1[i] = prefixSum1[i - 1] + arr[i];
        }

        for (int i = N; i > 0; i--) {
            prefixSum2[i] = prefixSum2[i + 1] + arr[i];
        }

        int answer = Integer.MIN_VALUE;

        for (int i = 2; i < N; i++) {
            answer = Integer.max(answer, (prefixSum1[N] - prefixSum1[1] - arr[i]) + (prefixSum1[N] - prefixSum1[i]));
        }

        for (int i = N - 1; i > 1; i--) {
            answer = Integer.max(answer, (prefixSum2[1] - prefixSum2[N] - arr[i]) + (prefixSum2[1] - prefixSum2[i]));
        }

        for (int i = 2; i < N; i++) {
            answer = Integer.max(answer, (prefixSum1[i] - prefixSum1[1]) + (prefixSum2[i] - prefixSum2[N]));
        }

        System.out.println(answer);
    }
}
