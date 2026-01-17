import java.io.*;
import java.util.*;

public class Main {
    static int T;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            String W = br.readLine();
            int K = Integer.parseInt(br.readLine());

            int[] alphabets = new int[26];
            for (int j = 0; j < W.length(); j++) {
                alphabets[W.charAt(j) % 97]++;
            }

            int min = Integer.MAX_VALUE;
            int max = -1;
            for (int j = 0; j < W.length(); j++) {
                if (alphabets[W.charAt(j) % 97] >= K) {
                    int count = 0;
                    for (int z = j; z < W.length(); z++) {
                        if (W.charAt(j) == W.charAt(z)) {
                            count++;
                        }
                        if (count == K) {
                            min = Math.min(min, z - j + 1);
                            max = Math.max(max, z - j +  1);
                            break;
                        }
                    }
                }
            }

            if (min == Integer.MIN_VALUE || max == -1) {
                System.out.println(-1);
            } else {
                System.out.println(min + " " + max);
            }
        }
    }
}
