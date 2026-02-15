import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] map;
    static boolean[][][] visited;

    static class Node {
        int y, x, v;
        boolean hasBroken;

        Node(int y, int x, int v, boolean hasBroken) {
            this.y = y;
            this.x = x;
            this.v = v;
            this.hasBroken = hasBroken;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited = new boolean[N][M][2];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for(int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt("" + line.charAt(j));
            }
        }

        if (N == 1 && M == 1) {
            System.out.println(1);
            System.exit(0);
        }

        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(0, 0, 1, false));
        visited[0][0][0] = true;

        int[][] deltas = {
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1}
        };

        int answer = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            for (int[] delta : deltas) {
                int newY = node.y + delta[0];
                int newX = node.x + delta[1];

                if (0 <= newY && newY < N && 0 <= newX && newX < M && !visited[newY][newX][node.hasBroken ? 1 : 0]) {
                    if (map[newY][newX] == 0) {
                        queue.add(new Node(newY, newX, node.v + 1, node.hasBroken));
                        visited[newY][newX][node.hasBroken ? 1 : 0] = true;
                        if (newY == N - 1 && newX == M - 1) answer = Math.min(answer, node.v + 1);
                    } else {
                        if (!node.hasBroken && !visited[newY][newX][1]) { // 벽은 상태 1
                            visited[newY][newX][1] = true;
                            queue.add(new Node(newY, newX, node.v + 1, true));
                            if (newY == N - 1 && newX == M - 1) answer = Math.min(answer, node.v + 1);
                        }
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
