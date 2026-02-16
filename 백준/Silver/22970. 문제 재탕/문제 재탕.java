import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] A;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        A = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for (int i = 0; i < N; i++) {
            boolean check = true;
            int temp = 0;
            int prev = 0;
            for (int j = i; j < N; j++) {
                if (check && A[j] > prev) {
                    temp++;
                } else if (check && A[j] < prev) {
                    temp++;
                    check = false;
                } else if (!check && A[j] < prev) {
                    temp++;
                } else {
                    break;
                }
                prev = A[j];
            }
            answer = Math.max(answer, temp);
        }
        System.out.println(answer);
    }
}
