import java.io.*;
import java.util.*;

public class Main {
    static int N, S;
    static int[] arr;
    static long[] prefixSum;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        arr = new int[N + 1];
        prefixSum = new long[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        prefixSum[1] = arr[1];
        for (int i = 2; i < N + 1; i++) {
            prefixSum[i] = prefixSum[i - 1] + arr[i];
        }

        int left = 0;
        int right = 0;

        int length = Integer.MAX_VALUE;

        while (right < N + 1) {
            if (prefixSum[right] - prefixSum[left] >= S) {
                length = Integer.min(length, right - left);
            }

            if (prefixSum[right] - prefixSum[left] < S) {
                right++;
            } else {
                left++;
            }
        }

        if (length != Integer.MAX_VALUE) {
            System.out.println(length);
        } else {
            System.out.println(0);
        }
    }
}
