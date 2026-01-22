import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] cows;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        cows = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            cows[i][0] = Integer.parseInt(st.nextToken());
            cows[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                if (cows[i][0] > cows[j][0]) {
                    int[] temp;
                    temp = cows[i];
                    cows[i] = cows[j];
                    cows[j] = temp;
                }

                if (cows[i][0] == cows[j][0]) {
                    if (cows[i][1] > cows[j][1]) {
                        int[] temp;
                        temp = cows[i];
                        cows[i] = cows[j];
                        cows[j] = temp;
                    }
                }
            }
        }

        int answer = 0;

        for (int i = 0; i < N; i++) {
            if (answer < cows[i][0]) {
                answer = cows[i][0];
            }
            answer += cows[i][1];
        }
        
        System.out.println(answer);
    }
}
