import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<Integer> W;
    static int answer = 0;

    static void dfs(List<Integer> arr, int energy) {
        if (arr.size() == 2) {
            answer = Math.max(answer, energy);
            return;
        }

        for (int i = 1; i < arr.size() - 1; i++) {
            int gain = arr.get(i - 1) * arr.get(i + 1);
            int removed = arr.remove(i);
            dfs(arr, energy + gain);
            arr.add(i, removed);
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        W = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            W.add(Integer.parseInt(st.nextToken()));
        }

        dfs(W, 0);
        System.out.println(answer);
    }
}
