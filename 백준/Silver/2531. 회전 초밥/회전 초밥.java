import java.io.*;
import java.util.*;

public class Main {
    static int N, d, k, c;
    static int[] sushi;
    static int[] cnt;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        sushi = new int[N];

        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        cnt = new int[d + 1];

        int distinct = 0;
        for (int i = 0; i < k; i++) {
            int x = sushi[i];
            if (cnt[x] == 0) {
                distinct++;
            }
            cnt[x]++;
        }

        int answer = distinct;
        if (cnt[c] == 0) {
            answer++;
        }

        for (int i = 1; i < N; i++) {
            int out = sushi[i - 1];
            cnt[out]--;
            if (cnt[out] == 0) {
                distinct--;
            }

            int in = sushi[(i + k - 1) % N];
            if (cnt[in] == 0) {
                distinct++;
            }
            cnt[in]++;

            int cursor = distinct;
            if (cnt[c] == 0) {
                cursor++;
            }
            if (cursor > answer) {
                answer = cursor;
            }
        }

        System.out.println(answer);
    }
}
