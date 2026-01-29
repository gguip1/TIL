import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, Q;
    static int[][] school;

    static int search(int f) {
        int answer = -1;
        int max = -1;

        for (int i = 1; i < N + 1; i++) {
            if (school[f][i] > max) {
                answer = i;
                max = school[f][i];
            }
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        school = new int[4 + 1][N + 1];

        for (int i = 0; i < Q; i ++) {
            st = new StringTokenizer(br.readLine());

            if (Integer.parseInt(st.nextToken()) == 1) {
                int _floor = Integer.parseInt(st.nextToken());
                int _class = Integer.parseInt(st.nextToken());

                if (_floor - 1 > 0) school[_floor - 1][_class]++;
                if (_floor + 1 < 5)  school[_floor + 1][_class]++;
                if (_class - 1 > 0)  school[_floor][_class - 1]++;
                if (_class + 1 < N + 1)  school[_floor][_class + 1]++;
                school[_floor][_class]++;
            } else {
                int _floor = Integer.parseInt(st.nextToken());
                System.out.println(search(_floor));
            }
        }

        int mF = -1;
        int mC = -1;
        int mV = -1;

        for (int f = 1; f < 5; f++) {
            for (int c = 1; c < N + 1; c++) {
                if (school[f][c] > mV) {
                    mF = f;
                    mC = c;
                    mV = school[f][c];
                }
            }
        }

        System.out.println(mF + " " + mC);
    }
}
