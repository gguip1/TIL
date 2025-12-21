import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {
    static class Pair {
        int a, b;
        Pair(int a, int b) { this.a = a; this.b = b; }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        List<Pair> pairs = new ArrayList<>();

        for (int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            pairs.add(new Pair(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        pairs.sort(
                Comparator.comparingInt((Pair p) -> p.a)
        );

        int current = 0;
        int answer = 0;

//        for (Pair p : pairs){
//            if (current < p.a){
//                current = p.a;
//            }
//
//            while (current < p.b){
//                current += L;
//                answer += 1;
//            }
//        }

        for (Pair p : pairs){
            if (current < p.a){
                current = p.a;
            }

            if (current < p.b) {
                int v = p.b - current;
                int k = (v + L - 1) / L;
                current += k * L;
                answer += k;
            }
        }

        System.out.println(answer);
    }
}