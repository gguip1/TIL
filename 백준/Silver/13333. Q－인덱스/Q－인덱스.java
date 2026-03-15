import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] theses;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        theses = new int[n];
        for (int i = 0; i < n; i++) {
            theses[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;

        for (int k = 0; k < 10_001; k++) {
            int cnt_1 = 0;
            int cnt_2 = 0;
            for (int i = 0; i < n; i++) {
                if (theses[i] >= k) {
                    cnt_1++;
                }
                if (theses[i] <= k) {
                    cnt_2++;
                }
            }

            if (cnt_1 >= k && cnt_2 <= k) {
                answer = k;
            }
        }

        System.out.println(answer);
    }
}
