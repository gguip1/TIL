import java.io.*;
import java.util.*;

public class Main {
    static int K;
    static int W, H;
    static int[][] map;
    static boolean[][][] visited;

    static class Monkey {
        int y, x, v, horseCount;

        Monkey(int y, int x, int v, int horseCount) {
            this.y = y;
            this.x = x;
            this.v = v;
            this.horseCount = horseCount;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        K = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        map = new int[H][W];
        visited = new boolean[H][W][K + 1];

        for (int i = 0; i < H; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < W; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Deque<Monkey> queue = new ArrayDeque<>();
        queue.add(new Monkey(0, 0, 0, 0));
        visited[0][0][0] = true;

        int[][] horseDeltas = {
                {-1, -2},
                {-2, -1},
                {-2, 1},
                {-1, 2},
                {1, -2},
                {2, -1},
                {2, 1},
                {1, 2}
        };

        int[][] deltas = {
                {1, 0},
                {0, 1},
                {-1, 0},
                {0, -1}
        };

        int answer = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            Monkey monkey = queue.poll();

            if (monkey.x == W - 1 && monkey.y == H - 1) {
                answer = Integer.min(answer, monkey.v);
            }

            for (int[] delta : deltas) {
                int newY = delta[0] + monkey.y;
                int newX = delta[1] + monkey.x;

                if (0 <= newY && newY < H && 0 <= newX && newX < W && map[newY][newX] == 0 && !visited[newY][newX][monkey.horseCount]) {
                    queue.add(new Monkey(newY, newX, monkey.v + 1, monkey.horseCount));
                    visited[newY][newX][monkey.horseCount] = true;
                }
            }

            if (monkey.horseCount < K) {
                for (int[] delta : horseDeltas) {
                    int newY = delta[0] + monkey.y;
                    int newX = delta[1] + monkey.x;

                    if (0 <= newY && newY < H && 0 <= newX && newX < W && map[newY][newX] == 0 && !visited[newY][newX][monkey.horseCount + 1]) {
                        queue.add(new Monkey(newY, newX,  monkey.v + 1,monkey.horseCount + 1));
                        visited[newY][newX][monkey.horseCount + 1] = true;
                    }
                }
            }
        }

        if (answer == Integer.MAX_VALUE) {
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
    }
}
