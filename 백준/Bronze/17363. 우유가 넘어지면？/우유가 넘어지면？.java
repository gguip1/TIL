import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static String[] box;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        box = new String[N];
        for (int i = 0; i < N; i++) {
            box[i] = br.readLine();
        }

        for (int i = M - 1; i >= 0; i--) {
            for (int j = 0; j < N; j++) {
                char pC = box[j].charAt(i);
                switch (pC) {
                    case '-' : pC = '|'; break;
                    case '|' : pC = '-'; break;
                    case '/' : pC = '\\'; break;
                    case '\\' : pC = '/'; break;
                    case '^' : pC = '<'; break;
                    case '<' : pC = 'v'; break;
                    case 'v' : pC = '>'; break;
                    case '>' : pC = '^'; break;
                }
                System.out.print(pC);
            }
            System.out.println();
        }
    }
}
