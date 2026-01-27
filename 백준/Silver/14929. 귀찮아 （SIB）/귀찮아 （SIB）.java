import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] xs;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        xs = new int[n];

        for (int i = 0; i < n; i++) {
            xs[i] = Integer.parseInt(st.nextToken());
        }

        long answer = 0;

        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                answer += (long) xs[a] * xs[b];
            }
        }

        System.out.println(answer);
    }
}
