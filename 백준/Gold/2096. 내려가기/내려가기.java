import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] numbers;
    static int[][] maxMemos;
    static int[][] minMemos;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        numbers = new int[N][3];

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            numbers[i][0] = Integer.parseInt(st.nextToken());
            numbers[i][1] = Integer.parseInt(st.nextToken());
            numbers[i][2] = Integer.parseInt(st.nextToken());
        }

        maxMemos = new int[N][3];
        minMemos = new int[N][3];

        maxMemos[0] = numbers[0];
        minMemos[0] = numbers[0];

        for (int i = 0; i < N - 1; i++) {
            maxMemos[i + 1][0] = Math.max(maxMemos[i][0] + numbers[i + 1][0], maxMemos[i][1] + numbers[i + 1][0]);
            maxMemos[i + 1][1] = Math.max(
                    Math.max(maxMemos[i][0] + numbers[i + 1][1],
                            maxMemos[i][1] + numbers[i + 1][1]),
                    maxMemos[i][2] + numbers[i + 1][1]
            );
            maxMemos[i + 1][2] = Math.max(maxMemos[i][1] + numbers[i + 1][2], maxMemos[i][2] + numbers[i + 1][2]);

            minMemos[i + 1][0] = Math.min(minMemos[i][0] + numbers[i + 1][0], minMemos[i][1] + numbers[i + 1][0]);
            minMemos[i + 1][1] = Math.min(
                    Math.min(minMemos[i][0] + numbers[i + 1][1],
                            minMemos[i][1] + numbers[i + 1][1]),
                    minMemos[i][2] + numbers[i + 1][1]
            );
            minMemos[i + 1][2] = Math.min(minMemos[i][1] + numbers[i + 1][2], minMemos[i][2] + numbers[i + 1][2]);
        }

        System.out.print(Math.max(
                Math.max(maxMemos[N - 1][0],
                        maxMemos[N - 1][1]),
                maxMemos[N - 1][2]
        ) + " ");

        System.out.println(Math.min(
                Math.min(minMemos[N - 1][0],
                        minMemos[N - 1][1]),
                minMemos[N - 1][2]
        ));
    }
}
