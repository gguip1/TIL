import java.io.*;
import java.util.*;

public class Main {
    static int[] array;
    static int[] memo;
    static boolean[] visited;

    static int bestEnd(int i) {
        if (visited[i]) return memo[i];
        visited[i] = true;

        if (i == 0) return memo[i] = array[0];
        return memo[i] = Math.max(array[i], array[i] + bestEnd(i - 1));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++){
            int N = Integer.parseInt(br.readLine());
            array = new int[N];
            memo = new int[N];
            visited = new boolean[N];

            StringTokenizer st = new StringTokenizer(br.readLine());
            int idx = 0;
            while (st.hasMoreTokens()) {
                array[idx++] = Integer.parseInt(st.nextToken());
            }

            int total_max = -9999;
            for (int j = 0; j < N; j++){
                total_max = Math.max(total_max, bestEnd(j));
            }

            System.out.println(total_max);
        }
    }
}