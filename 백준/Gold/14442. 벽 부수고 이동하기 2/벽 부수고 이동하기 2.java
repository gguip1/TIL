import java.io.*;
import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] map;
    static boolean[][][] visited;

    static class Node {
        int y, x, v, brokenCount;

        Node(int y, int x, int v, int brokenCount) {
            this.y = y;
            this.x = x;
            this.v = v;
            this.brokenCount = brokenCount;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt("" + line.charAt(j));
            }
        }

        visited = new boolean[N][M][K + 1];
        visited[0][0][0] = true;

        Deque<Node> queue = new ArrayDeque<>();
        queue.add(new Node(0, 0, 1, 0));

        int[][] deltas = {
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1},
        };

        int answer = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            Node node = queue.poll();

            if (node.y == N - 1 && node.x == M - 1) {
                answer = Integer.min(answer, node.v);
            }

            for (int[] delta : deltas) {
                int newY = delta[0] + node.y;
                int newX = delta[1] + node.x;

                if (0 <= newY && newY < N && 0 <= newX && newX < M && !visited[newY][newX][node.brokenCount]) {
                    if (map[newY][newX] == 0) {
                        queue.add(new Node(newY, newX, node.v + 1, node.brokenCount));
                        visited[newY][newX][node.brokenCount] = true;
                    } else {
                        if (node.brokenCount < K && !visited[newY][newX][node.brokenCount]) {
                            queue.add(new Node(newY, newX, node.v + 1, node.brokenCount + 1));
                            visited[newY][newX][node.brokenCount] = true;
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
