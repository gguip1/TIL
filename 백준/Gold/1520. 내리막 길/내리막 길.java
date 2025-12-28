import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    static int M;
    static int N;
    static int[][] map;
    static int[][] dp;
    static int[][] deltas = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    static int dfs(int y, int x){
        if (y == M - 1 && x == N - 1){
            return 1;
        }

        if (dp[y][x] != -1){
            return dp[y][x];
        }

        dp[y][x] = 0;

        for (int[] delta : deltas){
            int dy = delta[0], dx = delta[1], ny = y + dy, nx = x + dx;

            if (0 <= ny && ny < M && 0 <= nx && nx < N && map[ny][nx] < map[y][x]){
                dp[y][x] += dfs(ny, nx);
            }
        }
        return dp[y][x];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        map = new int[M][N];
        dp = new int[M][N];
        IntStream.range(0, M)
                .forEach(i -> Arrays.fill(dp[i], -1));

        for (int i = 0; i < M; i++){
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(dfs(0, 0));
    }
}
