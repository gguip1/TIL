import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int[] A;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        A = new int[N];

        int[] diff = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        diff[0] = A[0];
        int answer = diff[0];
        for (int i = 1; i < N; i++) {
            diff[i] = A[i] - A[i - 1];
            answer += diff[i];
        }
        Arrays.sort(diff);

        for (int i = 1; i <= K; i++) {
            answer -= diff[N - i];
        }
        System.out.println(answer);
    }
}
